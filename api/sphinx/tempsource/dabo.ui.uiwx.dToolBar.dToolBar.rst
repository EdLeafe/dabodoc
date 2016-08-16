
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dToolBar

.. _dabo.ui.uiwx.dToolBar.dToolBar:

==========================================
|doc_title|  **dToolBar.dToolBar** - class
==========================================


Creates a toolbar, which is a menu-like collection of icons.

You may also add items to a toolbar such as separators and real Dabo
controls, such as dropdown lists, radio boxes, and text boxes.

Under Gtk only, the toolbar can be detached into a floating toolbar,
and reattached by the user at will. wxPython doesn't support this behavior
for Windows or Mac yet, though.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dToolBar**

.. inheritance-diagram:: dToolBar


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`



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



   * - .. image:: _static/macWidgets/dToolBar.png
          :scale: 75 %
          :target: _static/macWidgets/dToolBar.png
          :alt: dToolBar



     - .. image:: _static/winWidgets/dToolBar.png
          :scale: 75 %
          :target: _static/winWidgets/dToolBar.png
          :alt: dToolBar



     - .. image:: _static/nixWidgets/dToolBar.png
          :scale: 75 %
          :target: _static/nixWidgets/dToolBar.png
          :alt: dToolBar


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dToolBar.dToolBar

   .. automethod:: dabo.ui.uiwx.dToolBar.dToolBar.__init__

|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-11009>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-11010>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-11011>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-11012>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-11013>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-11014>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-11015>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-11016>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-11017>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-11018>`                The caption of the object. (str)
:ref:`Children <no-11019>`               Returns a list of object references to the children of
:ref:`Class <no-11020>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-11021>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-11022>`   Reference to the sizer item that control's this control's layout.
:ref:`Dockable <no-11023>`               Specifies whether the toolbar can be docked and undocked.  (bool)
:ref:`DroppedFileHandler <no-11024>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-11025>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-11026>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-11027>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-11028>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-11029>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-11030>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-11031>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-11032>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-11033>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-11034>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-11035>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-11036>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-11037>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-11038>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-11039>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-11040>`          Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-11041>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-11042>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-11043>`        Dynamically determine the value of the Position property.
:ref:`DynamicShowCaptions <no-11044>`    Dynamically determine the value of the ShowCaptions property.
:ref:`DynamicShowIcons <no-11045>`       Dynamically determine the value of the ShowIcons property.
:ref:`DynamicSize <no-11046>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-11047>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-11048>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-11049>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-11050>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-11051>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-11052>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-11053>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-11054>`                Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-11055>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-11056>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-11057>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-11058>`               Specifies the font face. (str)
:ref:`FontInfo <no-11059>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-11060>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-11061>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-11062>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-11063>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-11064>`                   Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-11065>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-11066>`        Specifies the context-sensitive help text associated with this
:ref:`Hover <no-11067>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-11068>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-11069>`              Specifies which events to log.  (list of strings)
:ref:`MaxHeight <no-11070>`              Specifies the maximum height of added buttons.  (int)
:ref:`MaxWidth <no-11071>`               Specifies the maximum width of added buttons.  (int)
:ref:`MaximumHeight <no-11072>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-11073>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-11074>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-11075>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-11076>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-11077>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-11078>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-11079>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-11080>`               Specifies the base name of the object.
:ref:`Parent <no-11081>`                 The containing object. (obj)
:ref:`Position <no-11082>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-11083>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-11084>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-11085>`                  The position of the right side of the object. This is a
:ref:`ShowCaptions <no-11086>`           Specifies whether the text captions are shown in the toolbar.  (bool)
:ref:`ShowIcons <no-11087>`              Specifies whether the icons are shown in the toolbar.  (bool)
:ref:`Size <no-11088>`                   The size of the object. (tuple)
:ref:`Sizer <no-11089>`                  The sizer for the object.
:ref:`StatusText <no-11090>`             Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-11091>`                Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-11092>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-11093>`            Specifies the tooltip text associated with this window. (str)
:ref:`ToolbarItemClass <no-11094>`       Class to instantiate for toolbar items. Default=dToolBarItem.  (varies)
:ref:`Top <no-11095>`                    The top position of the object. (int)
:ref:`Transparency <no-11096>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-11097>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-11098>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-11099>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-11100>`                  The width of the object. (int)
:ref:`WindowHandle <no-11101>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties
==========

