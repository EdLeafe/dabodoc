
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dBorderlessButton

.. _dabo.ui.uiwx.dBorderlessButton.dBorderlessButton:

============================================================
|doc_title|  **dBorderlessButton.dBorderlessButton** - class
============================================================


Creates a button that can be pressed by the user to trigger an action.

Example::

        class MyButton(dabo.ui.dBorderlessButton):
            def initProperties(self):
                self.Caption = "Press Me"

            def onHit(self, evt):
                self.Caption = "Press Me one more time"





|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dBorderlessButton**

.. inheritance-diagram:: dBorderlessButton


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`
* wx.lib.platebtn.PlateButton - can not provide a link



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



     - no image available



     - .. image:: _static/nixWidgets/dBorderlessButton.png
          :scale: 75 %
          :target: _static/nixWidgets/dBorderlessButton.png
          :alt: dBorderlessButton


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton

   .. automethod:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.__init__

|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-12054>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-12055>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BackColorHover <no-12056>`         Color of the button background when mouse is hovered over control (str or tuple)
:ref:`BaseClass <no-12057>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-12058>`            Base key used when saving/restoring preferences  (str)
:ref:`Bitmap <no-12059>`                 The bitmap normally displayed on the button.  (wx.Bitmap)
:ref:`BorderColor <no-12060>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-12061>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-12062>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-12063>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-12064>`                 The position of the bottom side of the object. This is a
:ref:`ButtonShape <no-12065>`            
:ref:`Caption <no-12066>`                The caption of the object. (str)
:ref:`Children <no-12067>`               Returns a list of object references to the children of
:ref:`Class <no-12068>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-12069>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-12070>`   Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-12071>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-12072>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-12073>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-12074>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-12075>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-12076>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-12077>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-12078>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-12079>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-12080>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-12081>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-12082>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-12083>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-12084>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-12085>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-12086>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-12087>`          Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-12088>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-12089>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-12090>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-12091>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-12092>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-12093>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-12094>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-12095>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-12096>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-12097>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-12098>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-12099>`                Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-12100>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-12101>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-12102>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-12103>`               Specifies the font face. (str)
:ref:`FontInfo <no-12104>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-12105>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-12106>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-12107>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-12108>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-12109>`                   Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-12110>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-12111>`        Specifies the context-sensitive help text associated with this
:ref:`Hover <no-12112>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-12113>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-12114>`              Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-12115>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-12116>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-12117>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-12118>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-12119>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-12120>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-12121>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-12122>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-12123>`               Specifies the base name of the object.
:ref:`Parent <no-12124>`                 The containing object. (obj)
:ref:`Picture <no-12125>`                Specifies the image normally displayed on the button. (str)
:ref:`Position <no-12126>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-12127>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-12128>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-12129>`                  The position of the right side of the object. This is a
:ref:`Size <no-12130>`                   The size of the object. (tuple)
:ref:`Sizer <no-12131>`                  The sizer for the object.
:ref:`StatusText <no-12132>`             Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-12133>`                Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-12134>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-12135>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-12136>`                    The top position of the object. (int)
:ref:`Transparency <no-12137>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-12138>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-12139>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-12140>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-12141>`                  The width of the object. (int)
:ref:`WindowHandle <no-12142>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties
==========

.. _no-12056:

**BackColorHover** 

Color of the button background when mouse is hovered over control (str or tuple)
Default=(128, 128, 128)
Changing this color with change the color of the control when pressed as well.



-------

.. _no-12059:

**Bitmap** 

The bitmap normally displayed on the button.  (wx.Bitmap)



-------

.. _no-12065:

**ButtonShape** 



-------

.. _no-12125:

**Picture** 

Specifies the image normally displayed on the button. (str)



-------


Properties - inherited
========================

.. _no-12054:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12055:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12057:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12058:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12060:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12061:

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

