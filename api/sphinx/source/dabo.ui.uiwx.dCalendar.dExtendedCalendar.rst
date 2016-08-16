
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dCalendar

.. _dabo.ui.uiwx.dCalendar.dExtendedCalendar:

====================================================
|doc_title|  **dCalendar.dExtendedCalendar** - class
====================================================


This formats the calendar into an extended layout, with a
dropdown list for selecting any month, and a spinner for
moving from year to year. Use this when you need to be able
to navigate to any date quickly.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dExtendedCalendar**

.. inheritance-diagram:: dExtendedCalendar


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dCalendar.dExtendedCalendar

   .. automethod:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.__init__

|method_summary| Properties Summary
===================================


=========================================== ========================
:ref:`Application <no-21642>`               Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-21643>`                 Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-21644>`                 The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-21645>`               Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-21646>`               Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-21647>`           Style of line for the border drawn around the control.
:ref:`BorderStyle <no-21648>`               Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-21649>`               Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-21650>`                    The position of the bottom side of the object. This is a
:ref:`Caption <no-21651>`                   The caption of the object. (str)
:ref:`Children <no-21652>`                  Returns a list of object references to the children of
:ref:`Class <no-21653>`                     The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-21654>`          Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-21655>`      Reference to the sizer item that control's this control's layout.
:ref:`Date <no-21656>`                      The current Date of the calendar  (datetime.date)
:ref:`DroppedFileHandler <no-21657>`        Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-21658>`        Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-21659>`          Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-21660>`        Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-21661>`    Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-21662>`        Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-21663>`        Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-21664>`            Dynamically determine the value of the Caption property.
:ref:`DynamicDate <no-21665>`               Dynamically determine the value of the Date property.
:ref:`DynamicEnabled <no-21666>`            Dynamically determine the value of the Enabled property.
:ref:`DynamicFirstDayOfWeek <no-21667>`     Dynamically determine the value of the FirstDayOfWeek property.
:ref:`DynamicFixedMonth <no-21668>`         Dynamically determine the value of the FixedMonth property.
:ref:`DynamicFixedYear <no-21669>`          Dynamically determine the value of the FixedYear property.
:ref:`DynamicFont <no-21670>`               Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-21671>`           Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-21672>`           Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-21673>`         Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-21674>`           Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-21675>`      Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-21676>`          Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeaderBackColor <no-21677>`    Dynamically determine the value of the HeaderBackColor property.
:ref:`DynamicHeaderForeColor <no-21678>`    Dynamically determine the value of the HeaderForeColor property.
:ref:`DynamicHeight <no-21679>`             Dynamically determine the value of the Height property.
:ref:`DynamicHighlightBackColor <no-21680>` Dynamically determine the value of the HighlightBackColor property.
:ref:`DynamicHighlightForeColor <no-21681>` Dynamically determine the value of the HighlightForeColor property.
:ref:`DynamicHighlightHolidays <no-21682>`  Dynamically determine the value of the HighlightHolidays property.
:ref:`DynamicHolidayBackColor <no-21683>`   Dynamically determine the value of the HolidayBackColor property.
:ref:`DynamicHolidayForeColor <no-21684>`   Dynamically determine the value of the HolidayForeColor property.
:ref:`DynamicLeft <no-21685>`               Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-21686>`       Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-21687>`           Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-21688>`               Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-21689>`         Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-21690>`                Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-21691>`        Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-21692>`                Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-21693>`       Dynamically determine the value of the Transparency property.
:ref:`DynamicValue <no-21694>`              Dynamically determine the value of the Date property.
:ref:`DynamicVisible <no-21695>`            Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-21696>`              Dynamically determine the value of the Width property.
:ref:`Enabled <no-21697>`                   Specifies whether the object and children can get user input. (bool)
:ref:`FirstDayOfWeek <no-21698>`            Can be one of either 'Sunday' or 'Monday'. Determines which day
:ref:`FixedMonth <no-21699>`                When True, the user cannot change the displayed month.
:ref:`FixedYear <no-21700>`                 When True, the user cannot change the displayed month.
:ref:`Font <no-21701>`                      Specifies font object for this control. (dFont)
:ref:`FontBold <no-21702>`                  Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-21703>`           Human-readable description of the current font settings. (str)
:ref:`FontFace <no-21704>`                  Specifies the font face. (str)
:ref:`FontInfo <no-21705>`                  Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-21706>`                Specifies whether font is italicized. (bool)
:ref:`FontSize <no-21707>`                  Specifies the point size of the font. (int)
:ref:`FontUnderline <no-21708>`             Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-21709>`                 Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-21710>`                      Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`HeaderBackColor <no-21711>`           Background color of the calendar header  (str or tuple)
:ref:`HeaderForeColor <no-21712>`           Forecolor of the calendar header  (str or tuple)
:ref:`Height <no-21713>`                    Specifies the height of the object. (int)
:ref:`HelpContextText <no-21714>`           Specifies the context-sensitive help text associated with this
:ref:`HighlightBackColor <no-21715>`        Background color of the calendar highlight  (str or tuple)
:ref:`HighlightForeColor <no-21716>`        Forecolor of the calendar highlight  (str or tuple)
:ref:`HighlightHolidays <no-21717>`         Determines whether holidays are displayed as highlighted.
:ref:`HolidayBackColor <no-21718>`          Background color of the calendar holiday  (str or tuple)
:ref:`HolidayForeColor <no-21719>`          Forecolor of the calendar holiday  (str or tuple)
:ref:`Hover <no-21720>`                     When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-21721>`                      Specifies the left position of the object. (int)
:ref:`LogEvents <no-21722>`                 Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-21723>`             Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-21724>`               Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-21725>`              Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-21726>`             Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-21727>`               Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-21728>`              Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-21729>`              Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-21730>`                      Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-21731>`                  Specifies the base name of the object.
:ref:`Parent <no-21732>`                    The containing object. (obj)
:ref:`Position <no-21733>`                  The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-21734>`         Reference to the Preference Management object  (dPref)
:ref:`RegID <no-21735>`                     A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-21736>`                     The position of the right side of the object. This is a
:ref:`Size <no-21737>`                      The size of the object. (tuple)
:ref:`Sizer <no-21738>`                     The sizer for the object.
:ref:`StatusText <no-21739>`                Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-21740>`                   Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-21741>`                       A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-21742>`               Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-21743>`                       The top position of the object. (int)
:ref:`Transparency <no-21744>`              Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-21745>`         Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Value <no-21746>`                     The current Date of the calendar  (datetime.date)
:ref:`Visible <no-21747>`                   Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-21748>`           Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-21749>`                     The width of the object. (int)
:ref:`WindowHandle <no-21750>`              The platform-specific handle for the window. Read-only. (long)