.. _no-11023:

**Dockable** 


Specifies whether the toolbar can be docked and undocked.  (bool)

.. note::

    Currently, this only seems to work on Linux, and can't be changed after
    instantiation. Default is True.





-------

.. _no-11044:

**DynamicShowCaptions** 

Dynamically determine the value of the ShowCaptions property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowCaptions property. If DynamicShowCaptions is set to None (the default), ShowCaptions
will not be dynamically evaluated.



-------

.. _no-11045:

**DynamicShowIcons** 

Dynamically determine the value of the ShowIcons property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowIcons property. If DynamicShowIcons is set to None (the default), ShowIcons
will not be dynamically evaluated.



-------

.. _no-11086:

**ShowCaptions** 

Specifies whether the text captions are shown in the toolbar.  (bool)

Default is False.



-------

.. _no-11087:

**ShowIcons** 

Specifies whether the icons are shown in the toolbar.  (bool)

Note that you can set both ShowCaptions and ShowIcons to False, but in
that case, the icons will still show. Default is True.



-------

.. _no-11094:

**ToolbarItemClass** 

Class to instantiate for toolbar items. Default=dToolBarItem.  (varies)



-------


Properties - inherited
========================

.. _no-11009:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11010:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11011:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11012:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11013:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11014:

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

.. _no-11015:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11016:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11017:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-11018:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11019:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-11020:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11021:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11022:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11024:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11025:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11026:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11027:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11028:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11029:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11030:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11031:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11032:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11033:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11034:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11035:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11036:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11037:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11038:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11039:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11040:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11041:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11042:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11043:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11046:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11047:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11048:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11049:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11050:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11051:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11052:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11053:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11054:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-11055:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-11056:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11057:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11058:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11059:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11060:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11061:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11062:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11063:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11064:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-11065:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11066:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11067:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11068:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11069:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11070:

**MaxHeight** 

Specifies the maximum height of added buttons.  (int)

When set to zero, there will be no height limit.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-11071:

**MaxWidth** 

Specifies the maximum width of added buttons.  (int)

When set to zero, there will be no width limit.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-11072:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11073:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11074:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11075:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11076:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11077:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11078:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11079:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-11080:

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

.. _no-11081:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-11082:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-11083:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11084:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11085:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-11088:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-11089:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-11090:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11091:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-11092:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11093:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11095:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11096:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11097:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11098:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11099:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11100:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11101:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-11102>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-11103>`                 Occurs after the control or form is created.
:ref:`Destroy <no-11104>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-11105>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-11106>`               Occurs when the control gets the focus.
:ref:`Idle <no-11107>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-11108>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-11109>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-11110>`               
:ref:`KeyUp <no-11111>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-11112>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-11113>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-11114>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-11115>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-11116>`             
:ref:`MouseLeave <no-11117>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-11118>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-11119>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-11120>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-11121>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-11122>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-11123>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-11124>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-11125>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-11126>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-11127>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-11128>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-11129>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-11130>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-11131>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-11132>`                   Occurs when the control's position changes.
:ref:`Paint <no-11133>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-11134>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-11135>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-11136>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-11137>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-11102:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-11103:

**Create** 

Occurs after the control or form is created.



-------

.. _no-11104:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-11105:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-11106:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-11107:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-11108:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-11109:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-11110:

**KeyEvent** 



-------

.. _no-11111:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-11112:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-11113:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-11114:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-11115:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-11116:

**MouseEvent** 



-------

.. _no-11117:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-11118:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-11119:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-11120:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-11121:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-11122:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-11123:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-11124:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-11125:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-11126:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-11127:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-11128:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-11129:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-11130:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-11131:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-11132:

**Move** 

Occurs when the control's position changes.



-------