.. _no-12062:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12063:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12064:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12066:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12067:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-12068:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12069:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12070:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12071:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12072:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12073:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12074:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12075:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12076:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12077:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12078:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12079:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12080:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12081:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12082:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12083:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12084:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12085:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12086:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12087:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12088:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12089:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12090:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12091:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12092:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12093:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12094:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12095:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12096:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12097:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12098:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12099:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-12100:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-12101:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12102:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12103:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12104:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12105:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12106:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12107:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12108:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12109:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12110:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12111:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12112:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12113:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12114:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12115:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12116:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12117:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12118:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12119:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12120:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12121:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12122:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-12123:

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

.. _no-12124:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-12126:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-12127:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12128:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12129:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12130:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-12131:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-12132:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12133:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-12134:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12135:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12136:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12137:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12138:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12139:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12140:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12141:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12142:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-12143>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-12144>`                 Occurs after the control or form is created.
:ref:`Destroy <no-12145>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-12146>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-12147>`               Occurs when the control gets the focus.
:ref:`Idle <no-12148>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-12149>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-12150>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-12151>`               
:ref:`KeyUp <no-12152>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-12153>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-12154>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-12155>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-12156>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-12157>`             
:ref:`MouseLeave <no-12158>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-12159>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-12160>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-12161>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-12162>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-12163>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-12164>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-12165>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-12166>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-12167>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-12168>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-12169>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-12170>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-12171>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-12172>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-12173>`                   Occurs when the control's position changes.
:ref:`Paint <no-12174>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-12175>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-12176>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-12177>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-12178>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-12143:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-12144:

**Create** 

Occurs after the control or form is created.



-------

.. _no-12145:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-12146:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-12147:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-12148:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-12149:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-12150:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-12151:

**KeyEvent** 



-------

.. _no-12152:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-12153:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-12154:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-12155:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-12156:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-12157:

**MouseEvent** 



-------

.. _no-12158:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-12159:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-12160:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-12161:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-12162:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-12163:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-12164:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-12165:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-12166:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-12167:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-12168:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-12169:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-12170:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-12171:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-12172:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-12173:

**Move** 

Occurs when the control's position changes.



-------

.. _no-12174:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-12175:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-12176:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-12177:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-12178:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