=========================================== ========================


Properties - inherited
========================

.. _no-21642:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21643:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21644:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21645:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21646:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21647:

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

.. _no-21648:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21649:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21650:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-21651:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21652:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-21653:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21654:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21655:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21656:

**Date** 

The current Date of the calendar  (datetime.date)


Inherited from: 'wx.calendar.CalendarCtrl - can not provide a link

-------

.. _no-21657:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21658:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21659:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21660:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21661:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21662:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21663:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21664:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21665:

**DynamicDate** 

Dynamically determine the value of the Date property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Date property. If DynamicDate is set to None (the default), Date
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21666:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21667:

**DynamicFirstDayOfWeek** 

Dynamically determine the value of the FirstDayOfWeek property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FirstDayOfWeek property. If DynamicFirstDayOfWeek is set to None (the default), FirstDayOfWeek
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21668:

**DynamicFixedMonth** 

Dynamically determine the value of the FixedMonth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FixedMonth property. If DynamicFixedMonth is set to None (the default), FixedMonth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21669:

**DynamicFixedYear** 

Dynamically determine the value of the FixedYear property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FixedYear property. If DynamicFixedYear is set to None (the default), FixedYear
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21670:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21671:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21672:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21673:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21674:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21675:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21676:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21677:

**DynamicHeaderBackColor** 

Dynamically determine the value of the HeaderBackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HeaderBackColor property. If DynamicHeaderBackColor is set to None (the default), HeaderBackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21678:

**DynamicHeaderForeColor** 

Dynamically determine the value of the HeaderForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HeaderForeColor property. If DynamicHeaderForeColor is set to None (the default), HeaderForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21679:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21680:

**DynamicHighlightBackColor** 

