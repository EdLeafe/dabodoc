
.. include:: _static/headings.txt

.. module:: dabo.lib.datanav.Page

.. _dabo.lib.datanav.Page.SelectPage:

========================================
|doc_title|  **Page.SelectPage** - class
========================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **SelectPage**

.. inheritance-diagram:: SelectPage


|supclasses| Known Superclasses
===============================

* :ref:`dabo.lib.datanav.Page.Page`



|API| Class API
===============


.. autoclass:: dabo.lib.datanav.Page.SelectPage


|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-4119>`             Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-4120>`               Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-4121>`               The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-4122>`             Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-4123>`             Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-4124>`         Style of line for the border drawn around the control.
:ref:`BorderStyle <no-4125>`             Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-4126>`             Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-4127>`                  The position of the bottom side of the object. This is a
:ref:`Caption <no-4128>`                 The text identifying this particular page.  (str)
:ref:`Children <no-4129>`                Child controls of this panel. This excludes the wx-specific
:ref:`Class <no-4130>`                   The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-4131>`        Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-4132>`    Reference to the sizer item that control's this control's layout.
:ref:`DeferredUpdates <no-4133>`         Allow to defer controls updates until page become active.  (bool)
:ref:`DroppedFileHandler <no-4134>`      Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-4135>`      Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-4136>`        Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-4137>`      Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-4138>`  Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-4139>`      Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-4140>`      Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-4141>`          Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-4142>`          Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-4143>`             Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-4144>`         Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-4145>`         Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-4146>`       Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-4147>`         Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-4148>`    Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-4149>`        Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-4150>`           Dynamically determine the value of the Height property.
:ref:`DynamicHorizontalScroll <no-4151>` Dynamically determine the value of the HorizontalScroll property.
:ref:`DynamicImage <no-4152>`            Dynamically determine the value of the Image property.
:ref:`DynamicLeft <no-4153>`             Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-4154>`     Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-4155>`         Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-4156>`             Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-4157>`       Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-4158>`              Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-4159>`      Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-4160>`              Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-4161>`     Dynamically determine the value of the Transparency property.
:ref:`DynamicVerticalScroll <no-4162>`   Dynamically determine the value of the VerticalScroll property.
:ref:`DynamicVisible <no-4163>`          Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-4164>`            Dynamically determine the value of the Width property.
:ref:`Enabled <no-4165>`                 Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-4166>`                    Specifies font object for this control. (dFont)
:ref:`FontBold <no-4167>`                Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-4168>`         Human-readable description of the current font settings. (str)
:ref:`FontFace <no-4169>`                Specifies the font face. (str)
:ref:`FontInfo <no-4170>`                Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-4171>`              Specifies whether font is italicized. (bool)
:ref:`FontSize <no-4172>`                Specifies the point size of the font. (int)
:ref:`FontUnderline <no-4173>`           Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-4174>`               Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-4175>`                    Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-4176>`                  Specifies the height of the object. (int)
:ref:`HelpContextText <no-4177>`         Specifies the context-sensitive help text associated with this
:ref:`HorizontalScroll <no-4178>`        Controls whether this object will scroll horizontally (default=True)  (bool)
:ref:`Hover <no-4179>`                   When True, Mouse Enter events fire the onHover method, and
:ref:`Image <no-4180>`                   Sets the image that is displayed on the page tab. This is
:ref:`Left <no-4181>`                    Specifies the left position of the object. (int)
:ref:`LogEvents <no-4182>`               Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-4183>`           Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-4184>`             Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-4185>`            Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-4186>`           Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-4187>`             Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-4188>`            Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-4189>`            Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-4190>`                    Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-4191>`                Specifies the base name of the object.
:ref:`Parent <no-4192>`                  The containing object. (obj)
:ref:`Position <no-4193>`                The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-4194>`       Reference to the Preference Management object  (dPref)
:ref:`RegID <no-4195>`                   A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-4196>`                   The position of the right side of the object. This is a
:ref:`Size <no-4197>`                    The size of the object. (tuple)
:ref:`Sizer <no-4198>`                   The sizer for the object.
:ref:`StatusText <no-4199>`              Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-4200>`                 Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-4201>`                     A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-4202>`             Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-4203>`                     The top position of the object. (int)
:ref:`Transparency <no-4204>`            Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-4205>`       Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`UpdateOnPageEnter <no-4206>`       Specifies whether an implicit self.update() happens upon page entry.
:ref:`VerticalScroll <no-4207>`          Controls whether this object will scroll vertically (default=True)  (bool)
:ref:`Visible <no-4208>`                 Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-4209>`         Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-4210>`                   The width of the object. (int)
:ref:`WindowHandle <no-4211>`            The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties - inherited
========================

.. _no-4119:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-4120:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4121:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-4122:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-4123:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4124:

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

.. _no-4125:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4126:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4127:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-4128:

**Caption** 

The text identifying this particular page.  (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4129:

**Children** 

Child controls of this panel. This excludes the wx-specific
    scroll bars  (list of objects)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-4130:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-4131:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4132:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4133:

**DeferredUpdates** 

Allow to defer controls updates until page become active.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPage.dPage`

