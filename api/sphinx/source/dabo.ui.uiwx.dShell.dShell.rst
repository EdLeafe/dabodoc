
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dShell

.. _dabo.ui.uiwx.dShell.dShell:

======================================
|doc_title|  **dShell.dShell** - class
======================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dShell**

.. inheritance-diagram:: dShell


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`
* :ref:`wx.py.shell.Shell`



|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - .. image:: _static/macWidgets/dShell.png
          :scale: 75 %
          :target: _static/macWidgets/dShell.png
          :alt: dShell



     - .. image:: _static/winWidgets/dShell.png
          :scale: 75 %
          :target: _static/winWidgets/dShell.png
          :alt: dShell



     - .. image:: _static/nixWidgets/dShell.png
          :scale: 75 %
          :target: _static/nixWidgets/dShell.png
          :alt: dShell


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dShell.dShell

   .. automethod:: dabo.ui.uiwx.dShell.dShell.__init__

|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-32049>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-32050>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-32051>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-32052>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-32053>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-32054>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-32055>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-32056>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-32057>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-32058>`                The caption of the object. (str)
:ref:`Children <no-32059>`               Returns a list of object references to the children of
:ref:`Class <no-32060>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-32061>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-32062>`   Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-32063>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-32064>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-32065>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-32066>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-32067>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-32068>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-32069>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-32070>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-32071>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-32072>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-32073>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-32074>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-32075>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-32076>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-32077>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-32078>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-32079>`          Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-32080>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-32081>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-32082>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-32083>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-32084>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-32085>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-32086>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-32087>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-32088>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-32089>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-32090>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-32091>`                Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-32092>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-32093>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-32094>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-32095>`               Name of the font face used in the shell  (str)
:ref:`FontInfo <no-32096>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-32097>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-32098>`               Size of the font used in the shell  (int)
:ref:`FontUnderline <no-32099>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-32100>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-32101>`                   Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-32102>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-32103>`        Specifies the context-sensitive help text associated with this
:ref:`Hover <no-32104>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-32105>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-32106>`              Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-32107>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-32108>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-32109>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-32110>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-32111>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-32112>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-32113>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-32114>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-32115>`               Specifies the base name of the object.
:ref:`Parent <no-32116>`                 The containing object. (obj)
:ref:`Position <no-32117>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-32118>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-32119>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-32120>`                  The position of the right side of the object. This is a
:ref:`Size <no-32121>`                   The size of the object. (tuple)
:ref:`Sizer <no-32122>`                  The sizer for the object.
:ref:`StatusText <no-32123>`             Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-32124>`                Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-32125>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-32126>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-32127>`                    The top position of the object. (int)
:ref:`Transparency <no-32128>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-32129>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-32130>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-32131>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-32132>`                  The width of the object. (int)
:ref:`WindowHandle <no-32133>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties - inherited
========================

.. _no-32049:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32050:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32051:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32052:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32053:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32054:

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

.. _no-32055:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32056:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32057:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-32058:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32059:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-32060:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32061:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32062:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32063:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32064:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32065:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32066:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32067:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32068:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32069:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32070:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32071:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32072:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32073:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32074:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32075:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32076:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32077:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32078:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32079:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32080:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32081:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32082:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32083:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32084:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32085:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32086:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32087:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32088:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32089:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32090:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32091:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-32092:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-32093:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32094:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32095:

**FontFace** 