.. _no-11133:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-11134:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-11135:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-11136:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-11137:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-11138>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-11139>`             Instantiate object as a child of self.
:ref:`afterInit <no-11140>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-11141>`          
:ref:`afterSetProperties <no-11142>`    
:ref:`appendButton <no-11143>`          Adds a tool (button) to the toolbar.
:ref:`appendControl <no-11144>`         Adds any Dabo Control to the toolbar.
:ref:`appendItem <no-11145>`            Insert a dToolBarItem at the end of the toolbar.
:ref:`appendSeparator <no-11146>`       Inserts a separator at the end of the toolbar.
:ref:`autoBindEvents <no-11147>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-11148>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-11149>`   
:ref:`bindEvent <no-11150>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-11151>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-11152>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-11153>`          Makes this object topmost
:ref:`clear <no-11154>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-11155>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-11156>`  Given a position relative to this control, return a position relative
:ref:`copy <no-11157>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-11158>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-11159>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-11160>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-11161>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-11162>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-11163>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-11164>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-11165>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-11166>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-11167>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-11168>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-11169>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-11170>`              Draws text on the object at the specified position
:ref:`endHover <no-11171>`              
:ref:`fitToSizer <no-11172>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-11173>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-11174>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-11175>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-11176>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-11177>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-11178>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-11179>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-11180>`      Returns an object that locks the current display when created, and
:ref:`getItem <no-11181>`               Returns a reference to the item with the specified caption.
:ref:`getItemIndex <no-11182>`          Returns the index of the item with the specified caption.
:ref:`getMousePosition <no-11183>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-11184>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-11185>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-11186>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-11187>`         Returns a dict containing the object's sizer property info. The
:ref:`hasItem <no-11188>`               Given a toolbar item, returns True or False depending on whether
:ref:`hide <no-11189>`                  Make the object invisible.
:ref:`initEvents <no-11190>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-11191>`        Hook for subclasses. User subclasses should set properties
:ref:`insertButton <no-11192>`          Inserts a tool (button) to the toolbar at the specified position.
:ref:`insertControl <no-11193>`         Inserts any Dabo Control to the toolbar at the specified position.
:ref:`insertItem <no-11194>`            Insert a dToolBarItem before the specified position in the toolbar.
:ref:`insertSeparator <no-11195>`       Inserts a separator before the specified position in the toolbar.
:ref:`isContainedBy <no-11196>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-11197>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-11198>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-11199>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-11200>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-11201>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-11202>`               
:ref:`paste <no-11203>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-11204>`           
:ref:`prependButton <no-11205>`         Inserts a tool (button) to the beginning of the toolbar.
:ref:`prependControl <no-11206>`        Inserts any Dabo Control to the beginning of the toolbar.
:ref:`prependItem <no-11207>`           Insert a dToolBarItem at the beginning of the toolbar.
:ref:`prependSeparator <no-11208>`      Inserts a separator at the beginning of the toolbar.
:ref:`processDroppedFiles <no-11209>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-11210>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-11211>`            Raise the passed Dabo event.
:ref:`reCreate <no-11212>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-11213>`              Recreate the object.
:ref:`redraw <no-11214>`                Called when the object is (re)drawn.
:ref:`refresh <no-11215>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-11216>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-11217>`               Destroys the object.
:ref:`remove <no-11218>`                Removes an item from the toolbar. You can either pass a reference to
:ref:`removeDrawnObject <no-11219>`     
:ref:`sendToBack <no-11220>`            Places this object behind all others.
:ref:`setAll <no-11221>`                Set all child object properties to the passed value.
:ref:`setFocus <no-11222>`              Sets focus to the object.
:ref:`setPositionInSizer <no-11223>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-11224>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-11225>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-11226>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-11227>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-11228>`                  Make the object visible.
:ref:`showContainingPage <no-11229>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-11230>`       Display a context menu (popup) at the specified position.
:ref:`super <no-11231>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-11232>`           Remove a previously registered event binding.
:ref:`unbindKey <no-11233>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-11234>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-11235>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-11236>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods
=======

