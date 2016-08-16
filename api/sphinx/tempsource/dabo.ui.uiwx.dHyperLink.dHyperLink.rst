
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dHyperLink

.. _dabo.ui.uiwx.dHyperLink.dHyperLink:

==============================================
|doc_title|  **dHyperLink.dHyperLink** - class
==============================================


Creates a hyperlink that, when clicked, launches the specified
URL in the user's default browser, or raises a Hit event for your
code to catch and take the appropriate action.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dHyperLink**

.. inheritance-diagram:: dHyperLink


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.alignmentMixin.AlignmentMixin`
* :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`
* wx.lib.agw.hyperlink.HyperLinkCtrl - can not provide a link



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



     - .. image:: _static/winWidgets/dHyperLink.png
          :scale: 75 %
          :target: _static/winWidgets/dHyperLink.png
          :alt: dHyperLink



     - .. image:: _static/nixWidgets/dHyperLink.png
          :scale: 75 %
          :target: _static/nixWidgets/dHyperLink.png
          :alt: dHyperLink


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dHyperLink.dHyperLink

   .. automethod:: dabo.ui.uiwx.dHyperLink.dHyperLink.__init__

|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-34137>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-34138>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-34139>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-34140>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-34141>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-34142>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-34143>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-34144>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-34145>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-34146>`                The caption of the object. (str)
:ref:`Children <no-34147>`               Returns a list of object references to the children of
:ref:`Class <no-34148>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-34149>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-34150>`   Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-34151>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-34152>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-34153>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-34154>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-34155>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-34156>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-34157>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-34158>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-34159>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-34160>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-34161>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-34162>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-34163>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-34164>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-34165>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-34166>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-34167>`          Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-34168>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-34169>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-34170>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-34171>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-34172>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-34173>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-34174>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-34175>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-34176>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-34177>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-34178>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-34179>`                Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-34180>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-34181>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-34182>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-34183>`               Specifies the font face. (str)
:ref:`FontInfo <no-34184>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-34185>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-34186>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-34187>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-34188>`              Normal (unvisited) link text color.  (str or tuple)
:ref:`Form <no-34189>`                   Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-34190>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-34191>`        Specifies the context-sensitive help text associated with this
:ref:`Hover <no-34192>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`HoverColor <no-34193>`             Color of the link when the mouse passes over it.  (str or tuple)
:ref:`HoverUnderline <no-34194>`         Is the link underlined when the mouse passes over it?  (bool)
:ref:`Left <no-34195>`                   Specifies the left position of the object. (int)
:ref:`LinkColor <no-34196>`              Normal (unvisited) link text color.  (str or tuple)
:ref:`LinkUnderline <no-34197>`          Is the link underlined in the normal state?  (bool)
:ref:`LogEvents <no-34198>`              Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-34199>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-34200>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-34201>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-34202>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-34203>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-34204>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-34205>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-34206>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-34207>`               Specifies the base name of the object.
:ref:`Parent <no-34208>`                 The containing object. (obj)
:ref:`Position <no-34209>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-34210>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-34211>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-34212>`                  The position of the right side of the object. This is a
:ref:`ShowHover <no-34213>`              Does the link show the hover effect?  (bool)
:ref:`ShowInBrowser <no-34214>`          Specifies the behavior of clicking on the hyperlink:
:ref:`Size <no-34215>`                   The size of the object. (tuple)
:ref:`Sizer <no-34216>`                  The sizer for the object.
:ref:`StatusText <no-34217>`             Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-34218>`                Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-34219>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-34220>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-34221>`                    The top position of the object. (int)
:ref:`Transparency <no-34222>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-34223>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`URL <no-34224>`                    URL for this link  (str)
:ref:`Visible <no-34225>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-34226>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Visited <no-34227>`                Has this link been visited?  (bool)
:ref:`VisitedColor <no-34228>`           Color of visited links  (str or tuple)
:ref:`VisitedUnderline <no-34229>`       Is the link underlined in the visited state?  (bool)
:ref:`Width <no-34230>`                  The width of the object. (int)
:ref:`WindowHandle <no-34231>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties
==========

.. _no-34193:

**HoverColor** 

Color of the link when the mouse passes over it.  (str or tuple)



-------

.. _no-34194:

**HoverUnderline** 

Is the link underlined when the mouse passes over it?  (bool)



-------

.. _no-34196:

**LinkColor** 

Normal (unvisited) link text color.  (str or tuple)



-------

.. _no-34197:

**LinkUnderline** 

Is the link underlined in the normal state?  (bool)



-------

.. _no-34213:

**ShowHover** 

Does the link show the hover effect?  (bool)



-------

.. _no-34214:

**ShowInBrowser** 

Specifies the behavior of clicking on the hyperlink:
            True: open URL in user's default web browser (default)
            False: raise Hit event for your code to handle



-------

.. _no-34224:

**URL** 

URL for this link  (str)



-------

.. _no-34227:

**Visited** 

Has this link been visited?  (bool)



-------

.. _no-34228:

**VisitedColor** 

Color of visited links  (str or tuple)



-------

.. _no-34229:

**VisitedUnderline** 

Is the link underlined in the visited state?  (bool)



-------


Properties - inherited
========================

.. _no-34137:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34138:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34139:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34140:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34141:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34142:

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

.. _no-34143:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34144:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34145:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34146:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34147:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-34148:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34149:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34150:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34151:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34152:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34153:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34154:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34155:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34156:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34157:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34158:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34159:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34160:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34161:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34162:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34163:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34164:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34165:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34166:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34167:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34168:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34169:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34170:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34171:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34172:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34173:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34174:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34175:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34176:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34177:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34178:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34179:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-34180:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-34181:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34182:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34183:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34184:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34185:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34186:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34187:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34188:

**ForeColor** 

Normal (unvisited) link text color.  (str or tuple)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34189:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34190:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34191:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34192:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34195:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34198:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34199:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34200:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34201:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34202:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34203:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34204:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34205:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34206:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-34207:

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

.. _no-34208:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-34209:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-34210:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34211:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34212:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34215:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-34216:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-34217:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34218:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-34219:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34220:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34221:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34222:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34223:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34225:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34226:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34230:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34231:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-34232>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-34233>`                 Occurs after the control or form is created.
:ref:`Destroy <no-34234>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-34235>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-34236>`               Occurs when the control gets the focus.
:ref:`Idle <no-34237>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-34238>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-34239>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-34240>`               
:ref:`KeyUp <no-34241>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-34242>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-34243>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-34244>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-34245>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-34246>`             
:ref:`MouseLeave <no-34247>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-34248>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-34249>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-34250>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-34251>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-34252>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-34253>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-34254>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-34255>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-34256>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-34257>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-34258>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-34259>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-34260>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-34261>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-34262>`                   Occurs when the control's position changes.
:ref:`Paint <no-34263>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-34264>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-34265>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-34266>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-34267>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-34232:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-34233:

**Create** 

Occurs after the control or form is created.



-------

.. _no-34234:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-34235:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-34236:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-34237:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-34238:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-34239:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-34240:

**KeyEvent** 



-------

.. _no-34241:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-34242:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-34243:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-34244:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-34245:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-34246:

**MouseEvent** 



-------

.. _no-34247:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-34248:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-34249:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-34250:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-34251:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-34252:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-34253:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-34254:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-34255:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-34256:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-34257:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-34258:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-34259:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-34260:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-34261:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-34262:

**Move** 

Occurs when the control's position changes.



-------

.. _no-34263:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-34264:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-34265:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-34266:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-34267:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


=============================================== ========================
:ref:`absoluteCoordinates <no-34268>`           Translates a position value for a control to absolute screen position.
:ref:`addObject <no-34269>`                     Instantiate object as a child of self.
:ref:`afterInit <no-34270>`                     Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-34271>`                  
:ref:`afterSetProperties <no-34272>`            
:ref:`autoBindEvents <no-34273>`                Automatically bind any on*() methods to the associated event.
:ref:`base_AcceptsFocus <no-34274>`             Please use PyControl.AcceptsFocus instead.
:ref:`base_AcceptsFocusFromKeyboard <no-34275>` Please use PyControl.AcceptsFocusFromKeyboard instead.
:ref:`base_AddChild <no-34276>`                 Please use PyControl.AddChild instead.
:ref:`base_DoGetBestSize <no-34277>`            Please use PyControl.DoGetBestSize instead.
:ref:`base_DoGetClientSize <no-34278>`          Please use PyControl.DoGetClientSize instead.
:ref:`base_DoGetPosition <no-34279>`            Please use PyControl.DoGetPosition instead.
:ref:`base_DoGetSize <no-34280>`                Please use PyControl.DoGetSize instead.
:ref:`base_DoGetVirtualSize <no-34281>`         Please use PyControl.DoGetVirtualSize instead.
:ref:`base_DoMoveWindow <no-34282>`             Please use PyControl.DoMoveWindow instead.
:ref:`base_DoSetClientSize <no-34283>`          Please use PyControl.DoSetClientSize instead.
:ref:`base_DoSetSize <no-34284>`                Please use PyControl.DoSetSize instead.
:ref:`base_DoSetVirtualSize <no-34285>`         Please use PyControl.DoSetVirtualSize instead.
:ref:`base_Enable <no-34286>`                   Please use PyControl.Enable instead.
:ref:`base_GetDefaultAttributes <no-34287>`     Please use PyControl.GetDefaultAttributes instead.
:ref:`base_GetMaxSize <no-34288>`               Please use PyControl.GetMaxSize instead.
:ref:`base_InitDialog <no-34289>`               Please use PyControl.InitDialog instead.
:ref:`base_OnInternalIdle <no-34290>`           Please use PyControl.OnInternalIdle instead.
:ref:`base_RemoveChild <no-34291>`              Please use PyControl.RemoveChild instead.
:ref:`base_ShouldInheritColours <no-34292>`     Please use PyControl.ShouldInheritColours instead.
:ref:`base_TransferDataFromWindow <no-34293>`   Please use PyControl.TransferDataFromWindow instead.
:ref:`base_TransferDataToWindow <no-34294>`     Please use PyControl.TransferDataToWindow instead.
:ref:`base_Validate <no-34295>`                 Please use PyControl.Validate instead.
:ref:`beforeInit <no-34296>`                    Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-34297>`           
:ref:`bindEvent <no-34298>`                     Bind a dEvent to a callback function.
:ref:`bindEvents <no-34299>`                    Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-34300>`                       Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-34301>`                  Makes this object topmost
:ref:`clear <no-34302>`                         Clears the background of custom-drawn objects.
:ref:`clone <no-34303>`                         Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-34304>`          Given a position relative to this control, return a position relative
:ref:`copy <no-34305>`                          Called by uiApp when the user requests a copy operation.
:ref:`cut <no-34306>`                           Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-34307>`                       Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-34308>`                    Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-34309>`                    Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-34310>`                   Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-34311>`               Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-34312>`                  Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-34313>`                      Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-34314>`                 Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-34315>`                   Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-34316>`                 Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-34317>`          Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-34318>`                      Draws text on the object at the specified position
:ref:`endHover <no-34319>`                      
:ref:`fitToSizer <no-34320>`                    Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-34321>`                    Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-34322>`                Reset the font zoom back to zero.
:ref:`fontZoomOut <no-34323>`                   Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-34324>`               Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-34325>`               Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-34326>`              Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-34327>`             Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-34328>`              Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-34329>`              Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-34330>`            Convenience method to let you call this directly on the object.
:ref:`getProperties <no-34331>`                 Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-34332>`                  Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-34333>`                 Returns a dict containing the object's sizer property info. The
:ref:`hide <no-34334>`                          Make the object invisible.
:ref:`initEvents <no-34335>`                    Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-34336>`                Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-34337>`                 Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-34338>`                   Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-34339>`                   Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-34340>`             Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-34341>`            Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-34342>`             Given a position relative to the form, return a position relative
:ref:`onHover <no-34343>`                       
:ref:`onResize <no-34344>`                      
:ref:`paste <no-34345>`                         Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-34346>`                   
:ref:`processDroppedFiles <no-34347>`           Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-34348>`            Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-34349>`                    Raise the passed Dabo event.
:ref:`reCreate <no-34350>`                      Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-34351>`                      Recreate the object.
:ref:`redraw <no-34352>`                        Called when the object is (re)drawn.
:ref:`refresh <no-34353>`                       
:ref:`relativeCoordinates <no-34354>`           Translates an absolute screen position to position value for a control.
:ref:`release <no-34355>`                       Destroys the object.
:ref:`removeDrawnObject <no-34356>`             
:ref:`sendToBack <no-34357>`                    Places this object behind all others.
:ref:`setAll <no-34358>`                        Set all child object properties to the passed value.
:ref:`setFocus <no-34359>`                      Sets focus to the object.
:ref:`setPositionInSizer <no-34360>`            Convenience method to let you call this directly on the object.
:ref:`setProperties <no-34361>`                 Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-34362>`         Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-34363>`                  Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-34364>`                 Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-34365>`                          Make the object visible.
:ref:`showContainingPage <no-34366>`            If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-34367>`               Display a context menu (popup) at the specified position.
:ref:`super <no-34368>`                         This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-34369>`                   Remove a previously registered event binding.
:ref:`unbindKey <no-34370>`                     Unbind a previously bound key combination.
:ref:`unlockDisplay <no-34371>`                 Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-34372>`              Immediately unlocks the display, no matter how many previous
:ref:`update <no-34373>`                        Update the properties of this object and all contained objects.

=============================================== ========================


Methods
=======

.. _no-34344:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.onResize(self, evt)



-------

.. _no-34353:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.refresh(self)



-------


Methods - inherited
=====================

.. _no-34268:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34269:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-34270:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34271:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34272:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34273:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.autoBindEvents(self, force=True)
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

.. _no-34274:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.base_AcceptsFocus(*args, \**kwargs)
   :noindex:


   Please use PyControl.AcceptsFocus instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-34275:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.base_AcceptsFocusFromKeyboard(*args, \**kwargs)
   :noindex:


   Please use PyControl.AcceptsFocusFromKeyboard instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-34276:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.base_AddChild(*args, \**kwargs)
   :noindex:


   Please use PyControl.AddChild instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-34277:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.base_DoGetBestSize(*args, \**kwargs)
   :noindex:


   Please use PyControl.DoGetBestSize instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-34278:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.base_DoGetClientSize(*args, \**kwargs)
   :noindex:


   Please use PyControl.DoGetClientSize instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-34279:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.base_DoGetPosition(*args, \**kwargs)
   :noindex:


   Please use PyControl.DoGetPosition instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-34280:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.base_DoGetSize(*args, \**kwargs)
   :noindex:


   Please use PyControl.DoGetSize instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-34281:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.base_DoGetVirtualSize(*args, \**kwargs)
   :noindex:


   Please use PyControl.DoGetVirtualSize instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-34282:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.base_DoMoveWindow(*args, \**kwargs)
   :noindex:


   Please use PyControl.DoMoveWindow instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-34283:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.base_DoSetClientSize(*args, \**kwargs)
   :noindex:


   Please use PyControl.DoSetClientSize instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-34284:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.base_DoSetSize(*args, \**kwargs)
   :noindex:


   Please use PyControl.DoSetSize instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-34285:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.base_DoSetVirtualSize(*args, \**kwargs)
   :noindex:


   Please use PyControl.DoSetVirtualSize instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-34286:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.base_Enable(*args, \**kwargs)
   :noindex:


   Please use PyControl.Enable instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-34287:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.base_GetDefaultAttributes(*args, \**kwargs)
   :noindex:


   Please use PyControl.GetDefaultAttributes instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-34288:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.base_GetMaxSize(*args, \**kwargs)
   :noindex:


   Please use PyControl.GetMaxSize instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-34289:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.base_InitDialog(*args, \**kwargs)
   :noindex:


   Please use PyControl.InitDialog instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-34290:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.base_OnInternalIdle(*args, \**kwargs)
   :noindex:


   Please use PyControl.OnInternalIdle instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-34291:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.base_RemoveChild(*args, \**kwargs)
   :noindex:


   Please use PyControl.RemoveChild instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-34292:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.base_ShouldInheritColours(*args, \**kwargs)
   :noindex:


   Please use PyControl.ShouldInheritColours instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-34293:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.base_TransferDataFromWindow(*args, \**kwargs)
   :noindex:


   Please use PyControl.TransferDataFromWindow instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-34294:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.base_TransferDataToWindow(*args, \**kwargs)
   :noindex:


   Please use PyControl.TransferDataToWindow instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-34295:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.base_Validate(*args, \**kwargs)
   :noindex:


   Please use PyControl.Validate instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-34296:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34297:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34298:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-34299:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-34300:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-34301:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34302:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34303:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34304:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34305:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34306:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34307:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34308:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34309:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-34310:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34311:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34312:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34313:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34314:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34315:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34316:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34317:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34318:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34319:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34320:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34321:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34322:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34323:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34324:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34325:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34326:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34327:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34328:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34329:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34330:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34331:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-34332:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34333:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34334:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34335:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34336:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34337:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34338:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34339:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.lockDisplay(self)
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

.. _no-34340:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34341:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34342:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34343:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34345:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34346:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34347:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34348:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34349:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34350:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-34351:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34352:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34354:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34355:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34356:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34357:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34358:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-34359:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34360:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34361:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-34362:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-34363:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34364:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34365:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34366:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34367:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34368:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-34369:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-34370:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34371:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34372:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-34373:

.. function:: dabo.ui.uiwx.dHyperLink.dHyperLink.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