-------

.. _no-4134:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4135:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4136:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4137:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4138:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4139:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4140:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4141:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4142:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4143:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4144:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4145:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4146:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4147:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4148:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4149:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4150:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4151:

**DynamicHorizontalScroll** 

Dynamically determine the value of the HorizontalScroll property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HorizontalScroll property. If DynamicHorizontalScroll is set to None (the default), HorizontalScroll
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-4152:

**DynamicImage** 

Dynamically determine the value of the Image property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Image property. If DynamicImage is set to None (the default), Image
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPage.dPage`

-------

.. _no-4153:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4154:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4155:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4156:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4157:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4158:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4159:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4160:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4161:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4162:

**DynamicVerticalScroll** 

Dynamically determine the value of the VerticalScroll property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
VerticalScroll property. If DynamicVerticalScroll is set to None (the default), VerticalScroll
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-4163:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4164:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4165:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-4166:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-4167:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4168:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4169:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4170:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4171:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4172:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4173:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4174:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4175:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-4176:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4177:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4178:

**HorizontalScroll** 

Controls whether this object will scroll horizontally (default=True)  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-4179:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4180:

**Image** 

Sets the image that is displayed on the page tab. This is
    determined by the key value passed, which must refer to an
    image already added to the parent pageframe.
    When used to retrieve an image, it returns the index of the
    page's image in the parent pageframe's image list.   (int)


Inherited from: :ref:`dabo.ui.uiwx.dPage.dPage`

-------

.. _no-4181:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4182:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-4183:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4184:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4185:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4186:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4187:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4188:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4189:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4190:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-4191:

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

.. _no-4192:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-4193:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-4194:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-4195:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4196:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-4197:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-4198:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-4199:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4200:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-4201:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4202:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4203:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4204:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4205:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4206:

**UpdateOnPageEnter** 

Specifies whether an implicit self.update() happens upon page entry.


Inherited from: :ref:`dabo.lib.datanav.Page.Page`

-------

.. _no-4207:

**VerticalScroll** 

Controls whether this object will scroll vertically (default=True)  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-4208:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4209:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4210:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4211:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================= ========================
:ref:`BackgroundErased <no-4212>`       Occurs when a window background has been erased and needs repainting.
:ref:`ChildBorn <no-4213>`              Occurs when a child control is created.
:ref:`ControlNavigationEvent <no-4214>` 
:ref:`Create <no-4215>`                 Occurs after the control or form is created.
:ref:`Destroy <no-4216>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-4217>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-4218>`               Occurs when the control gets the focus.
:ref:`Idle <no-4219>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-4220>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-4221>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-4222>`               
:ref:`KeyUp <no-4223>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-4224>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-4225>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-4226>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-4227>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-4228>`             
:ref:`MouseLeave <no-4229>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-4230>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-4231>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-4232>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-4233>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-4234>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-4235>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-4236>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-4237>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-4238>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-4239>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-4240>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-4241>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-4242>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-4243>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-4244>`                   Occurs when the control's position changes.
:ref:`PageContextMenu <no-4245>`        Occurs when the user requests a context event for a dPage
:ref:`PageEnter <no-4246>`              Occurs when the page becomes the active page.
:ref:`PageLeave <no-4247>`              Occurs when a different page becomes active.
:ref:`Paint <no-4248>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-4249>`                 Occurs when the control or form is resized.
:ref:`ScrollBottom <no-4250>`           Occurs when a scrollable window reaches the bottom or right.
:ref:`ScrollEvent <no-4251>`            
:ref:`ScrollLineDown <no-4252>`         Occurs when a scrollable window is scrolled a line down or right.
:ref:`ScrollLineUp <no-4253>`           Occurs when a scrollable window is scrolled a line up or left.
:ref:`ScrollPageDown <no-4254>`         Occurs when a scrollable window is scrolled down or right by a full page.
:ref:`ScrollPageUp <no-4255>`           Occurs when a scrollable window is scrolled up or left by a full page.
:ref:`ScrollThumbDrag <no-4256>`        Occurs when the 'thumb' control of a scrollable window's scrollbars is moved.
:ref:`ScrollThumbRelease <no-4257>`     Occurs when the 'thumb' control of a scrollable window's scrollbars is released.
:ref:`ScrollTop <no-4258>`              Occurs when a scrollable window reaches the top or left.
:ref:`TreeBeginDrag <no-4259>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-4260>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-4261>`                 Occurs when a container wants its controls to update

======================================= ========================


Events
=======

.. _no-4212:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-4213:

**ChildBorn** 

Occurs when a child control is created.



-------

.. _no-4214:

**ControlNavigationEvent** 



-------

.. _no-4215:

**Create** 

Occurs after the control or form is created.



-------

.. _no-4216:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-4217:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-4218:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-4219:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-4220:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-4221:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-4222:

**KeyEvent** 



-------

.. _no-4223:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-4224:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-4225:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-4226:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-4227:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-4228:

**MouseEvent** 



-------

.. _no-4229:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-4230:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-4231:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-4232:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-4233:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-4234:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-4235:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-4236:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-4237:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-4238:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-4239:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-4240:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-4241:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-4242:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-4243:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-4244:

**Move** 

Occurs when the control's position changes.



-------

.. _no-4245:

**PageContextMenu** 

Occurs when the user requests a context event for a dPage



-------

.. _no-4246:

**PageEnter** 

Occurs when the page becomes the active page.



-------

.. _no-4247:

**PageLeave** 

Occurs when a different page becomes active.



-------

.. _no-4248:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-4249:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-4250:

**ScrollBottom** 

Occurs when a scrollable window reaches the bottom or right.



-------

.. _no-4251:

**ScrollEvent** 



-------

.. _no-4252:

**ScrollLineDown** 

Occurs when a scrollable window is scrolled a line down or right.



-------

.. _no-4253:

**ScrollLineUp** 

Occurs when a scrollable window is scrolled a line up or left.



-------

.. _no-4254:

**ScrollPageDown** 

Occurs when a scrollable window is scrolled down or right by a full page.



-------

.. _no-4255:

**ScrollPageUp** 

Occurs when a scrollable window is scrolled up or left by a full page.



-------

.. _no-4256:

**ScrollThumbDrag** 

Occurs when the 'thumb' control of a scrollable window's scrollbars is moved.



-------

.. _no-4257:

**ScrollThumbRelease** 

Occurs when the 'thumb' control of a scrollable window's scrollbars is released.



-------

.. _no-4258:

**ScrollTop** 

Occurs when a scrollable window reaches the top or left.



-------

.. _no-4259:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-4260:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-4261:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


====================================== ========================
:ref:`absoluteCoordinates <no-4262>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-4263>`             Instantiate object as a child of self.
:ref:`afterInit <no-4264>`             
:ref:`afterInitAll <no-4265>`          
:ref:`afterSetProperties <no-4266>`    
:ref:`autoBindEvents <no-4267>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-4268>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-4269>`   
:ref:`bindEvent <no-4270>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-4271>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-4272>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-4273>`          Makes this object topmost
:ref:`clear <no-4274>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-4275>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-4276>`  Given a position relative to this control, return a position relative
:ref:`copy <no-4277>`                  Called by uiApp when the user requests a copy operation.
:ref:`createItems <no-4278>`           
:ref:`cut <no-4279>`                   Called by uiApp when the user requests a cut operation.
:ref:`deleteRecord <no-4280>`          Called by a browse grid when the user wants to delete the current row.
:ref:`drawArc <no-4281>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-4282>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-4283>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-4284>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-4285>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-4286>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-4287>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-4288>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-4289>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-4290>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-4291>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-4292>`              Draws text on the object at the specified position
:ref:`editRecord <no-4293>`            Called by a browse grid when the user wants to edit the current row.
:ref:`endHover <no-4294>`              
:ref:`fitToSizer <no-4295>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-4296>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-4297>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-4298>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-4299>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-4300>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-4301>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-4302>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-4303>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-4304>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-4305>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-4306>`         Returns a dictionary of property name/value pairs.
:ref:`getSearchCtrlClass <no-4307>`    Returns the appropriate editing control class for the given data type.
:ref:`getSelectOptionsPanel <no-4308>` Subclass hook. Return the panel instance to display on the select page.
:ref:`getSelectorOptions <no-4309>`    
:ref:`getSizerProp <no-4310>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-4311>`         Returns a dict containing the object's sizer property info. The
:ref:`handleSort <no-4312>`            
:ref:`handleSortAsc <no-4313>`         
:ref:`handleSortDesc <no-4314>`        
:ref:`handleSortOrder <no-4315>`       
:ref:`handleSortRemove <no-4316>`      
:ref:`hide <no-4317>`                  Make the object invisible.
:ref:`initEvents <no-4318>`            
:ref:`initProperties <no-4319>`        Hook for subclasses. User subclasses should set properties
:ref:`initSizer <no-4320>`             Set up the default vertical box sizer for the page.
:ref:`isContainedBy <no-4321>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-4322>`           Call the given function on this object and all of its Children. If
:ref:`layout <no-4323>`                Wrap the wx version of the call, if possible.
:ref:`lockDisplay <no-4324>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-4325>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-4326>`    Moves this object's tab order before the passed obj.
:ref:`newRecord <no-4327>`             Called by a browse grid when the user wants to add a new row.
:ref:`objectCoordinates <no-4328>`     Given a position relative to the form, return a position relative
:ref:`onCustomSQL <no-4329>`           
:ref:`onHover <no-4330>`               
:ref:`onRequery <no-4331>`             
:ref:`onSortLabelRClick <no-4332>`     
:ref:`pageDown <no-4333>`              
:ref:`pageHorizontally <no-4334>`      Scroll horizontally one 'page' width.
:ref:`pageLeft <no-4335>`              
:ref:`pageRight <no-4336>`             
:ref:`pageUp <no-4337>`                
:ref:`pageVertically <no-4338>`        Scroll vertically one 'page' height.
:ref:`paste <no-4339>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-4340>`           
:ref:`processDroppedFiles <no-4341>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-4342>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-4343>`            Raise the passed Dabo event.
:ref:`reCreate <no-4344>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-4345>`              Recreate the object.
:ref:`redraw <no-4346>`                Called when the object is (re)drawn.
:ref:`refresh <no-4347>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-4348>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-4349>`               Destroys the object.
:ref:`removeDrawnObject <no-4350>`     
:ref:`requery <no-4351>`               
:ref:`scrollHorizontally <no-4352>`    Change the horizontal scroll position by 'amt' units.
:ref:`scrollVertically <no-4353>`      Change the vertical scroll position by 'amt' units.
:ref:`sendToBack <no-4354>`            Places this object behind all others.
:ref:`setAll <no-4355>`                Set all child object properties to the passed value.
:ref:`setFocus <no-4356>`              Sets focus to the object.
:ref:`setFrom <no-4357>`               Subclass hook.
:ref:`setGroupBy <no-4358>`            Subclass hook.
:ref:`setLimit <no-4359>`              
:ref:`setOrderBy <no-4360>`            
:ref:`setPositionInSizer <no-4361>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-4362>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-4363>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-4364>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-4365>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`setWhere <no-4366>`              
:ref:`show <no-4367>`                  Make the object visible.
:ref:`showContainingPage <no-4368>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-4369>`       Display a context menu (popup) at the specified position.
:ref:`super <no-4370>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-4371>`           Remove a previously registered event binding.
:ref:`unbindKey <no-4372>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-4373>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-4374>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-4375>`                