Dynamically determine the value of the HighlightBackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HighlightBackColor property. If DynamicHighlightBackColor is set to None (the default), HighlightBackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21681:

**DynamicHighlightForeColor** 

Dynamically determine the value of the HighlightForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HighlightForeColor property. If DynamicHighlightForeColor is set to None (the default), HighlightForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21682:

**DynamicHighlightHolidays** 

Dynamically determine the value of the HighlightHolidays property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HighlightHolidays property. If DynamicHighlightHolidays is set to None (the default), HighlightHolidays
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21683:

**DynamicHolidayBackColor** 

Dynamically determine the value of the HolidayBackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HolidayBackColor property. If DynamicHolidayBackColor is set to None (the default), HolidayBackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21684:

**DynamicHolidayForeColor** 

Dynamically determine the value of the HolidayForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HolidayForeColor property. If DynamicHolidayForeColor is set to None (the default), HolidayForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21685:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21686:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21687:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21688:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21689:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21690:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21691:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21692:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21693:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21694:

**DynamicValue** 

Dynamically determine the value of the Date property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Date property. If DynamicDate is set to None (the default), Date
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21695:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21696:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21697:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-21698:

**FirstDayOfWeek** 

Can be one of either 'Sunday' or 'Monday'. Determines which day
    of the week appears in the first column. Defaults to the value set
    in dabo.firstDayOfWeek. Read-only at runtime.  (str)


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21699:

**FixedMonth** 

When True, the user cannot change the displayed month.
    Default=False  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21700:

**FixedYear** 

When True, the user cannot change the displayed month.
    Default=False  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21701:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-21702:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21703:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21704:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21705:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21706:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21707:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21708:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21709:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21710:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-21711:

**HeaderBackColor** 

Background color of the calendar header  (str or tuple)


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21712:

**HeaderForeColor** 

Forecolor of the calendar header  (str or tuple)


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21713:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21714:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21715:

**HighlightBackColor** 

Background color of the calendar highlight  (str or tuple)


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21716:

**HighlightForeColor** 

Forecolor of the calendar highlight  (str or tuple)


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21717:

**HighlightHolidays** 

Determines whether holidays are displayed as highlighted.
    Default=False.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21718:

**HolidayBackColor** 

Background color of the calendar holiday  (str or tuple)


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21719:

**HolidayForeColor** 

Forecolor of the calendar holiday  (str or tuple)


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21720:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21721:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21722:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21723:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21724:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21725:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21726:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21727:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21728:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21729:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21730:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-21731:

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

.. _no-21732:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-21733:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-21734:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21735:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21736:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-21737:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-21738:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-21739:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21740:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-21741:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21742:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21743:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21744:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21745:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21746:

**Value** 

The current Date of the calendar  (datetime.date)


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21747:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21748:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21749:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21750:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-21751>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-21752>`                 Occurs after the control or form is created.
:ref:`Destroy <no-21753>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-21754>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-21755>`               Occurs when the control gets the focus.
:ref:`Idle <no-21756>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-21757>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-21758>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-21759>`               
:ref:`KeyUp <no-21760>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-21761>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-21762>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-21763>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-21764>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-21765>`             
:ref:`MouseLeave <no-21766>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-21767>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-21768>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-21769>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-21770>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-21771>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-21772>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-21773>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-21774>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-21775>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-21776>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-21777>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-21778>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-21779>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-21780>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-21781>`                   Occurs when the control's position changes.
:ref:`Paint <no-21782>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-21783>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-21784>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-21785>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-21786>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-21751:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-21752:

**Create** 

Occurs after the control or form is created.



-------

.. _no-21753:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-21754:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-21755:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-21756:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-21757:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-21758:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-21759:

**KeyEvent** 



-------

.. _no-21760:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-21761:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-21762:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-21763:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-21764:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-21765:

**MouseEvent** 



-------

.. _no-21766:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-21767:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-21768:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-21769:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-21770:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-21771:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-21772:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-21773:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-21774:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-21775:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-21776:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-21777:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-21778:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-21779:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-21780:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-21781:

**Move** 

Occurs when the control's position changes.



-------