.. _no-11143:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.appendButton(self, caption, pic, toggle=False, tip='', help='', \*args, \**kwargs)

   
   Adds a tool (button) to the toolbar.
   
   You must pass a caption and an image for the button. The picture can be a
   wx.Bitmap, or a path to an image file of any supported type. If you pass
   toggle=True, the button will exist in an up and down state. Pass the
   function you want to be called when this button is clicked in an
   'OnHit' param.
   



-------

.. _no-11144:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.appendControl(self, control)

   Adds any Dabo Control to the toolbar.



-------

.. _no-11145:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.appendItem(self, itm)

   Insert a dToolBarItem at the end of the toolbar.



-------

.. _no-11146:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.appendSeparator(self)

   Inserts a separator at the end of the toolbar.



-------

.. _no-11181:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.getItem(self, caption)

   
   Returns a reference to the item with the specified caption.
   
   If the item isn't found, None is returned.
   



-------

.. _no-11182:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.getItemIndex(self, caption)

   
   Returns the index of the item with the specified caption.
   
   If the item isn't found, None is returned.
   



-------

.. _no-11188:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.hasItem(self, itm)

   
   Given a toolbar item, returns True or False depending on whether
   that item is currently in this toolbar.
   



-------

.. _no-11192:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.insertButton(self, pos, caption, pic, toggle=False, tip='', help='', \*args, \**kwargs)

   
   Inserts a tool (button) to the toolbar at the specified position.
   
   You must pass a caption and an image for the button. The picture can be a
   wx.Bitmap, or a path to an image file of any supported type. If you pass
   toggle=True, the button will exist in an up and down state. Pass the
   function you want to be called when this button is clicked in an
   'OnHit' param.
   



-------

.. _no-11193:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.insertControl(self, pos, control)

   Inserts any Dabo Control to the toolbar at the specified position.



-------

.. _no-11194:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.insertItem(self, pos, itm)

   Insert a dToolBarItem before the specified position in the toolbar.



-------

.. _no-11195:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.insertSeparator(self, pos)

   Inserts a separator before the specified position in the toolbar.



-------

.. _no-11205:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.prependButton(self, caption, pic, toggle=False, tip='', help='', \*args, \**kwargs)

   
   Inserts a tool (button) to the beginning of the toolbar.
   
   You must pass a caption and an image for the button. The picture can be a
   wx.Bitmap, or a path to an image file of any supported type. If you pass
   toggle=True, the button will exist in an up and down state. Pass the
   function you want to be called when this button is clicked in an
   'OnHit' param.
   



-------

.. _no-11206:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.prependControl(self, control)

   Inserts any Dabo Control to the beginning of the toolbar.



-------

.. _no-11207:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.prependItem(self, itm)

   Insert a dToolBarItem at the beginning of the toolbar.



-------

.. _no-11208:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.prependSeparator(self)

   Inserts a separator at the beginning of the toolbar.



-------

.. _no-11218:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.remove(self, idxOrItem, release=True)

   
   Removes an item from the toolbar. You can either pass a reference to
   the item, or its position in the toolbar. If release is True (the default),
   the item is deleted as well. If release is False, a reference to the  object
   will be returned, and the caller is responsible for deleting it.
   



-------


Methods - inherited
=====================

.. _no-11138:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11139:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-11140:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11141:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11142:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11147:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.autoBindEvents(self, force=True)
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

.. _no-11148:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11149:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11150:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-11151:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-11152:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-11153:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11154:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11155:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11156:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11157:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11158:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11159:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11160:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11161:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-11162:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11163:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11164:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11165:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11166:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11167:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11168:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11169:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11170:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11171:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11172:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11173:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-11174:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-11175:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-11176:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11177:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11178:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11179:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11180:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11183:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11184:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11185:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-11186:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11187:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11189:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11190:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11191:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11196:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11197:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-11198:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.lockDisplay(self)
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

.. _no-11199:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11200:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11201:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11202:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11203:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11204:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11209:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11210:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11211:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11212:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-11213:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11214:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11215:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11216:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11217:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11219:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11220:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11221:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-11222:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11223:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11224:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-11225:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-11226:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11227:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11228:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11229:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11230:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11231:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11232:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-11233:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11234:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11235:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-11236:

.. function:: dabo.ui.uiwx.dToolBar.dToolBar.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