====================================== ========================


Methods
=======

.. _no-4264:

.. function:: dabo.lib.datanav.Page.SelectPage.afterInit(self)



-------

.. _no-4278:

.. function:: dabo.lib.datanav.Page.SelectPage.createItems(self)



-------

.. _no-4307:

.. function:: dabo.lib.datanav.Page.SelectPage.getSearchCtrlClass(self, typ)

   Returns the appropriate editing control class for the given data type.



-------

.. _no-4308:

.. function:: dabo.lib.datanav.Page.SelectPage.getSelectOptionsPanel(self)

   Subclass hook. Return the panel instance to display on the select page.



-------

.. _no-4309:

.. function:: dabo.lib.datanav.Page.SelectPage.getSelectorOptions(self, typ, wordSearch=False)



-------

.. _no-4312:

.. function:: dabo.lib.datanav.Page.SelectPage.handleSort(self, evt, action)



-------

.. _no-4313:

.. function:: dabo.lib.datanav.Page.SelectPage.handleSortAsc(self, evt)



-------

.. _no-4314:

.. function:: dabo.lib.datanav.Page.SelectPage.handleSortDesc(self, evt)



-------

.. _no-4315:

.. function:: dabo.lib.datanav.Page.SelectPage.handleSortOrder(self, evt)