.. _no-21782:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-21783:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-21784:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-21785:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-21786:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-21787>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-21788>`             Instantiate object as a child of self.
:ref:`afterInit <no-21789>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-21790>`          
:ref:`afterSetProperties <no-21791>`    
:ref:`autoBindEvents <no-21792>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-21793>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-21794>`   
:ref:`bindEvent <no-21795>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-21796>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-21797>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-21798>`          Makes this object topmost
:ref:`clear <no-21799>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-21800>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-21801>`  Given a position relative to this control, return a position relative
:ref:`copy <no-21802>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-21803>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-21804>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-21805>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-21806>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-21807>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-21808>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-21809>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-21810>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-21811>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-21812>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-21813>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-21814>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-21815>`              Draws text on the object at the specified position
:ref:`endHover <no-21816>`              
:ref:`fitToSizer <no-21817>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-21818>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-21819>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-21820>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-21821>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-21822>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-21823>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-21824>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-21825>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-21826>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-21827>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-21828>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-21829>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-21830>`         Returns a dict containing the object's sizer property info. The
:ref:`goDays <no-21831>`                
:ref:`goMonths <no-21832>`              
:ref:`hide <no-21833>`                  Make the object invisible.
:ref:`initEvents <no-21834>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-21835>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-21836>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-21837>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-21838>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-21839>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-21840>`    Moves this object's tab order before the passed obj.
:ref:`nextDay <no-21841>`               
:ref:`objectCoordinates <no-21842>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-21843>`               
:ref:`paste <no-21844>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-21845>`           
:ref:`priorDay <no-21846>`              
:ref:`processDroppedFiles <no-21847>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-21848>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-21849>`            Raise the passed Dabo event.
:ref:`reCreate <no-21850>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-21851>`              Recreate the object.
:ref:`redraw <no-21852>`                Called when the object is (re)drawn.
:ref:`refresh <no-21853>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-21854>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-21855>`               Destroys the object.
:ref:`removeDrawnObject <no-21856>`     
:ref:`sendToBack <no-21857>`            Places this object behind all others.
:ref:`setAll <no-21858>`                Set all child object properties to the passed value.
:ref:`setFocus <no-21859>`              Sets focus to the object.
:ref:`setHoliday <no-21860>`            Adds the specified date to the list of holidays. This should be
:ref:`setHolidays <no-21861>`           
:ref:`setPositionInSizer <no-21862>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-21863>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-21864>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-21865>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-21866>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-21867>`                  Make the object visible.
:ref:`showContainingPage <no-21868>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-21869>`       Display a context menu (popup) at the specified position.
:ref:`super <no-21870>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-21871>`           Remove a previously registered event binding.
:ref:`unbindKey <no-21872>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-21873>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-21874>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-21875>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods - inherited
=====================

.. _no-21787:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21788:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-21789:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21790:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21791:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21792:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.autoBindEvents(self, force=True)
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

.. _no-21793:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21794:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21795:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-21796:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-21797:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-21798:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21799:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21800:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21801:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21802:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21803:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21804:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21805:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21806:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-21807:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21808:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21809:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21810:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21811:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21812:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21813:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21814:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21815:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21816:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21817:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21818:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-21819:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-21820:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-21821:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21822:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21823:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21824:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21825:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21826:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21827:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21828:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-21829:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21830:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21831:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.goDays(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21832:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.goMonths(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21833:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21834:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21835:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21836:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21837:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-21838:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.lockDisplay(self)
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

.. _no-21839:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21840:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21841:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.nextDay(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21842:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21843:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21844:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21845:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21846:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.priorDay(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21847:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21848:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21849:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21850:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-21851:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21852:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21853:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21854:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21855:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21856:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21857:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21858:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-21859:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21860:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.setHoliday(self, val)
   :noindex:


   
   Adds the specified date to the list of holidays. This should be
   a tuple in the format (Y, M, D). If this is a holiday that is to apply
   to every year, pass the year as None (e.g.: (None, 12, 25)
   


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21861:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.setHolidays(self, dtList)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21862:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21863:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-21864:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-21865:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21866:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21867:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21868:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21869:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21870:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21871:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-21872:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21873:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21874:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21875:

.. function:: dabo.ui.uiwx.dCalendar.dExtendedCalendar.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
