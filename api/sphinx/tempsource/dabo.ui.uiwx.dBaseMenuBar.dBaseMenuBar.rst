
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dBaseMenuBar

.. _dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar:

==================================================
|doc_title|  **dBaseMenuBar.dBaseMenuBar** - class
==================================================


Creates a basic menu bar with File, Edit, and Help menus.

The Edit menu has standard Copy, Cut, and Paste menu items, and the Help menu
has an About menu item. On Mac, the About menu item and Help menu are moved
to the appropriate place in the application menu.

Typical usage would be to instantiate dBaseMenuBar, set it to your form's
menubar (using form.MenuBar = dabo.ui.dBaseMenuBar) and then use the
append() methods of dMenuBar and dMenu to add the specific dMenu(s) and
dMenuItem(s) that your application needs.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dBaseMenuBar**

.. inheritance-diagram:: dBaseMenuBar


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dMenuBar.dMenuBar`



|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - .. image:: _static/macWidgets/dBaseMenuBar.png
          :scale: 75 %
          :target: _static/macWidgets/dBaseMenuBar.png
          :alt: dBaseMenuBar



     - .. image:: _static/winWidgets/dBaseMenuBar.png
          :scale: 75 %
          :target: _static/winWidgets/dBaseMenuBar.png
          :alt: dBaseMenuBar



     - .. image:: _static/nixWidgets/dBaseMenuBar.png
          :scale: 75 %
          :target: _static/nixWidgets/dBaseMenuBar.png
          :alt: dBaseMenuBar


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar


|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-30122>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-30123>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-30124>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-30125>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-30126>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-30127>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-30128>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-30129>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-30130>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-30131>`                The caption of the object. (str)
:ref:`Children <no-30132>`               Returns a list of object references to the children of
:ref:`Class <no-30133>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-30134>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-30135>`   Reference to the sizer item that control's this control's layout.
:ref:`Count <no-30136>`                  Returns the number of child menus. Read-only.  (int)
:ref:`DroppedFileHandler <no-30137>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-30138>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-30139>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-30140>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-30141>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-30142>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-30143>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-30144>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-30145>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-30146>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-30147>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-30148>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-30149>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-30150>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-30151>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-30152>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-30153>`          Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-30154>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-30155>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-30156>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-30157>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-30158>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-30159>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-30160>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-30161>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-30162>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-30163>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-30164>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-30165>`                Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-30166>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-30167>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-30168>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-30169>`               Specifies the font face. (str)
:ref:`FontInfo <no-30170>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-30171>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-30172>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-30173>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-30174>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-30175>`                   Specifies the form that we are a member of.  (dabo.ui.dForm)
:ref:`Height <no-30176>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-30177>`        Specifies the context-sensitive help text associated with this
:ref:`Hover <no-30178>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-30179>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-30180>`              Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-30181>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-30182>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-30183>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-30184>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-30185>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-30186>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-30187>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-30188>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-30189>`               Specifies the base name of the object.
:ref:`Parent <no-30190>`                 The containing object. (obj)
:ref:`Position <no-30191>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-30192>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-30193>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-30194>`                  The position of the right side of the object. This is a
:ref:`Size <no-30195>`                   The size of the object. (tuple)
:ref:`Sizer <no-30196>`                  The sizer for the object.
:ref:`StatusText <no-30197>`             Specifies the text that displays in the form's status bar, if any.
:ref:`Tag <no-30198>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-30199>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-30200>`                    The top position of the object. (int)
:ref:`Transparency <no-30201>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-30202>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-30203>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-30204>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-30205>`                  The width of the object. (int)
:ref:`WindowHandle <no-30206>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties - inherited
========================

.. _no-30122:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30123:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30124:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30125:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30126:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30127:

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

.. _no-30128:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30129:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30130:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30131:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30132:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-30133:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30134:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30135:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30136:

**Count** 