-------

.. _no-4316:

.. function:: dabo.lib.datanav.Page.SelectPage.handleSortRemove(self, evt)



-------

.. _no-4329:

.. function:: dabo.lib.datanav.Page.SelectPage.onCustomSQL(self, evt)



-------

.. _no-4331:

.. function:: dabo.lib.datanav.Page.SelectPage.onRequery(self, evt)



-------

.. _no-4332:

.. function:: dabo.lib.datanav.Page.SelectPage.onSortLabelRClick(self, evt)



-------

.. _no-4351:

.. function:: dabo.lib.datanav.Page.SelectPage.requery(self)



-------

.. _no-4357:

.. function:: dabo.lib.datanav.Page.SelectPage.setFrom(self, biz)

   Subclass hook.



-------

.. _no-4358:

.. function:: dabo.lib.datanav.Page.SelectPage.setGroupBy(self, biz)

   Subclass hook.



-------

.. _no-4359:

.. function:: dabo.lib.datanav.Page.SelectPage.setLimit(self, biz)



-------

.. _no-4360:

.. function:: dabo.lib.datanav.Page.SelectPage.setOrderBy(self, biz)



-------

.. _no-4366:

.. function:: dabo.lib.datanav.Page.SelectPage.setWhere(self, biz)



-------


Methods - inherited
=====================

