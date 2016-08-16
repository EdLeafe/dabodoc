
.. include:: _static/headings.txt

.. module:: dabo.ui.dialogs.infoMessage

.. _dabo.ui.dialogs.infoMessage.LblMessage:

===============================================
|doc_title|  **infoMessage.LblMessage** - class
===============================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **LblMessage**

.. inheritance-diagram:: LblMessage


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dLabel.dLabel`



|API| Class API
===============


.. autoclass:: dabo.ui.dialogs.infoMessage.LblMessage


|method_summary| Properties Summary
===================================


======================================= ========================
:ref:`Application <no-8227>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`AutoResize <no-8228>`             Specifies whether the length of the caption determines
:ref:`BackColor <no-8229>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-8230>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-8231>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-8232>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-8233>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-8234>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-8235>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-8236>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-8237>`                The caption of the object. (str)
:ref:`Children <no-8238>`               Returns a list of object references to the children of
:ref:`Class <no-8239>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-8240>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-8241>`   Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-8242>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-8243>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-8244>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-8245>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-8246>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-8247>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-8248>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-8249>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-8250>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-8251>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-8252>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-8253>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-8254>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-8255>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-8256>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-8257>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-8258>`          Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-8259>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-8260>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-8261>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-8262>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-8263>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-8264>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-8265>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-8266>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-8267>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-8268>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-8269>`           Dynamically determine the value of the Width property.
:ref:`DynamicWordWrap <no-8270>`        Dynamically determine the value of the WordWrap property.
:ref:`Enabled <no-8271>`                Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-8272>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-8273>`               Sets the Bold of the Font (int)
:ref:`FontDescription <no-8274>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-8275>`               Sets the face of the Font (int)
:ref:`FontInfo <no-8276>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-8277>`             Sets the Italic of the Font (int)
:ref:`FontSize <no-8278>`               Sets the size of the Font (int)
:ref:`FontUnderline <no-8279>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-8280>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-8281>`                   Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-8282>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-8283>`        Specifies the context-sensitive help text associated with this
:ref:`Hover <no-8284>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-8285>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-8286>`              Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-8287>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-8288>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-8289>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-8290>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-8291>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-8292>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-8293>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-8294>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-8295>`               Specifies the base name of the object.
:ref:`Parent <no-8296>`                 The containing object. (obj)
:ref:`Position <no-8297>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-8298>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-8299>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-8300>`                  The position of the right side of the object. This is a
:ref:`Size <no-8301>`                   The size of the object. (tuple)
:ref:`Sizer <no-8302>`                  The sizer for the object.
:ref:`StatusText <no-8303>`             Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-8304>`                Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-8305>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-8306>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-8307>`                    The top position of the object. (int)
:ref:`Transparency <no-8308>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-8309>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-8310>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-8311>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-8312>`                  The width of the object. (int)
:ref:`WindowHandle <no-8313>`           The platform-specific handle for the window. Read-only. (long)
:ref:`WordWrap <no-8314>`               When True, the Caption is wrapped to the Width. Note

======================================= ========================


Properties - inherited
========================

.. _no-8227:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-8228:

**AutoResize** 

Specifies whether the length of the caption determines
    the size of the label. This cannot be True if WordWrap is
    also set to True. Default=True.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dLabel.dLabel`

-------

.. _no-8229:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8230:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-8231:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-8232:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8233:

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

.. _no-8234:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8235:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8236:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-8237:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8238:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-8239:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-8240:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8241:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8242:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8243:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8244:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8245:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8246:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8247:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8248:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8249:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8250:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8251:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8252:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8253:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8254:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8255:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8256:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8257:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8258:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8259:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8260:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8261:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8262:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8263:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8264:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8265:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8266:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8267:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8268:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8269:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8270:

**DynamicWordWrap** 

Dynamically determine the value of the WordWrap property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
WordWrap property. If DynamicWordWrap is set to None (the default), WordWrap
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dLabel.dLabel`

-------

.. _no-8271:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-8272:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-8273:

**FontBold** 

Sets the Bold of the Font (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8274:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8275:

**FontFace** 

Sets the face of the Font (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8276:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8277:

**FontItalic** 

Sets the Italic of the Font (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8278:

**FontSize** 

Sets the size of the Font (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8279:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8280:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8281:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-8282:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8283:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8284:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8285:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8286:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-8287:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8288:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8289:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8290:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8291:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8292:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8293:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8294:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-8295:

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

.. _no-8296:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-8297:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-8298:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-8299:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8300:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-8301:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-8302:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-8303:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8304:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-8305:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8306:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8307:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8308:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8309:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8310:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8311:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8312:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8313:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8314:

**WordWrap** 

When True, the Caption is wrapped to the Width. Note
    that the control must have sufficient Height to display any
    wrapped text.
    Default=False  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dLabel.dLabel`

-------


|method_summary| Events Summary
===============================


