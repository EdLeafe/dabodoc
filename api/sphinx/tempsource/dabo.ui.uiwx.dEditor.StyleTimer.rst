
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dEditor

.. _dabo.ui.uiwx.dEditor.StyleTimer:

===========================================
|doc_title|  **dEditor.StyleTimer** - class
===========================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **StyleTimer**

.. inheritance-diagram:: StyleTimer


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dTimer.dTimer`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dEditor.StyleTimer


|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-23060>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-23061>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-23062>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-23063>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-23064>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-23065>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-23066>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-23067>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-23068>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-23069>`                The caption of the object. (str)
:ref:`Children <no-23070>`               Returns a list of object references to the children of
:ref:`Class <no-23071>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-23072>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-23073>`   Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-23074>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-23075>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-23076>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-23077>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-23078>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-23079>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-23080>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-23081>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-23082>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-23083>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-23084>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-23085>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-23086>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-23087>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-23088>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-23089>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-23090>`          Dynamically determine the value of the Height property.
:ref:`DynamicInterval <no-23091>`        Dynamically determine the value of the Interval property.
:ref:`DynamicLeft <no-23092>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-23093>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-23094>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-23095>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-23096>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-23097>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-23098>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-23099>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-23100>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-23101>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-23102>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-23103>`                Alternative means of starting/stopping the timer, or determining
:ref:`Font <no-23104>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-23105>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-23106>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-23107>`               Specifies the font face. (str)
:ref:`FontInfo <no-23108>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-23109>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-23110>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-23111>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-23112>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-23113>`                   Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-23114>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-23115>`        Specifies the context-sensitive help text associated with this
:ref:`Hover <no-23116>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Interval <no-23117>`               Specifies the timer interval (milliseconds).
:ref:`Left <no-23118>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-23119>`              Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-23120>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-23121>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-23122>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-23123>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-23124>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-23125>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-23126>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-23127>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-23128>`               Specifies the base name of the object.
:ref:`Parent <no-23129>`                 The containing object. (obj)
:ref:`Position <no-23130>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-23131>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-23132>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-23133>`                  The position of the right side of the object. This is a
:ref:`Size <no-23134>`                   The size of the object. (tuple)
:ref:`Sizer <no-23135>`                  The sizer for the object.
:ref:`StatusText <no-23136>`             Specifies the text that displays in the form's status bar, if any.
:ref:`Tag <no-23137>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-23138>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-23139>`                    The top position of the object. (int)
:ref:`Transparency <no-23140>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-23141>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-23142>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-23143>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-23144>`                  The width of the object. (int)
:ref:`WindowHandle <no-23145>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties - inherited
========================

.. _no-23060:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23061:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23062:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23063:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23064:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23065:

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

.. _no-23066:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23067:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23068:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-23069:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23070:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-23071:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23072:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23073:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23074:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23075:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23076:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23077:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23078:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23079:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23080:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23081:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23082:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23083:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23084:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23085:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23086:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23087:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23088:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23089:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23090:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23091:

**DynamicInterval** 