.. _no-4262:

.. function:: dabo.lib.datanav.Page.SelectPage.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4263:

.. function:: dabo.lib.datanav.Page.SelectPage.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-4265:

.. function:: dabo.lib.datanav.Page.SelectPage.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4266:

.. function:: dabo.lib.datanav.Page.SelectPage.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4267:

.. function:: dabo.lib.datanav.Page.SelectPage.autoBindEvents(self, force=True)
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

.. _no-4268:

.. function:: dabo.lib.datanav.Page.SelectPage.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-4269:

.. function:: dabo.lib.datanav.Page.SelectPage.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4270:

.. function:: dabo.lib.datanav.Page.SelectPage.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-4271:

.. function:: dabo.lib.datanav.Page.SelectPage.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-4272:

.. function:: dabo.lib.datanav.Page.SelectPage.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-4273:

.. function:: dabo.lib.datanav.Page.SelectPage.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4274:

.. function:: dabo.lib.datanav.Page.SelectPage.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4275:

.. function:: dabo.lib.datanav.Page.SelectPage.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4276:

.. function:: dabo.lib.datanav.Page.SelectPage.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4277:

.. function:: dabo.lib.datanav.Page.SelectPage.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4279:

.. function:: dabo.lib.datanav.Page.SelectPage.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4280:

.. function:: dabo.lib.datanav.Page.SelectPage.deleteRecord(self, ds=None)
   :noindex:


   Called by a browse grid when the user wants to delete the current row.


Inherited from: :ref:`dabo.lib.datanav.Page.Page`

-------

.. _no-4281:

.. function:: dabo.lib.datanav.Page.SelectPage.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4282:

.. function:: dabo.lib.datanav.Page.SelectPage.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4283:

.. function:: dabo.lib.datanav.Page.SelectPage.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-4284:

.. function:: dabo.lib.datanav.Page.SelectPage.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4285:

.. function:: dabo.lib.datanav.Page.SelectPage.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4286:

.. function:: dabo.lib.datanav.Page.SelectPage.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4287:

.. function:: dabo.lib.datanav.Page.SelectPage.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4288:

.. function:: dabo.lib.datanav.Page.SelectPage.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4289:

.. function:: dabo.lib.datanav.Page.SelectPage.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4290:

.. function:: dabo.lib.datanav.Page.SelectPage.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4291:

.. function:: dabo.lib.datanav.Page.SelectPage.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4292:

.. function:: dabo.lib.datanav.Page.SelectPage.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4293:

.. function:: dabo.lib.datanav.Page.SelectPage.editRecord(self, ds=None)
   :noindex:


   Called by a browse grid when the user wants to edit the current row.


Inherited from: :ref:`dabo.lib.datanav.Page.Page`

-------

.. _no-4294:

.. function:: dabo.lib.datanav.Page.SelectPage.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4295:

.. function:: dabo.lib.datanav.Page.SelectPage.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4296:

.. function:: dabo.lib.datanav.Page.SelectPage.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-4297:

.. function:: dabo.lib.datanav.Page.SelectPage.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-4298:

.. function:: dabo.lib.datanav.Page.SelectPage.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-4299:

.. function:: dabo.lib.datanav.Page.SelectPage.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4300:

.. function:: dabo.lib.datanav.Page.SelectPage.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-4301:

.. function:: dabo.lib.datanav.Page.SelectPage.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4302:

.. function:: dabo.lib.datanav.Page.SelectPage.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4303:

.. function:: dabo.lib.datanav.Page.SelectPage.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4304:

.. function:: dabo.lib.datanav.Page.SelectPage.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4305:

.. function:: dabo.lib.datanav.Page.SelectPage.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4306:

.. function:: dabo.lib.datanav.Page.SelectPage.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-4310:

.. function:: dabo.lib.datanav.Page.SelectPage.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4311:

.. function:: dabo.lib.datanav.Page.SelectPage.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4317:

.. function:: dabo.lib.datanav.Page.SelectPage.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4318:

.. function:: dabo.lib.datanav.Page.SelectPage.initEvents(self)
   :noindex:



Inherited from: :ref:`dabo.lib.datanav.Page.Page`

-------

.. _no-4319:

.. function:: dabo.lib.datanav.Page.SelectPage.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-4320:

.. function:: dabo.lib.datanav.Page.SelectPage.initSizer(self)
   :noindex:


   Set up the default vertical box sizer for the page.


Inherited from: :ref:`dabo.ui.uiwx.dPage.dPage`

-------

.. _no-4321:

.. function:: dabo.lib.datanav.Page.SelectPage.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4322:

.. function:: dabo.lib.datanav.Page.SelectPage.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-4323:

.. function:: dabo.lib.datanav.Page.SelectPage.layout(self, resetMin=False)
   :noindex:


   Wrap the wx version of the call, if possible.


Inherited from: 'dabo.ui.uiwx.dPanel._BasePanelMixin - can not provide a link

