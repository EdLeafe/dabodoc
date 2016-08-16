
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dPage

.. _dabo.ui.uiwx.dPage.dPage:

====================================
|doc_title|  **dPage.dPage** - class
====================================

Creates a page to appear as a tab in a pageframe.



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dPage**

.. inheritance-diagram:: dPage


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`



|subclasses| Known Subclasses
=============================

* :ref:`dabo.lib.datanav.Page.Page`
* :ref:`dabo.ui.uiwx.dPageFrameNoTabs.TestPage`



|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - no image available



     - .. image:: _static/winWidgets/dPage.png
          :scale: 75 %
          :target: _static/winWidgets/dPage.png
          :alt: dPage



     - no image available


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dPage.dPage

   .. automethod:: dabo.ui.uiwx.dPage.dPage.__init__

|method_summary| Properties Summary
===================================


========================================= ========================
:ref:`Application <no-13000>`             Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-13001>`               Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-13002>`               The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-13003>`             Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-13004>`             Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-13005>`         Style of line for the border drawn around the control.
:ref:`BorderStyle <no-13006>`             Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-13007>`             Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-13008>`                  The position of the bottom side of the object. This is a
:ref:`Caption <no-13009>`                 The text identifying this particular page.  (str)
:ref:`Children <no-13010>`                Child controls of this panel. This excludes the wx-specific
:ref:`Class <no-13011>`                   The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-13012>`        Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-13013>`    Reference to the sizer item that control's this control's layout.
:ref:`DeferredUpdates <no-13014>`         Allow to defer controls updates until page become active.  (bool)
:ref:`DroppedFileHandler <no-13015>`      Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-13016>`      Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-13017>`        Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-13018>`      Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-13019>`  Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-13020>`      Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-13021>`      Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-13022>`          Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-13023>`          Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-13024>`             Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-13025>`         Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-13026>`         Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-13027>`       Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-13028>`         Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-13029>`    Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-13030>`        Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-13031>`           Dynamically determine the value of the Height property.
:ref:`DynamicHorizontalScroll <no-13032>` Dynamically determine the value of the HorizontalScroll property.
:ref:`DynamicImage <no-13033>`            Dynamically determine the value of the Image property.
:ref:`DynamicLeft <no-13034>`             Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-13035>`     Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-13036>`         Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-13037>`             Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-13038>`       Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-13039>`              Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-13040>`      Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-13041>`              Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-13042>`     Dynamically determine the value of the Transparency property.
:ref:`DynamicVerticalScroll <no-13043>`   Dynamically determine the value of the VerticalScroll property.
:ref:`DynamicVisible <no-13044>`          Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-13045>`            Dynamically determine the value of the Width property.
:ref:`Enabled <no-13046>`                 Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-13047>`                    Specifies font object for this control. (dFont)
:ref:`FontBold <no-13048>`                Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-13049>`         Human-readable description of the current font settings. (str)
:ref:`FontFace <no-13050>`                Specifies the font face. (str)
:ref:`FontInfo <no-13051>`                Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-13052>`              Specifies whether font is italicized. (bool)
:ref:`FontSize <no-13053>`                Specifies the point size of the font. (int)
:ref:`FontUnderline <no-13054>`           Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-13055>`               Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-13056>`                    Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-13057>`                  Specifies the height of the object. (int)
:ref:`HelpContextText <no-13058>`         Specifies the context-sensitive help text associated with this
:ref:`HorizontalScroll <no-13059>`        Controls whether this object will scroll horizontally (default=True)  (bool)
:ref:`Hover <no-13060>`                   When True, Mouse Enter events fire the onHover method, and
:ref:`Image <no-13061>`                   Sets the image that is displayed on the page tab. This is
:ref:`Left <no-13062>`                    Specifies the left position of the object. (int)
:ref:`LogEvents <no-13063>`               Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-13064>`           Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-13065>`             Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-13066>`            Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-13067>`           Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-13068>`             Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-13069>`            Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-13070>`            Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-13071>`                    Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-13072>`                Specifies the base name of the object.
:ref:`Parent <no-13073>`                  The containing object. (obj)
:ref:`Position <no-13074>`                The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-13075>`       Reference to the Preference Management object  (dPref)
:ref:`RegID <no-13076>`                   A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-13077>`                   The position of the right side of the object. This is a
:ref:`Size <no-13078>`                    The size of the object. (tuple)
:ref:`Sizer <no-13079>`                   The sizer for the object.
:ref:`StatusText <no-13080>`              Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-13081>`                 Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-13082>`                     A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-13083>`             Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-13084>`                     The top position of the object. (int)
:ref:`Transparency <no-13085>`            Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-13086>`       Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`VerticalScroll <no-13087>`          Controls whether this object will scroll vertically (default=True)  (bool)
:ref:`Visible <no-13088>`                 Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-13089>`         Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-13090>`                   The width of the object. (int)
:ref:`WindowHandle <no-13091>`            The platform-specific handle for the window. Read-only. (long)

========================================= ========================


Properties
==========

.. _no-13014:

**DeferredUpdates** 

Allow to defer controls updates until page become active.  (bool)



-------

.. _no-13033:

**DynamicImage** 

Dynamically determine the value of the Image property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Image property. If DynamicImage is set to None (the default), Image
will not be dynamically evaluated.



-------

.. _no-13061:

**Image** 

Sets the image that is displayed on the page tab. This is
    determined by the key value passed, which must refer to an
    image already added to the parent pageframe.
    When used to retrieve an image, it returns the index of the
    page's image in the parent pageframe's image list.   (int)



-------


Properties - inherited
========================

.. _no-13000:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13001:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13002:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13003:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13004:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13005:

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

.. _no-13006:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13007:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13008:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-13009:

**Caption** 

The text identifying this particular page.  (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13010:

**Children** 

Child controls of this panel. This excludes the wx-specific
    scroll bars  (list of objects)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-13011:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13012:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13013:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13015:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13016:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13017:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13018:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13019:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13020:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13021:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13022:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13023:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13024:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13025:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13026:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13027:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13028:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13029:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13030:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13031:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13032:

**DynamicHorizontalScroll** 

Dynamically determine the value of the HorizontalScroll property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HorizontalScroll property. If DynamicHorizontalScroll is set to None (the default), HorizontalScroll
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-13034:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13035:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13036:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13037:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13038:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13039:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13040:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13041:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13042:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13043:

**DynamicVerticalScroll** 

Dynamically determine the value of the VerticalScroll property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
VerticalScroll property. If DynamicVerticalScroll is set to None (the default), VerticalScroll
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-13044:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13045:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13046:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-13047:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-13048:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13049:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13050:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13051:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13052:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13053:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13054:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13055:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13056:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-13057:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13058:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13059:

**HorizontalScroll** 

Controls whether this object will scroll horizontally (default=True)  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-13060:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13062:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13063:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13064:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13065:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13066:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13067:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13068:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13069:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13070:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13071:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-13072:

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

.. _no-13073:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-13074:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-13075:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13076:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13077:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-13078:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-13079:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-13080:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13081:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-13082:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13083:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13084:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13085:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13086:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13087:

**VerticalScroll** 

Controls whether this object will scroll vertically (default=True)  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-13088:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13089:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13090:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13091:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-13092>`       Occurs when a window background has been erased and needs repainting.
:ref:`ChildBorn <no-13093>`              Occurs when a child control is created.
:ref:`ControlNavigationEvent <no-13094>` 
:ref:`Create <no-13095>`                 Occurs after the control or form is created.
:ref:`Destroy <no-13096>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-13097>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-13098>`               Occurs when the control gets the focus.
:ref:`Idle <no-13099>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-13100>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-13101>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-13102>`               
:ref:`KeyUp <no-13103>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-13104>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-13105>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-13106>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-13107>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-13108>`             
:ref:`MouseLeave <no-13109>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-13110>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-13111>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-13112>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-13113>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-13114>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-13115>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-13116>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-13117>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-13118>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-13119>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-13120>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-13121>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-13122>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-13123>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-13124>`                   Occurs when the control's position changes.
:ref:`PageContextMenu <no-13125>`        Occurs when the user requests a context event for a dPage
:ref:`PageEnter <no-13126>`              Occurs when the page becomes the active page.
:ref:`PageLeave <no-13127>`              Occurs when a different page becomes active.
:ref:`Paint <no-13128>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-13129>`                 Occurs when the control or form is resized.
:ref:`ScrollBottom <no-13130>`           Occurs when a scrollable window reaches the bottom or right.
:ref:`ScrollEvent <no-13131>`            
:ref:`ScrollLineDown <no-13132>`         Occurs when a scrollable window is scrolled a line down or right.
:ref:`ScrollLineUp <no-13133>`           Occurs when a scrollable window is scrolled a line up or left.
:ref:`ScrollPageDown <no-13134>`         Occurs when a scrollable window is scrolled down or right by a full page.
:ref:`ScrollPageUp <no-13135>`           Occurs when a scrollable window is scrolled up or left by a full page.
:ref:`ScrollThumbDrag <no-13136>`        Occurs when the 'thumb' control of a scrollable window's scrollbars is moved.
:ref:`ScrollThumbRelease <no-13137>`     Occurs when the 'thumb' control of a scrollable window's scrollbars is released.
:ref:`ScrollTop <no-13138>`              Occurs when a scrollable window reaches the top or left.
:ref:`TreeBeginDrag <no-13139>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-13140>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-13141>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-13092:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-13093:

**ChildBorn** 

Occurs when a child control is created.



-------

.. _no-13094:

**ControlNavigationEvent** 



-------

.. _no-13095:

**Create** 

Occurs after the control or form is created.



-------

.. _no-13096:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-13097:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-13098:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-13099:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-13100:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-13101:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-13102:

**KeyEvent** 



-------

.. _no-13103:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-13104:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-13105:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-13106:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-13107:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-13108:

**MouseEvent** 



-------

.. _no-13109:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-13110:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-13111:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-13112:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-13113:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-13114:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-13115:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-13116:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-13117:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-13118:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-13119:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-13120:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-13121:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-13122:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-13123:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-13124:

**Move** 

Occurs when the control's position changes.



-------

.. _no-13125:

**PageContextMenu** 

Occurs when the user requests a context event for a dPage



-------

.. _no-13126:

**PageEnter** 

Occurs when the page becomes the active page.



-------

.. _no-13127:

**PageLeave** 

Occurs when a different page becomes active.



-------

.. _no-13128:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-13129:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-13130:

**ScrollBottom** 

Occurs when a scrollable window reaches the bottom or right.



-------

.. _no-13131:

**ScrollEvent** 



-------

.. _no-13132:

**ScrollLineDown** 

Occurs when a scrollable window is scrolled a line down or right.



-------

.. _no-13133:

**ScrollLineUp** 

Occurs when a scrollable window is scrolled a line up or left.



-------

.. _no-13134:

**ScrollPageDown** 

Occurs when a scrollable window is scrolled down or right by a full page.



-------

.. _no-13135:

**ScrollPageUp** 

Occurs when a scrollable window is scrolled up or left by a full page.



-------

.. _no-13136:

**ScrollThumbDrag** 

Occurs when the 'thumb' control of a scrollable window's scrollbars is moved.



-------

.. _no-13137:

**ScrollThumbRelease** 

Occurs when the 'thumb' control of a scrollable window's scrollbars is released.



-------

.. _no-13138:

**ScrollTop** 

Occurs when a scrollable window reaches the top or left.



-------

.. _no-13139:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-13140:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-13141:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-13142>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-13143>`             Instantiate object as a child of self.
:ref:`afterInit <no-13144>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-13145>`          
:ref:`afterSetProperties <no-13146>`    
:ref:`autoBindEvents <no-13147>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-13148>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-13149>`   
:ref:`bindEvent <no-13150>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-13151>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-13152>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-13153>`          Makes this object topmost
:ref:`clear <no-13154>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-13155>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-13156>`  Given a position relative to this control, return a position relative
:ref:`copy <no-13157>`                  Called by uiApp when the user requests a copy operation.
:ref:`createItems <no-13158>`           Create the controls in the page.
:ref:`cut <no-13159>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-13160>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-13161>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-13162>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-13163>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-13164>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-13165>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-13166>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-13167>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-13168>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-13169>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-13170>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-13171>`              Draws text on the object at the specified position
:ref:`endHover <no-13172>`              
:ref:`fitToSizer <no-13173>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-13174>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-13175>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-13176>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-13177>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-13178>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-13179>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-13180>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-13181>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-13182>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-13183>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-13184>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-13185>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-13186>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-13187>`                  Make the object invisible.
:ref:`initEvents <no-13188>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-13189>`        Hook for subclasses. User subclasses should set properties
:ref:`initSizer <no-13190>`             Set up the default vertical box sizer for the page.
:ref:`isContainedBy <no-13191>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-13192>`           Call the given function on this object and all of its Children. If
:ref:`layout <no-13193>`                Wrap the wx version of the call, if possible.
:ref:`lockDisplay <no-13194>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-13195>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-13196>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-13197>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-13198>`               
:ref:`pageDown <no-13199>`              
:ref:`pageHorizontally <no-13200>`      Scroll horizontally one 'page' width.
:ref:`pageLeft <no-13201>`              
:ref:`pageRight <no-13202>`             
:ref:`pageUp <no-13203>`                
:ref:`pageVertically <no-13204>`        Scroll vertically one 'page' height.
:ref:`paste <no-13205>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-13206>`           
:ref:`processDroppedFiles <no-13207>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-13208>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-13209>`            Raise the passed Dabo event.
:ref:`reCreate <no-13210>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-13211>`              Recreate the object.
:ref:`redraw <no-13212>`                Called when the object is (re)drawn.
:ref:`refresh <no-13213>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-13214>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-13215>`               Destroys the object.
:ref:`removeDrawnObject <no-13216>`     
:ref:`scrollHorizontally <no-13217>`    Change the horizontal scroll position by 'amt' units.
:ref:`scrollVertically <no-13218>`      Change the vertical scroll position by 'amt' units.
:ref:`sendToBack <no-13219>`            Places this object behind all others.
:ref:`setAll <no-13220>`                Set all child object properties to the passed value.
:ref:`setFocus <no-13221>`              Sets focus to the object.
:ref:`setPositionInSizer <no-13222>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-13223>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-13224>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-13225>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-13226>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-13227>`                  Make the object visible.
:ref:`showContainingPage <no-13228>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-13229>`       Display a context menu (popup) at the specified position.
:ref:`super <no-13230>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-13231>`           Remove a previously registered event binding.
:ref:`unbindKey <no-13232>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-13233>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-13234>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-13235>`                