Dynamically determine the value of the Interval property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Interval property. If DynamicInterval is set to None (the default), Interval
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dTimer.dTimer`

-------

.. _no-23092:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23093:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23094:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23095:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23096:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23097:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23098:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23099:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23100:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23101:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23102:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23103:

**Enabled** 

Alternative means of starting/stopping the timer, or determining
    its status. If Enabled is set to True and the timer has a positive value
    for its Interval, the timer will be started.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23104:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23105:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23106:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23107:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23108:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23109:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23110:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23111:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23112:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23113:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-23114:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23115:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23116:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23117:

**Interval** 

Specifies the timer interval (milliseconds).


Inherited from: :ref:`dabo.ui.uiwx.dTimer.dTimer`

-------

.. _no-23118:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23119:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23120:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23121:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23122:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23123:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23124:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23125:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23126:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23127:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23128:

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

.. _no-23129:

**Parent** 

The containing object. (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23130:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23131:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23132:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23133:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-23134:

**Size** 

The size of the object. (tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23135:

**Sizer** 

The sizer for the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23136:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23137:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23138:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23139:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23140:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23141:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23142:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23143:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23144:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23145:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-23146>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-23147>`                 Occurs after the control or form is created.
:ref:`Destroy <no-23148>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-23149>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-23150>`               Occurs when the control gets the focus.
:ref:`Hit <no-23151>`                    Occurs with the control's default event (button click,
:ref:`Idle <no-23152>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-23153>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-23154>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-23155>`               
:ref:`KeyUp <no-23156>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-23157>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-23158>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-23159>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-23160>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-23161>`             
:ref:`MouseLeave <no-23162>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-23163>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-23164>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-23165>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-23166>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-23167>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-23168>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-23169>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-23170>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-23171>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-23172>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-23173>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-23174>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-23175>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-23176>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-23177>`                   Occurs when the control's position changes.
:ref:`Paint <no-23178>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-23179>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-23180>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-23181>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-23182>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-23146:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-23147:

**Create** 

Occurs after the control or form is created.



-------

.. _no-23148:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-23149:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-23150:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-23151:

**Hit** 

Occurs with the control's default event (button click,
listbox pick, checkbox, etc.)




-------

.. _no-23152:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-23153:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-23154:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-23155:

**KeyEvent** 



-------

.. _no-23156:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-23157:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-23158:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-23159:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-23160:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-23161:

**MouseEvent** 



-------

.. _no-23162:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-23163:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-23164:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-23165:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-23166:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-23167:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-23168:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-23169:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-23170:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-23171:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-23172:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-23173:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-23174:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-23175:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-23176:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-23177:

**Move** 

Occurs when the control's position changes.



-------

.. _no-23178:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-23179:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-23180:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-23181:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-23182:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-23183>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-23184>`             Instantiate object as a child of self.
:ref:`afterInit <no-23185>`             
:ref:`afterInitAll <no-23186>`          
:ref:`afterSetProperties <no-23187>`    
:ref:`autoBindEvents <no-23188>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-23189>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-23190>`   
:ref:`bindEvent <no-23191>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-23192>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-23193>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-23194>`          Makes this object topmost
:ref:`clear <no-23195>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-23196>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-23197>`  Given a position relative to this control, return a position relative
:ref:`copy <no-23198>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-23199>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-23200>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-23201>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-23202>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-23203>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-23204>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-23205>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-23206>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-23207>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-23208>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-23209>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-23210>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-23211>`              Draws text on the object at the specified position
:ref:`endHover <no-23212>`              
:ref:`fitToSizer <no-23213>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-23214>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-23215>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-23216>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-23217>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-23218>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-23219>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-23220>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-23221>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-23222>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-23223>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-23224>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-23225>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-23226>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-23227>`                  Make the object invisible.
:ref:`initEvents <no-23228>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-23229>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-23230>`         Returns True if the containership hierarchy for this control
:ref:`isRunning <no-23231>`             
:ref:`iterateCall <no-23232>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-23233>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-23234>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-23235>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-23236>`     Given a position relative to the form, return a position relative
:ref:`onHit <no-23237>`                 
:ref:`onHover <no-23238>`               
:ref:`paste <no-23239>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-23240>`           
:ref:`processDroppedFiles <no-23241>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-23242>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-23243>`            Raise the passed Dabo event.
:ref:`reCreate <no-23244>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-23245>`              Recreate the object.
:ref:`redraw <no-23246>`                Called when the object is (re)drawn.
:ref:`refresh <no-23247>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-23248>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-23249>`               Make sure that the timer is stopped first
:ref:`removeDrawnObject <no-23250>`     
:ref:`sendToBack <no-23251>`            Places this object behind all others.
:ref:`setAll <no-23252>`                Set all child object properties to the passed value.
:ref:`setFocus <no-23253>`              Sets focus to the object.
:ref:`setPositionInSizer <no-23254>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-23255>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-23256>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-23257>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-23258>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-23259>`                  Make the object visible.
:ref:`showContainingPage <no-23260>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-23261>`       Display a context menu (popup) at the specified position.
:ref:`start <no-23262>`                 
:ref:`stop <no-23263>`                  
:ref:`super <no-23264>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-23265>`           Remove a previously registered event binding.
:ref:`unbindKey <no-23266>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-23267>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-23268>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-23269>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods
=======

.. _no-23185:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.afterInit(self)



-------

.. _no-23237:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.onHit(self, evt)



-------


Methods - inherited
=====================

.. _no-23183:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23184:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-23186:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23187:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23188:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.autoBindEvents(self, force=True)
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

.. _no-23189:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23190:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23191:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-23192:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-23193:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-23194:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23195:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23196:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23197:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23198:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23199:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23200:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23201:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23202:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-23203:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23204:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23205:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23206:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23207:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23208:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23209:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23210:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23211:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23212:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23213:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23214:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-23215:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-23216:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-23217:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23218:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23219:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23220:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23221:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23222:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23223:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23224:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-23225:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23226:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23227:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23228:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23229:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23230:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23231:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.isRunning(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dTimer.dTimer`

-------

.. _no-23232:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-23233:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.lockDisplay(self)
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

.. _no-23234:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23235:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23236:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23238:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23239:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23240:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23241:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23242:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23243:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23244:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-23245:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23246:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23247:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23248:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23249:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.release(self)
   :noindex:


   Make sure that the timer is stopped first


Inherited from: :ref:`dabo.ui.uiwx.dTimer.dTimer`

-------

.. _no-23250:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23251:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23252:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-23253:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23254:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23255:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-23256:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-23257:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23258:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23259:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23260:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23261:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23262:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.start(self, interval=-1)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dTimer.dTimer`

-------

.. _no-23263:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.stop(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dTimer.dTimer`

-------

.. _no-23264:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-23265:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-23266:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23267:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23268:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-23269:

.. function:: dabo.ui.uiwx.dEditor.StyleTimer.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