=============================================== ========================
:ref:`absoluteCoordinates <no-12179>`           Translates a position value for a control to absolute screen position.
:ref:`addObject <no-12180>`                     Instantiate object as a child of self.
:ref:`afterInit <no-12181>`                     Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-12182>`                  
:ref:`afterSetProperties <no-12183>`            
:ref:`autoBindEvents <no-12184>`                Automatically bind any on*() methods to the associated event.
:ref:`base_AcceptsFocus <no-12185>`             Please use PyControl.AcceptsFocus instead.
:ref:`base_AcceptsFocusFromKeyboard <no-12186>` Please use PyControl.AcceptsFocusFromKeyboard instead.
:ref:`base_AddChild <no-12187>`                 Please use PyControl.AddChild instead.
:ref:`base_DoGetBestSize <no-12188>`            Please use PyControl.DoGetBestSize instead.
:ref:`base_DoGetClientSize <no-12189>`          Please use PyControl.DoGetClientSize instead.
:ref:`base_DoGetPosition <no-12190>`            Please use PyControl.DoGetPosition instead.
:ref:`base_DoGetSize <no-12191>`                Please use PyControl.DoGetSize instead.
:ref:`base_DoGetVirtualSize <no-12192>`         Please use PyControl.DoGetVirtualSize instead.
:ref:`base_DoMoveWindow <no-12193>`             Please use PyControl.DoMoveWindow instead.
:ref:`base_DoSetClientSize <no-12194>`          Please use PyControl.DoSetClientSize instead.
:ref:`base_DoSetSize <no-12195>`                Please use PyControl.DoSetSize instead.
:ref:`base_DoSetVirtualSize <no-12196>`         Please use PyControl.DoSetVirtualSize instead.
:ref:`base_Enable <no-12197>`                   Please use PyControl.Enable instead.
:ref:`base_GetDefaultAttributes <no-12198>`     Please use PyControl.GetDefaultAttributes instead.
:ref:`base_GetMaxSize <no-12199>`               Please use PyControl.GetMaxSize instead.
:ref:`base_InitDialog <no-12200>`               Please use PyControl.InitDialog instead.
:ref:`base_OnInternalIdle <no-12201>`           Please use PyControl.OnInternalIdle instead.
:ref:`base_RemoveChild <no-12202>`              Please use PyControl.RemoveChild instead.
:ref:`base_ShouldInheritColours <no-12203>`     Please use PyControl.ShouldInheritColours instead.
:ref:`base_TransferDataFromWindow <no-12204>`   Please use PyControl.TransferDataFromWindow instead.
:ref:`base_TransferDataToWindow <no-12205>`     Please use PyControl.TransferDataToWindow instead.
:ref:`base_Validate <no-12206>`                 Please use PyControl.Validate instead.
:ref:`beforeInit <no-12207>`                    Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-12208>`           
:ref:`bindEvent <no-12209>`                     Bind a dEvent to a callback function.
:ref:`bindEvents <no-12210>`                    Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-12211>`                       Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-12212>`                  Makes this object topmost
:ref:`clear <no-12213>`                         Clears the background of custom-drawn objects.
:ref:`clone <no-12214>`                         Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-12215>`          Given a position relative to this control, return a position relative
:ref:`copy <no-12216>`                          Called by uiApp when the user requests a copy operation.
:ref:`cut <no-12217>`                           Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-12218>`                       Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-12219>`                    Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-12220>`                    Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-12221>`                   Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-12222>`               Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-12223>`                  Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-12224>`                      Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-12225>`                 Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-12226>`                   Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-12227>`                 Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-12228>`          Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-12229>`                      Draws text on the object at the specified position
:ref:`endHover <no-12230>`                      
:ref:`fitToSizer <no-12231>`                    Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-12232>`                    Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-12233>`                Reset the font zoom back to zero.
:ref:`fontZoomOut <no-12234>`                   Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-12235>`               Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-12236>`               Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-12237>`              Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-12238>`             Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-12239>`              Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-12240>`              Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-12241>`            Convenience method to let you call this directly on the object.
:ref:`getProperties <no-12242>`                 Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-12243>`                  Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-12244>`                 Returns a dict containing the object's sizer property info. The
:ref:`hide <no-12245>`                          Make the object invisible.
:ref:`initEvents <no-12246>`                    Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-12247>`                Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-12248>`                 Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-12249>`                   Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-12250>`                   Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-12251>`             Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-12252>`            Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-12253>`             Given a position relative to the form, return a position relative
:ref:`onHover <no-12254>`                       
:ref:`paste <no-12255>`                         Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-12256>`                   
:ref:`processDroppedFiles <no-12257>`           Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-12258>`            Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-12259>`                    Raise the passed Dabo event.
:ref:`reCreate <no-12260>`                      Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-12261>`                      Recreate the object.
:ref:`redraw <no-12262>`                        Called when the object is (re)drawn.
:ref:`refresh <no-12263>`                       Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-12264>`           Translates an absolute screen position to position value for a control.
:ref:`release <no-12265>`                       Destroys the object.
:ref:`removeDrawnObject <no-12266>`             
:ref:`sendToBack <no-12267>`                    Places this object behind all others.
:ref:`setAll <no-12268>`                        Set all child object properties to the passed value.
:ref:`setFocus <no-12269>`                      Sets focus to the object.
:ref:`setPositionInSizer <no-12270>`            Convenience method to let you call this directly on the object.
:ref:`setProperties <no-12271>`                 Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-12272>`         Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-12273>`                  Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-12274>`                 Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-12275>`                          Make the object visible.
:ref:`showContainingPage <no-12276>`            If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-12277>`               Display a context menu (popup) at the specified position.
:ref:`super <no-12278>`                         This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-12279>`                   Remove a previously registered event binding.
:ref:`unbindKey <no-12280>`                     Unbind a previously bound key combination.
:ref:`unlockDisplay <no-12281>`                 Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-12282>`              Immediately unlocks the display, no matter how many previous
:ref:`update <no-12283>`                        Update the properties of this object and all contained objects.

=============================================== ========================


Methods - inherited
=====================

.. _no-12179:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12180:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-12181:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12182:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12183:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12184:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.autoBindEvents(self, force=True)
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

.. _no-12185:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.base_AcceptsFocus(*args, \**kwargs)
   :noindex:


   Please use PyControl.AcceptsFocus instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-12186:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.base_AcceptsFocusFromKeyboard(*args, \**kwargs)
   :noindex:


   Please use PyControl.AcceptsFocusFromKeyboard instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-12187:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.base_AddChild(*args, \**kwargs)
   :noindex:


   Please use PyControl.AddChild instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-12188:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.base_DoGetBestSize(*args, \**kwargs)
   :noindex:


   Please use PyControl.DoGetBestSize instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-12189:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.base_DoGetClientSize(*args, \**kwargs)
   :noindex:


   Please use PyControl.DoGetClientSize instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-12190:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.base_DoGetPosition(*args, \**kwargs)
   :noindex:


   Please use PyControl.DoGetPosition instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-12191:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.base_DoGetSize(*args, \**kwargs)
   :noindex:


   Please use PyControl.DoGetSize instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-12192:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.base_DoGetVirtualSize(*args, \**kwargs)
   :noindex:


   Please use PyControl.DoGetVirtualSize instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-12193:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.base_DoMoveWindow(*args, \**kwargs)
   :noindex:


   Please use PyControl.DoMoveWindow instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-12194:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.base_DoSetClientSize(*args, \**kwargs)
   :noindex:


   Please use PyControl.DoSetClientSize instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-12195:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.base_DoSetSize(*args, \**kwargs)
   :noindex:


   Please use PyControl.DoSetSize instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-12196:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.base_DoSetVirtualSize(*args, \**kwargs)
   :noindex:


   Please use PyControl.DoSetVirtualSize instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-12197:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.base_Enable(*args, \**kwargs)
   :noindex:


   Please use PyControl.Enable instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-12198:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.base_GetDefaultAttributes(*args, \**kwargs)
   :noindex:


   Please use PyControl.GetDefaultAttributes instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-12199:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.base_GetMaxSize(*args, \**kwargs)
   :noindex:


   Please use PyControl.GetMaxSize instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-12200:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.base_InitDialog(*args, \**kwargs)
   :noindex:


   Please use PyControl.InitDialog instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-12201:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.base_OnInternalIdle(*args, \**kwargs)
   :noindex:


   Please use PyControl.OnInternalIdle instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-12202:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.base_RemoveChild(*args, \**kwargs)
   :noindex:


   Please use PyControl.RemoveChild instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-12203:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.base_ShouldInheritColours(*args, \**kwargs)
   :noindex:


   Please use PyControl.ShouldInheritColours instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-12204:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.base_TransferDataFromWindow(*args, \**kwargs)
   :noindex:


   Please use PyControl.TransferDataFromWindow instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-12205:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.base_TransferDataToWindow(*args, \**kwargs)
   :noindex:


   Please use PyControl.TransferDataToWindow instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-12206:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.base_Validate(*args, \**kwargs)
   :noindex:


   Please use PyControl.Validate instead.


Inherited from: 'wx._controls.PyControl - can not provide a link

-------

.. _no-12207:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12208:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12209:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-12210:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-12211:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-12212:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12213:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12214:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12215:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12216:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12217:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12218:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12219:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12220:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-12221:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12222:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12223:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12224:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12225:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12226:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12227:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12228:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12229:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12230:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12231:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12232:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12233:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12234:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12235:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12236:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12237:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12238:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12239:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12240:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12241:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12242:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-12243:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12244:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12245:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12246:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12247:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12248:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12249:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12250:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.lockDisplay(self)
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

.. _no-12251:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12252:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12253:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12254:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12255:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12256:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12257:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12258:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12259:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12260:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-12261:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12262:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12263:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12264:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12265:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12266:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12267:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12268:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-12269:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12270:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12271:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-12272:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-12273:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12274:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12275:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12276:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12277:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12278:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-12279:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-12280:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12281:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12282:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-12283:

.. function:: dabo.ui.uiwx.dBorderlessButton.dBorderlessButton.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