Name of the font face used in the shell  (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32096:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32097:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32098:

**FontSize** 

Size of the font used in the shell  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32099:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32100:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32101:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-32102:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32103:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32104:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32105:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32106:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32107:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32108:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32109:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32110:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32111:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32112:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32113:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32114:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-32115:

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

.. _no-32116:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-32117:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-32118:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32119:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32120:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-32121:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-32122:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-32123:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32124:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-32125:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32126:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32127:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32128:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32129:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32130:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32131:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32132:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32133:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-32134>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-32135>`                 Occurs after the control or form is created.
:ref:`Destroy <no-32136>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-32137>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-32138>`               Occurs when the control gets the focus.
:ref:`Idle <no-32139>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-32140>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-32141>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-32142>`               
:ref:`KeyUp <no-32143>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-32144>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-32145>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-32146>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-32147>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-32148>`             
:ref:`MouseLeave <no-32149>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-32150>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-32151>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-32152>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-32153>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-32154>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-32155>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-32156>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-32157>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-32158>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-32159>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-32160>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-32161>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-32162>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-32163>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-32164>`                   Occurs when the control's position changes.
:ref:`Paint <no-32165>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-32166>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-32167>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-32168>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-32169>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-32134:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-32135:

**Create** 

Occurs after the control or form is created.



-------

.. _no-32136:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-32137:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-32138:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-32139:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-32140:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-32141:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-32142:

**KeyEvent** 



-------

.. _no-32143:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-32144:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-32145:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-32146:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-32147:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-32148:

**MouseEvent** 



-------

.. _no-32149:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-32150:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-32151:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-32152:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-32153:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-32154:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-32155:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-32156:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-32157:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-32158:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-32159:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-32160:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-32161:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-32162:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-32163:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-32164:

**Move** 

Occurs when the control's position changes.



-------

.. _no-32165:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-32166:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-32167:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-32168:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-32169:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`about <no-32170>`                 Display information about Py.
:ref:`absoluteCoordinates <no-32171>`   Translates a position value for a control to absolute screen position.
:ref:`addHistory <no-32172>`            Add command to the command history.
:ref:`addObject <no-32173>`             Instantiate object as a child of self.
:ref:`afterInit <no-32174>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-32175>`          
:ref:`afterSetProperties <no-32176>`    
:ref:`ask <no-32177>`                   Get response from the user using a dialog box.
:ref:`autoBindEvents <no-32178>`        Automatically bind any on*() methods to the associated event.
:ref:`autoCallTipShow <no-32179>`       Display argument spec and docstring in a popup window.
:ref:`autoCompleteShow <no-32180>`      Display auto-completion popup list.
:ref:`beforeInit <no-32181>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-32182>`   
:ref:`bindEvent <no-32183>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-32184>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-32185>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-32186>`          Makes this object topmost
:ref:`clear <no-32187>`                 Clears the background of custom-drawn objects.
:ref:`clearCommand <no-32188>`          Delete the current, unexecuted command.
:ref:`clearHistory <no-32189>`          
:ref:`clone <no-32190>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-32191>`  Given a position relative to this control, return a position relative
:ref:`copy <no-32192>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-32193>`                   Called by uiApp when the user requests a cut operation.
:ref:`destroy <no-32194>`               
:ref:`drawArc <no-32195>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-32196>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-32197>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-32198>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-32199>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-32200>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-32201>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-32202>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-32203>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-32204>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-32205>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-32206>`              Draws text on the object at the specified position
:ref:`endHover <no-32207>`              
:ref:`execStartupScript <no-32208>`     Execute the user's PYTHONSTARTUP script if they have one.
:ref:`fitToSizer <no-32209>`            Resize the control to fit the size required by its sizer.
:ref:`fixLineEndings <no-32210>`        Return text with line endings replaced by OS-specific endings.
:ref:`fontZoomIn <no-32211>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-32212>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-32213>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-32214>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-32215>`       Return the fully qualified name of the object.
:ref:`getAutoCompleteList <no-32216>`   
:ref:`getCaptureBitmap <no-32217>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getCommand <no-32218>`            Extract a command from text which may include a shell prompt.
:ref:`getContainingPage <no-32219>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-32220>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-32221>`      Returns the current mouse position on the entire screen
:ref:`getMultilineCommand <no-32222>`   Extract a multi-line command from the editor.
:ref:`getPositionInSizer <no-32223>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-32224>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-32225>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-32226>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-32227>`                  Make the object invisible.
:ref:`initEvents <no-32228>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-32229>`        Hook for subclasses. User subclasses should set properties
:ref:`insertLineBreak <no-32230>`       Insert a new line break.
:ref:`isContainedBy <no-32231>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-32232>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-32233>`           Locks the visual updates to the control.
:ref:`lstripPrompt <no-32234>`          Return text without a leading prompt.
:ref:`moveTabOrderAfter <no-32235>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-32236>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-32237>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-32238>`               
:ref:`paste <no-32239>`                 Called by uiApp when the user requests a paste operation.
:ref:`pause <no-32240>`                 Halt execution pending a response from the user.
:ref:`posIsWithin <no-32241>`           
:ref:`processDroppedFiles <no-32242>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-32243>`    Handler for text dropped on the control. Override in your
:ref:`processLine <no-32244>`           This is part of the underlying class. We need to add the command that
:ref:`prompt <no-32245>`                Display proper prompt for the context: ps1, ps2 or ps3.
:ref:`push <no-32246>`                  Need to raise an event when the interpreter executes a command.
:ref:`quit <no-32247>`                  Quit the application.
:ref:`raiseEvent <no-32248>`            Raise the passed Dabo event.
:ref:`raw_input <no-32249>`             Return string based on user input.
:ref:`reCreate <no-32250>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`readline <no-32251>`              Replacement for stdin.readline().
:ref:`readlines <no-32252>`             Replacement for stdin.readlines().
:ref:`recreate <no-32253>`              Recreate the object.
:ref:`redirectStderr <no-32254>`        If redirect is true then sys.stderr will go to the shell.
:ref:`redirectStdin <no-32255>`         If redirect is true then sys.stdin will come from the shell.
:ref:`redirectStdout <no-32256>`        If redirect is true then sys.stdout will go to the shell.
:ref:`redraw <no-32257>`                Called when the object is (re)drawn.
:ref:`refresh <no-32258>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-32259>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-32260>`               Destroys the object.
:ref:`removeDrawnObject <no-32261>`     
:ref:`replaceFromHistory <no-32262>`    Replace selection with command from the history buffer.
:ref:`run <no-32263>`                   Execute command as if it was typed in directly.
:ref:`runfile <no-32264>`               Execute all commands in file as if they were typed into the
:ref:`sendToBack <no-32265>`            Places this object behind all others.
:ref:`setAll <no-32266>`                Set all child object properties to the passed value.
:ref:`setBuiltinKeywords <no-32267>`    Create pseudo keywords as part of builtins.
:ref:`setDefaultFont <no-32268>`        
:ref:`setDisplayLineNumbers <no-32269>` 
:ref:`setFocus <no-32270>`              Sets focus to the object.
:ref:`setLocalShell <no-32271>`         Add 'shell' to locals as reference to ShellFacade instance.
:ref:`setPositionInSizer <no-32272>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-32273>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-32274>` Sets a group of properties on the object all at once. This
:ref:`setPyFont <no-32275>`             
:ref:`setSizerProp <no-32276>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-32277>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`setStatusText <no-32278>`         Display status information.
:ref:`setStyles <no-32279>`             Configure font size, typeface and color for lexer.
:ref:`show <no-32280>`                  Make the object visible.
:ref:`showContainingPage <no-32281>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-32282>`       Display a context menu (popup) at the specified position.
:ref:`showIntro <no-32283>`             Display introductory text in the shell.
:ref:`super <no-32284>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-32285>`           Remove a previously registered event binding.
:ref:`unbindKey <no-32286>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-32287>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-32288>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-32289>`                Update the properties of this object and all contained objects.
:ref:`wrap <no-32290>`                  Sets whether text is word wrapped.
:ref:`write <no-32291>`                 Display text in the shell.
:ref:`writeErr <no-32292>`              Replacement for stderr.
:ref:`writeOut <no-32293>`              Replacement for stdout.
:ref:`zoom <no-32294>`                  Set the zoom level.

======================================= ========================


Methods
=======

.. _no-32216:

.. function:: dabo.ui.uiwx.dShell.dShell.getAutoCompleteList(self, cmd)



-------

.. _no-32244:

.. function:: dabo.ui.uiwx.dShell.dShell.processLine(self)

   
   This is part of the underlying class. We need to add the command that
   gets processed into our internal stack.
   



-------

.. _no-32246:

.. function:: dabo.ui.uiwx.dShell.dShell.push(self, command, silent=False)

   Need to raise an event when the interpreter executes a command.



-------

.. _no-32268:

.. function:: dabo.ui.uiwx.dShell.dShell.setDefaultFont(self, fontFace, fontSize)



-------

.. _no-32275:

.. function:: dabo.ui.uiwx.dShell.dShell.setPyFont(self, fontFace, fontSize)



-------


Methods - inherited
=====================

.. _no-32170:

.. function:: dabo.ui.uiwx.dShell.dShell.about(self)
   :noindex:


   Display information about Py.


Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32171:

.. function:: dabo.ui.uiwx.dShell.dShell.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32172:

.. function:: dabo.ui.uiwx.dShell.dShell.addHistory(self, command)
   :noindex:


   Add command to the command history.


Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32173:

.. function:: dabo.ui.uiwx.dShell.dShell.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-32174:

.. function:: dabo.ui.uiwx.dShell.dShell.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32175:

.. function:: dabo.ui.uiwx.dShell.dShell.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32176:

.. function:: dabo.ui.uiwx.dShell.dShell.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32177:

.. function:: dabo.ui.uiwx.dShell.dShell.ask(self, prompt='Please enter your response:')
   :noindex:


   Get response from the user using a dialog box.


Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32178:

.. function:: dabo.ui.uiwx.dShell.dShell.autoBindEvents(self, force=True)
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

.. _no-32179:

.. function:: dabo.ui.uiwx.dShell.dShell.autoCallTipShow(self, command, insertcalltip=True, forceCallTip=False)
   :noindex:


   Display argument spec and docstring in a popup window.


Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32180:

.. function:: dabo.ui.uiwx.dShell.dShell.autoCompleteShow(self, command, offset=0)
   :noindex:


   Display auto-completion popup list.


Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32181:

.. function:: dabo.ui.uiwx.dShell.dShell.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32182:

.. function:: dabo.ui.uiwx.dShell.dShell.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32183:

.. function:: dabo.ui.uiwx.dShell.dShell.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-32184:

.. function:: dabo.ui.uiwx.dShell.dShell.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-32185:

.. function:: dabo.ui.uiwx.dShell.dShell.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-32186:

.. function:: dabo.ui.uiwx.dShell.dShell.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32187:

.. function:: dabo.ui.uiwx.dShell.dShell.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32188:

.. function:: dabo.ui.uiwx.dShell.dShell.clearCommand(self)
   :noindex:


   Delete the current, unexecuted command.


Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32189:

.. function:: dabo.ui.uiwx.dShell.dShell.clearHistory(self)
   :noindex:



Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32190:

.. function:: dabo.ui.uiwx.dShell.dShell.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32191:

.. function:: dabo.ui.uiwx.dShell.dShell.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32192:

.. function:: dabo.ui.uiwx.dShell.dShell.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32193:

.. function:: dabo.ui.uiwx.dShell.dShell.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32194:

.. function:: dabo.ui.uiwx.dShell.dShell.destroy(self)
   :noindex:



Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32195:

.. function:: dabo.ui.uiwx.dShell.dShell.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32196:

.. function:: dabo.ui.uiwx.dShell.dShell.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32197:

.. function:: dabo.ui.uiwx.dShell.dShell.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-32198:

.. function:: dabo.ui.uiwx.dShell.dShell.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32199:

.. function:: dabo.ui.uiwx.dShell.dShell.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32200:

.. function:: dabo.ui.uiwx.dShell.dShell.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32201:

.. function:: dabo.ui.uiwx.dShell.dShell.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32202:

.. function:: dabo.ui.uiwx.dShell.dShell.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32203:

.. function:: dabo.ui.uiwx.dShell.dShell.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32204:

.. function:: dabo.ui.uiwx.dShell.dShell.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32205:

.. function:: dabo.ui.uiwx.dShell.dShell.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32206:

.. function:: dabo.ui.uiwx.dShell.dShell.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32207:

.. function:: dabo.ui.uiwx.dShell.dShell.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32208:

.. function:: dabo.ui.uiwx.dShell.dShell.execStartupScript(self, startupScript)
   :noindex:


   Execute the user's PYTHONSTARTUP script if they have one.


Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32209:

.. function:: dabo.ui.uiwx.dShell.dShell.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32210:

.. function:: dabo.ui.uiwx.dShell.dShell.fixLineEndings(self, text)
   :noindex:


   Return text with line endings replaced by OS-specific endings.


Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32211:

.. function:: dabo.ui.uiwx.dShell.dShell.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-32212:

.. function:: dabo.ui.uiwx.dShell.dShell.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-32213:

.. function:: dabo.ui.uiwx.dShell.dShell.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-32214:

.. function:: dabo.ui.uiwx.dShell.dShell.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32215:

.. function:: dabo.ui.uiwx.dShell.dShell.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32217:

.. function:: dabo.ui.uiwx.dShell.dShell.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32218:

.. function:: dabo.ui.uiwx.dShell.dShell.getCommand(self, text=None, rstrip=True)
   :noindex:


   Extract a command from text which may include a shell prompt.
   
           The command may not necessarily be valid Python syntax.


Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32219:

.. function:: dabo.ui.uiwx.dShell.dShell.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32220:

.. function:: dabo.ui.uiwx.dShell.dShell.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32221:

.. function:: dabo.ui.uiwx.dShell.dShell.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32222:

.. function:: dabo.ui.uiwx.dShell.dShell.getMultilineCommand(self, rstrip=True)
   :noindex:


   Extract a multi-line command from the editor.
   
           The command may not necessarily be valid Python syntax.


Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32223:

.. function:: dabo.ui.uiwx.dShell.dShell.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32224:

.. function:: dabo.ui.uiwx.dShell.dShell.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-32225:

.. function:: dabo.ui.uiwx.dShell.dShell.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32226:

.. function:: dabo.ui.uiwx.dShell.dShell.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32227:

.. function:: dabo.ui.uiwx.dShell.dShell.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32228:

.. function:: dabo.ui.uiwx.dShell.dShell.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32229:

.. function:: dabo.ui.uiwx.dShell.dShell.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32230:

.. function:: dabo.ui.uiwx.dShell.dShell.insertLineBreak(self)
   :noindex:


   Insert a new line break.


Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32231:

.. function:: dabo.ui.uiwx.dShell.dShell.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32232:

.. function:: dabo.ui.uiwx.dShell.dShell.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-32233:

.. function:: dabo.ui.uiwx.dShell.dShell.lockDisplay(self)
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

.. _no-32234:

.. function:: dabo.ui.uiwx.dShell.dShell.lstripPrompt(self, text)
   :noindex:


   Return text without a leading prompt.


Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32235:

.. function:: dabo.ui.uiwx.dShell.dShell.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32236:

.. function:: dabo.ui.uiwx.dShell.dShell.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32237:

.. function:: dabo.ui.uiwx.dShell.dShell.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32238:

.. function:: dabo.ui.uiwx.dShell.dShell.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32239:

.. function:: dabo.ui.uiwx.dShell.dShell.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32240:

.. function:: dabo.ui.uiwx.dShell.dShell.pause(self)
   :noindex:


   Halt execution pending a response from the user.


Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32241:

.. function:: dabo.ui.uiwx.dShell.dShell.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32242:

.. function:: dabo.ui.uiwx.dShell.dShell.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32243:

.. function:: dabo.ui.uiwx.dShell.dShell.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32245:

.. function:: dabo.ui.uiwx.dShell.dShell.prompt(self)
   :noindex:


   Display proper prompt for the context: ps1, ps2 or ps3.
   
           If this is a continuation line, autoindent as necessary.


Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32247:

.. function:: dabo.ui.uiwx.dShell.dShell.quit(self)
   :noindex:


   Quit the application.


Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32248:

.. function:: dabo.ui.uiwx.dShell.dShell.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32249:

.. function:: dabo.ui.uiwx.dShell.dShell.raw_input(self, prompt='')
   :noindex:


   Return string based on user input.


Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32250:

.. function:: dabo.ui.uiwx.dShell.dShell.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-32251:

.. function:: dabo.ui.uiwx.dShell.dShell.readline(self)
   :noindex:


   Replacement for stdin.readline().


Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32252:

.. function:: dabo.ui.uiwx.dShell.dShell.readlines(self)
   :noindex:


   Replacement for stdin.readlines().


Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32253:

.. function:: dabo.ui.uiwx.dShell.dShell.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32254:

.. function:: dabo.ui.uiwx.dShell.dShell.redirectStderr(self, redirect=True)
   :noindex:


   If redirect is true then sys.stderr will go to the shell.


Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32255:

.. function:: dabo.ui.uiwx.dShell.dShell.redirectStdin(self, redirect=True)
   :noindex:


   If redirect is true then sys.stdin will come from the shell.


Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32256:

.. function:: dabo.ui.uiwx.dShell.dShell.redirectStdout(self, redirect=True)
   :noindex:


   If redirect is true then sys.stdout will go to the shell.


Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32257:

.. function:: dabo.ui.uiwx.dShell.dShell.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32258:

.. function:: dabo.ui.uiwx.dShell.dShell.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32259:

.. function:: dabo.ui.uiwx.dShell.dShell.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32260:

.. function:: dabo.ui.uiwx.dShell.dShell.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32261:

.. function:: dabo.ui.uiwx.dShell.dShell.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32262:

.. function:: dabo.ui.uiwx.dShell.dShell.replaceFromHistory(self, step)
   :noindex:


   Replace selection with command from the history buffer.


Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32263:

.. function:: dabo.ui.uiwx.dShell.dShell.run(self, command, prompt=True, verbose=True)
   :noindex:


   Execute command as if it was typed in directly.
           >>> shell.run('print "this"')
           >>> print "this"
           this
           >>>
           


Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32264:

.. function:: dabo.ui.uiwx.dShell.dShell.runfile(self, filename)
   :noindex:


   Execute all commands in file as if they were typed into the
           shell.


Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32265:

.. function:: dabo.ui.uiwx.dShell.dShell.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32266:

.. function:: dabo.ui.uiwx.dShell.dShell.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-32267:

.. function:: dabo.ui.uiwx.dShell.dShell.setBuiltinKeywords(self)
   :noindex:


   Create pseudo keywords as part of builtins.
   
           This sets "close", "exit" and "quit" to a helpful string.
           


Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32269:

.. function:: dabo.ui.uiwx.dShell.dShell.setDisplayLineNumbers(self, state)
   :noindex:



Inherited from: :ref:`wx.py.editwindow.EditWindow`

-------

.. _no-32270:

.. function:: dabo.ui.uiwx.dShell.dShell.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32271:

.. function:: dabo.ui.uiwx.dShell.dShell.setLocalShell(self)
   :noindex:


   Add 'shell' to locals as reference to ShellFacade instance.


Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32272:

.. function:: dabo.ui.uiwx.dShell.dShell.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32273:

.. function:: dabo.ui.uiwx.dShell.dShell.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-32274:

.. function:: dabo.ui.uiwx.dShell.dShell.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-32276:

.. function:: dabo.ui.uiwx.dShell.dShell.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32277:

.. function:: dabo.ui.uiwx.dShell.dShell.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32278:

.. function:: dabo.ui.uiwx.dShell.dShell.setStatusText(self, text)
   :noindex:


   Display status information.


Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32279:

.. function:: dabo.ui.uiwx.dShell.dShell.setStyles(self, faces)
   :noindex:


   Configure font size, typeface and color for lexer.


Inherited from: :ref:`wx.py.editwindow.EditWindow`

-------

.. _no-32280:

.. function:: dabo.ui.uiwx.dShell.dShell.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32281:

.. function:: dabo.ui.uiwx.dShell.dShell.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32282:

.. function:: dabo.ui.uiwx.dShell.dShell.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32283:

.. function:: dabo.ui.uiwx.dShell.dShell.showIntro(self, text='')
   :noindex:


   Display introductory text in the shell.


Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32284:

.. function:: dabo.ui.uiwx.dShell.dShell.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-32285:

.. function:: dabo.ui.uiwx.dShell.dShell.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-32286:

.. function:: dabo.ui.uiwx.dShell.dShell.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32287:

.. function:: dabo.ui.uiwx.dShell.dShell.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32288:

.. function:: dabo.ui.uiwx.dShell.dShell.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32289:

.. function:: dabo.ui.uiwx.dShell.dShell.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-32290:

.. function:: dabo.ui.uiwx.dShell.dShell.wrap(self, wrap=True)
   :noindex:


   Sets whether text is word wrapped.


Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32291:

.. function:: dabo.ui.uiwx.dShell.dShell.write(self, text)
   :noindex:


   Display text in the shell.
   
           Replace line endings with OS-specific endings.


Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32292:

.. function:: dabo.ui.uiwx.dShell.dShell.writeErr(self, text)
   :noindex:


   Replacement for stderr.


Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32293:

.. function:: dabo.ui.uiwx.dShell.dShell.writeOut(self, text)
   :noindex:


   Replacement for stdout.


Inherited from: :ref:`wx.py.shell.Shell`

-------

.. _no-32294:

.. function:: dabo.ui.uiwx.dShell.dShell.zoom(self, points=0)
   :noindex:


   Set the zoom level.
   
           This number of points is added to the size of all fonts.  It
           may be positive to magnify or negative to reduce.


Inherited from: :ref:`wx.py.shell.Shell`

-------


|