======================================= ========================
:ref:`BackgroundErased <no-8315>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-8316>`                 Occurs after the control or form is created.
:ref:`Destroy <no-8317>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-8318>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-8319>`               Occurs when the control gets the focus.
:ref:`Idle <no-8320>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-8321>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-8322>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-8323>`               
:ref:`KeyUp <no-8324>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-8325>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-8326>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-8327>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-8328>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-8329>`             
:ref:`MouseLeave <no-8330>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-8331>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-8332>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-8333>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-8334>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-8335>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-8336>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-8337>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-8338>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-8339>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-8340>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-8341>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-8342>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-8343>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-8344>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-8345>`                   Occurs when the control's position changes.
:ref:`Paint <no-8346>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-8347>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-8348>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-8349>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-8350>`                 Occurs when a container wants its controls to update

======================================= ========================


Events
=======

.. _no-8315:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-8316:

**Create** 

Occurs after the control or form is created.



-------

.. _no-8317:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-8318:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-8319:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-8320:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-8321:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-8322:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-8323:

**KeyEvent** 



-------

.. _no-8324:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-8325:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-8326:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-8327:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-8328:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-8329:

**MouseEvent** 



-------

.. _no-8330:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-8331:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-8332:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-8333:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-8334:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-8335:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-8336:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-8337:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-8338:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-8339:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-8340:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-8341:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-8342:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-8343:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-8344:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-8345:

**Move** 

Occurs when the control's position changes.



-------

.. _no-8346:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-8347:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-8348:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-8349:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-8350:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


====================================== ========================
:ref:`absoluteCoordinates <no-8351>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-8352>`             Instantiate object as a child of self.
:ref:`afterInit <no-8353>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-8354>`          
:ref:`afterSetProperties <no-8355>`    
:ref:`autoBindEvents <no-8356>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-8357>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-8358>`   
:ref:`bindEvent <no-8359>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-8360>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-8361>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-8362>`          Makes this object topmost
:ref:`clear <no-8363>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-8364>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-8365>`  Given a position relative to this control, return a position relative
:ref:`copy <no-8366>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-8367>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-8368>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-8369>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-8370>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-8371>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-8372>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-8373>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-8374>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-8375>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-8376>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-8377>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-8378>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-8379>`              Draws text on the object at the specified position
:ref:`endHover <no-8380>`              
:ref:`fitToSizer <no-8381>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-8382>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-8383>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-8384>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-8385>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-8386>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-8387>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-8388>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-8389>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-8390>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-8391>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-8392>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-8393>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-8394>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-8395>`                  Make the object invisible.
:ref:`initEvents <no-8396>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-8397>`        
:ref:`isContainedBy <no-8398>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-8399>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-8400>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-8401>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-8402>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-8403>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-8404>`               
:ref:`paste <no-8405>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-8406>`           
:ref:`processDroppedFiles <no-8407>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-8408>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-8409>`            Raise the passed Dabo event.
:ref:`reCreate <no-8410>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-8411>`              Recreate the object.
:ref:`redraw <no-8412>`                Called when the object is (re)drawn.
:ref:`refresh <no-8413>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-8414>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-8415>`               Destroys the object.
:ref:`removeDrawnObject <no-8416>`     
:ref:`sendToBack <no-8417>`            Places this object behind all others.
:ref:`setAll <no-8418>`                Set all child object properties to the passed value.
:ref:`setFocus <no-8419>`              Sets focus to the object.
:ref:`setPositionInSizer <no-8420>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-8421>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-8422>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-8423>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-8424>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-8425>`                  Make the object visible.
:ref:`showContainingPage <no-8426>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-8427>`       Display a context menu (popup) at the specified position.
:ref:`super <no-8428>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-8429>`           Remove a previously registered event binding.
:ref:`unbindKey <no-8430>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-8431>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-8432>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-8433>`                Update the properties of this object and all contained objects.

====================================== ========================


Methods
=======

.. _no-8397:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.initProperties(self)



-------


Methods - inherited
=====================

.. _no-8351:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8352:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-8353:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-8354:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8355:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8356:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.autoBindEvents(self, force=True)
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

.. _no-8357:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-8358:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8359:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-8360:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-8361:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-8362:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8363:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8364:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8365:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8366:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8367:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8368:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8369:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8370:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-8371:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8372:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8373:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8374:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8375:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8376:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8377:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8378:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8379:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8380:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8381:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8382:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-8383:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-8384:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-8385:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8386:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-8387:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8388:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8389:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8390:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8391:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8392:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-8393:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8394:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8395:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8396:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-8398:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8399:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-8400:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.lockDisplay(self)
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

.. _no-8401:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8402:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8403:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8404:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8405:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8406:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8407:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8408:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8409:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8410:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-8411:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8412:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8413:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8414:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8415:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8416:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8417:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8418:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-8419:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8420:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8421:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-8422:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-8423:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8424:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8425:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8426:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8427:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8428:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-8429:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-8430:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8431:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8432:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-8433:

.. function:: dabo.ui.dialogs.infoMessage.LblMessage.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