-------

.. _no-4324:

.. function:: dabo.lib.datanav.Page.SelectPage.lockDisplay(self)
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

.. _no-4325:

.. function:: dabo.lib.datanav.Page.SelectPage.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4326:

.. function:: dabo.lib.datanav.Page.SelectPage.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4327:

.. function:: dabo.lib.datanav.Page.SelectPage.newRecord(self, ds=None)
   :noindex:


   Called by a browse grid when the user wants to add a new row.


Inherited from: :ref:`dabo.lib.datanav.Page.Page`

-------

.. _no-4328:

.. function:: dabo.lib.datanav.Page.SelectPage.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4330:

.. function:: dabo.lib.datanav.Page.SelectPage.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4333:

.. function:: dabo.lib.datanav.Page.SelectPage.pageDown(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-4334:

.. function:: dabo.lib.datanav.Page.SelectPage.pageHorizontally(self, direction)
   :noindex:


   Scroll horizontally one 'page' width.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-4335:

.. function:: dabo.lib.datanav.Page.SelectPage.pageLeft(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-4336:

.. function:: dabo.lib.datanav.Page.SelectPage.pageRight(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-4337:

.. function:: dabo.lib.datanav.Page.SelectPage.pageUp(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-4338:

.. function:: dabo.lib.datanav.Page.SelectPage.pageVertically(self, direction)
   :noindex:


   Scroll vertically one 'page' height.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-4339:

.. function:: dabo.lib.datanav.Page.SelectPage.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4340:

.. function:: dabo.lib.datanav.Page.SelectPage.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4341:

.. function:: dabo.lib.datanav.Page.SelectPage.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4342:

.. function:: dabo.lib.datanav.Page.SelectPage.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4343:

.. function:: dabo.lib.datanav.Page.SelectPage.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4344:

.. function:: dabo.lib.datanav.Page.SelectPage.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-4345:

.. function:: dabo.lib.datanav.Page.SelectPage.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4346:

.. function:: dabo.lib.datanav.Page.SelectPage.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4347:

.. function:: dabo.lib.datanav.Page.SelectPage.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4348:

.. function:: dabo.lib.datanav.Page.SelectPage.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4349:

.. function:: dabo.lib.datanav.Page.SelectPage.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4350:

.. function:: dabo.lib.datanav.Page.SelectPage.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4352:

.. function:: dabo.lib.datanav.Page.SelectPage.scrollHorizontally(self, amt)
   :noindex:


   Change the horizontal scroll position by 'amt' units.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-4353:

.. function:: dabo.lib.datanav.Page.SelectPage.scrollVertically(self, amt)
   :noindex:


   Change the vertical scroll position by 'amt' units.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-4354:

.. function:: dabo.lib.datanav.Page.SelectPage.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4355:

.. function:: dabo.lib.datanav.Page.SelectPage.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-4356:

.. function:: dabo.lib.datanav.Page.SelectPage.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4361:

.. function:: dabo.lib.datanav.Page.SelectPage.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4362:

.. function:: dabo.lib.datanav.Page.SelectPage.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-4363:

.. function:: dabo.lib.datanav.Page.SelectPage.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-4364:

.. function:: dabo.lib.datanav.Page.SelectPage.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4365:

.. function:: dabo.lib.datanav.Page.SelectPage.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4367:

.. function:: dabo.lib.datanav.Page.SelectPage.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4368:

.. function:: dabo.lib.datanav.Page.SelectPage.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4369:

.. function:: dabo.lib.datanav.Page.SelectPage.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4370:

.. function:: dabo.lib.datanav.Page.SelectPage.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-4371:

.. function:: dabo.lib.datanav.Page.SelectPage.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-4372:

.. function:: dabo.lib.datanav.Page.SelectPage.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4373:

.. function:: dabo.lib.datanav.Page.SelectPage.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4374:

.. function:: dabo.lib.datanav.Page.SelectPage.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-4375:

.. function:: dabo.lib.datanav.Page.SelectPage.update(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPage.dPage`

-------


|