Returns the number of child menus. Read-only.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dMenuBar.dMenuBar`

-------

.. _no-30137:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30138:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30139:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30140:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30141:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30142:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30143:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30144:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30145:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30146:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30147:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30148:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30149:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30150:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30151:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30152:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30153:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30154:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30155:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30156:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30157:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30158:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30159:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30160:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30161:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30162:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30163:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30164:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30165:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-30166:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-30167:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30168:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30169:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30170:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30171:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30172:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30173:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30174:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30175:

**Form** 

Specifies the form that we are a member of.  (dabo.ui.dForm)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30176:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30177:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30178:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30179:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30180:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30181:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30182:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30183:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30184:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30185:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30186:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30187:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30188:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-30189:

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

.. _no-30190:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-30191:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-30192:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30193:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30194:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30195:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-30196:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-30197:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30198:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30199:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30200:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30201:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30202:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30203:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30204:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30205:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30206:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-30207>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-30208>`                 Occurs after the control or form is created.
:ref:`Destroy <no-30209>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-30210>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-30211>`               Occurs when the control gets the focus.
:ref:`Idle <no-30212>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-30213>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-30214>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-30215>`               
:ref:`KeyUp <no-30216>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-30217>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-30218>`              Occurs when a menu has just been closed.
:ref:`MenuEvent <no-30219>`              
:ref:`MenuHighlight <no-30220>`          Occurs when a menu item is highlighted.
:ref:`MenuOpen <no-30221>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-30222>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-30223>`             
:ref:`MouseLeave <no-30224>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-30225>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-30226>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-30227>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-30228>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-30229>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-30230>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-30231>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-30232>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-30233>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-30234>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-30235>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-30236>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-30237>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-30238>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-30239>`                   Occurs when the control's position changes.
:ref:`Paint <no-30240>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-30241>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-30242>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-30243>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-30244>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-30207:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-30208:

**Create** 

Occurs after the control or form is created.



-------

.. _no-30209:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-30210:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-30211:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-30212:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-30213:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-30214:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-30215:

**KeyEvent** 



-------

.. _no-30216:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-30217:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-30218:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-30219:

**MenuEvent** 



-------

.. _no-30220:

**MenuHighlight** 

Occurs when a menu item is highlighted.



-------

.. _no-30221:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-30222:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-30223:

**MouseEvent** 



-------

.. _no-30224:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-30225:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-30226:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-30227:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-30228:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-30229:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-30230:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-30231:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-30232:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-30233:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-30234:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-30235:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-30236:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-30237:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-30238:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-30239:

**Move** 

Occurs when the control's position changes.



-------

.. _no-30240:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-30241:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-30242:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-30243:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-30244:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-30245>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-30246>`             Instantiate object as a child of self.
:ref:`afterInit <no-30247>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-30248>`          
:ref:`afterSetProperties <no-30249>`    
:ref:`append <no-30250>`                Appends a dMenu to the end of the dMenuBar, and returns a reference
:ref:`appendMenu <no-30251>`            Inserts a dMenu at the end of the dMenuBar, and returns the
:ref:`autoBindEvents <no-30252>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-30253>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-30254>`   
:ref:`bindEvent <no-30255>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-30256>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-30257>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-30258>`          Makes this object topmost
:ref:`clear <no-30259>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-30260>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-30261>`  Given a position relative to this control, return a position relative
:ref:`copy <no-30262>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-30263>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-30264>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-30265>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-30266>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-30267>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-30268>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-30269>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-30270>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-30271>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-30272>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-30273>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-30274>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-30275>`              Draws text on the object at the specified position
:ref:`endHover <no-30276>`              
:ref:`fitToSizer <no-30277>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-30278>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-30279>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-30280>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-30281>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-30282>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-30283>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-30284>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-30285>`      Returns an object that locks the current display when created, and
:ref:`getMenu <no-30286>`               Returns a reference to the menu with the specified MenuID or Caption.
:ref:`getMenuIndex <no-30287>`          Returns the index of the menu with the specified ID or caption.
:ref:`getMousePosition <no-30288>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-30289>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-30290>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-30291>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-30292>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-30293>`                  Make the object invisible.
:ref:`initEvents <no-30294>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-30295>`        Hook for subclasses. User subclasses should set properties
:ref:`insert <no-30296>`                Inserts a dMenu at the specified position in the dMenuBar, and returns
:ref:`insertMenu <no-30297>`            Inserts a dMenu in the dMenuBar at the specified position, and
:ref:`isContainedBy <no-30298>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-30299>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-30300>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-30301>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-30302>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-30303>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-30304>`               
:ref:`paste <no-30305>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-30306>`           
:ref:`prepend <no-30307>`               Prepends a dMenu to the beginning of the dMenuBar, and returns
:ref:`prependMenu <no-30308>`           Inserts a dMenu at the beginning of the dMenuBar, and returns
:ref:`processDroppedFiles <no-30309>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-30310>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-30311>`            Raise the passed Dabo event.
:ref:`reCreate <no-30312>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-30313>`              Recreate the object.
:ref:`redraw <no-30314>`                Called when the object is (re)drawn.
:ref:`refresh <no-30315>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-30316>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-30317>`               Destroys the object.
:ref:`remove <no-30318>`                Removes the menu at the specified index from the menu bar. You may
:ref:`removeDrawnObject <no-30319>`     
:ref:`sendToBack <no-30320>`            Places this object behind all others.
:ref:`setAll <no-30321>`                Set all child object properties to the passed value.
:ref:`setFocus <no-30322>`              Sets focus to the object.
:ref:`setPositionInSizer <no-30323>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-30324>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-30325>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-30326>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-30327>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-30328>`                  Make the object visible.
:ref:`showContainingPage <no-30329>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-30330>`       Display a context menu (popup) at the specified position.
:ref:`super <no-30331>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-30332>`           Remove a previously registered event binding.
:ref:`unbindKey <no-30333>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-30334>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-30335>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-30336>`                