======================================= ========================


Methods
=======

.. _no-13158:

.. function:: dabo.ui.uiwx.dPage.dPage.createItems(self)

   
   Create the controls in the page.
   
   Called when the page is entered for the first time, allowing subclasses
   to delay-populate the page.
   



-------

.. _no-13190:

.. function:: dabo.ui.uiwx.dPage.dPage.initSizer(self)

   Set up the default vertical box sizer for the page.



-------

.. _no-13235:

.. function:: dabo.ui.uiwx.dPage.dPage.update(self)



-------


Methods - inherited
=====================

.. _no-13142:

.. function:: dabo.ui.uiwx.dPage.dPage.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13143:

.. function:: dabo.ui.uiwx.dPage.dPage.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-13144:

.. function:: dabo.ui.uiwx.dPage.dPage.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13145:

.. function:: dabo.ui.uiwx.dPage.dPage.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13146:

.. function:: dabo.ui.uiwx.dPage.dPage.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13147:

.. function:: dabo.ui.uiwx.dPage.dPage.autoBindEvents(self, force=True)
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

.. _no-13148:

.. function:: dabo.ui.uiwx.dPage.dPage.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13149:

.. function:: dabo.ui.uiwx.dPage.dPage.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13150:

.. function:: dabo.ui.uiwx.dPage.dPage.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-13151:

.. function:: dabo.ui.uiwx.dPage.dPage.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-13152:

.. function:: dabo.ui.uiwx.dPage.dPage.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-13153:

.. function:: dabo.ui.uiwx.dPage.dPage.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13154:

.. function:: dabo.ui.uiwx.dPage.dPage.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13155:

.. function:: dabo.ui.uiwx.dPage.dPage.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13156:

.. function:: dabo.ui.uiwx.dPage.dPage.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13157:

.. function:: dabo.ui.uiwx.dPage.dPage.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13159:

.. function:: dabo.ui.uiwx.dPage.dPage.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13160:

.. function:: dabo.ui.uiwx.dPage.dPage.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13161:

.. function:: dabo.ui.uiwx.dPage.dPage.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13162:

.. function:: dabo.ui.uiwx.dPage.dPage.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-13163:

.. function:: dabo.ui.uiwx.dPage.dPage.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13164:

.. function:: dabo.ui.uiwx.dPage.dPage.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13165:

.. function:: dabo.ui.uiwx.dPage.dPage.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13166:

.. function:: dabo.ui.uiwx.dPage.dPage.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13167:

.. function:: dabo.ui.uiwx.dPage.dPage.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13168:

.. function:: dabo.ui.uiwx.dPage.dPage.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13169:

.. function:: dabo.ui.uiwx.dPage.dPage.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13170:

.. function:: dabo.ui.uiwx.dPage.dPage.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13171:

.. function:: dabo.ui.uiwx.dPage.dPage.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13172:

.. function:: dabo.ui.uiwx.dPage.dPage.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13173:

.. function:: dabo.ui.uiwx.dPage.dPage.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13174:

.. function:: dabo.ui.uiwx.dPage.dPage.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-13175:

.. function:: dabo.ui.uiwx.dPage.dPage.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-13176:

.. function:: dabo.ui.uiwx.dPage.dPage.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-13177:

.. function:: dabo.ui.uiwx.dPage.dPage.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13178:

.. function:: dabo.ui.uiwx.dPage.dPage.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13179:

.. function:: dabo.ui.uiwx.dPage.dPage.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13180:

.. function:: dabo.ui.uiwx.dPage.dPage.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13181:

.. function:: dabo.ui.uiwx.dPage.dPage.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13182:

.. function:: dabo.ui.uiwx.dPage.dPage.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13183:

.. function:: dabo.ui.uiwx.dPage.dPage.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13184:

.. function:: dabo.ui.uiwx.dPage.dPage.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-13185:

.. function:: dabo.ui.uiwx.dPage.dPage.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13186:

.. function:: dabo.ui.uiwx.dPage.dPage.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13187:

.. function:: dabo.ui.uiwx.dPage.dPage.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13188:

.. function:: dabo.ui.uiwx.dPage.dPage.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13189:

.. function:: dabo.ui.uiwx.dPage.dPage.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13191:

.. function:: dabo.ui.uiwx.dPage.dPage.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13192:

.. function:: dabo.ui.uiwx.dPage.dPage.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-13193:

.. function:: dabo.ui.uiwx.dPage.dPage.layout(self, resetMin=False)
   :noindex:


   Wrap the wx version of the call, if possible.


Inherited from: 'dabo.ui.uiwx.dPanel._BasePanelMixin - can not provide a link

-------

.. _no-13194:

.. function:: dabo.ui.uiwx.dPage.dPage.lockDisplay(self)
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

.. _no-13195:

.. function:: dabo.ui.uiwx.dPage.dPage.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13196:

.. function:: dabo.ui.uiwx.dPage.dPage.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13197:

.. function:: dabo.ui.uiwx.dPage.dPage.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13198:

.. function:: dabo.ui.uiwx.dPage.dPage.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13199:

.. function:: dabo.ui.uiwx.dPage.dPage.pageDown(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-13200:

.. function:: dabo.ui.uiwx.dPage.dPage.pageHorizontally(self, direction)
   :noindex:


   Scroll horizontally one 'page' width.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-13201:

.. function:: dabo.ui.uiwx.dPage.dPage.pageLeft(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-13202:

.. function:: dabo.ui.uiwx.dPage.dPage.pageRight(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-13203:

.. function:: dabo.ui.uiwx.dPage.dPage.pageUp(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-13204:

.. function:: dabo.ui.uiwx.dPage.dPage.pageVertically(self, direction)
   :noindex:


   Scroll vertically one 'page' height.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-13205:

.. function:: dabo.ui.uiwx.dPage.dPage.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13206:

.. function:: dabo.ui.uiwx.dPage.dPage.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13207:

.. function:: dabo.ui.uiwx.dPage.dPage.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13208:

.. function:: dabo.ui.uiwx.dPage.dPage.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13209:

.. function:: dabo.ui.uiwx.dPage.dPage.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13210:

.. function:: dabo.ui.uiwx.dPage.dPage.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-13211:

.. function:: dabo.ui.uiwx.dPage.dPage.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13212:

.. function:: dabo.ui.uiwx.dPage.dPage.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13213:

.. function:: dabo.ui.uiwx.dPage.dPage.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13214:

.. function:: dabo.ui.uiwx.dPage.dPage.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13215:

.. function:: dabo.ui.uiwx.dPage.dPage.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13216:

.. function:: dabo.ui.uiwx.dPage.dPage.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13217:

.. function:: dabo.ui.uiwx.dPage.dPage.scrollHorizontally(self, amt)
   :noindex:


   Change the horizontal scroll position by 'amt' units.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-13218:

.. function:: dabo.ui.uiwx.dPage.dPage.scrollVertically(self, amt)
   :noindex:


   Change the vertical scroll position by 'amt' units.


Inherited from: :ref:`dabo.ui.uiwx.dPanel.dScrollPanel`

-------

.. _no-13219:

.. function:: dabo.ui.uiwx.dPage.dPage.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13220:

.. function:: dabo.ui.uiwx.dPage.dPage.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-13221:

.. function:: dabo.ui.uiwx.dPage.dPage.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13222:

.. function:: dabo.ui.uiwx.dPage.dPage.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13223:

.. function:: dabo.ui.uiwx.dPage.dPage.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-13224:

.. function:: dabo.ui.uiwx.dPage.dPage.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-13225:

.. function:: dabo.ui.uiwx.dPage.dPage.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13226:

.. function:: dabo.ui.uiwx.dPage.dPage.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13227:

.. function:: dabo.ui.uiwx.dPage.dPage.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13228:

.. function:: dabo.ui.uiwx.dPage.dPage.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13229:

.. function:: dabo.ui.uiwx.dPage.dPage.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13230:

.. function:: dabo.ui.uiwx.dPage.dPage.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-13231:

.. function:: dabo.ui.uiwx.dPage.dPage.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-13232:

.. function:: dabo.ui.uiwx.dPage.dPage.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13233:

.. function:: dabo.ui.uiwx.dPage.dPage.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-13234:

.. function:: dabo.ui.uiwx.dPage.dPage.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