======================================= ========================


Methods - inherited
=====================

.. _no-30245:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30246:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-30247:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30248:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30249:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30250:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.append(self, caption, MenuID=None)
   :noindex:


   
   Appends a dMenu to the end of the dMenuBar, and returns a reference
   to that menu.
   
   A generic dMenu will be created with the passed caption. Also see the
   appendMenu() function, which takes a dMenu instance as an argument.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenuBar.dMenuBar`

-------

.. _no-30251:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.appendMenu(self, menu)
   :noindex:


   
   Inserts a dMenu at the end of the dMenuBar, and returns the
   reference to that menu.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenuBar.dMenuBar`

-------

.. _no-30252:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.autoBindEvents(self, force=True)
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

.. _no-30253:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30254:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30255:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-30256:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-30257:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-30258:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30259:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30260:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30261:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30262:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30263:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30264:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30265:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30266:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-30267:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30268:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30269:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30270:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30271:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30272:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30273:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30274:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30275:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30276:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30277:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30278:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30279:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30280:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30281:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30282:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30283:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30284:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30285:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30286:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.getMenu(self, idOrCaption)
   :noindex:


   
   Returns a reference to the menu with the specified MenuID or Caption.
   The MenuID property is checked first; then the Caption. If no match is found,
   None is returned.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenuBar.dMenuBar`

-------

.. _no-30287:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.getMenuIndex(self, idOrCaption)
   :noindex:


   
   Returns the index of the menu with the specified ID or caption.
   If the menu isn't found, None is returned.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenuBar.dMenuBar`

-------

.. _no-30288:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30289:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30290:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-30291:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30292:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30293:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30294:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30295:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30296:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.insert(self, pos, caption, MenuID=None)
   :noindex:


   
   Inserts a dMenu at the specified position in the dMenuBar, and returns
   a reference to that menu.
   
   A generic dMenu will be created with the passed caption. Also see the
   insertMenu() function, which takes a dMenu instance as an argument.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenuBar.dMenuBar`

-------

.. _no-30297:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.insertMenu(self, pos, menu)
   :noindex:


   
   Inserts a dMenu in the dMenuBar at the specified position, and
   returns a reference to that menu.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenuBar.dMenuBar`

-------

.. _no-30298:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30299:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30300:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.lockDisplay(self)
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

.. _no-30301:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30302:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30303:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30304:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30305:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30306:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30307:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.prepend(self, caption, MenuID=None)
   :noindex:


   
   Prepends a dMenu to the beginning of the dMenuBar, and returns
   a reference to that menu.
   
   A generic dMenu will be created with the passed caption. Also see the
   prependMenu() function, which takes a dMenu instance as an argument.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenuBar.dMenuBar`

-------

.. _no-30308:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.prependMenu(self, menu)
   :noindex:


   
   Inserts a dMenu at the beginning of the dMenuBar, and returns
   a reference to that menu.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenuBar.dMenuBar`

-------

.. _no-30309:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30310:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30311:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30312:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-30313:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30314:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30315:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30316:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30317:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30318:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.remove(self, indexOrMenu, release=True)
   :noindex:


   
   Removes the menu at the specified index from the menu bar. You may
   also pass a reference to the menu, or the menu's Caption, and it will
   find the associated index.
   
   If release is True (the default), the menu is deleted as well. If release
   is False, a reference to the menu object will be returned, and the caller
   is responsible for deleting it.
   


Inherited from: :ref:`dabo.ui.uiwx.dMenuBar.dMenuBar`

-------

.. _no-30319:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30320:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30321:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-30322:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30323:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30324:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-30325:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-30326:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30327:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30328:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30329:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30330:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30331:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-30332:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-30333:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30334:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30335:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-30336:

.. function:: dabo.ui.uiwx.dBaseMenuBar.dBaseMenuBar.update(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dMenuBar.dMenuBar`

-------


|
