
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dCalendar

.. _dabo.ui.uiwx.dCalendar.dCalendar:

============================================
|doc_title|  **dCalendar.dCalendar** - class
============================================


This formats the calendar into a more compact layout, with
arrow buttons for moving back and forth a month at a time.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dCalendar**

.. inheritance-diagram:: dCalendar


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`



|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - .. image:: _static/macWidgets/dCalendar.png
          :scale: 75 %
          :target: _static/macWidgets/dCalendar.png
          :alt: dCalendar



     - .. image:: _static/winWidgets/dCalendar.png
          :scale: 75 %
          :target: _static/winWidgets/dCalendar.png
          :alt: dCalendar



     - .. image:: _static/nixWidgets/dCalendar.png
          :scale: 75 %
          :target: _static/nixWidgets/dCalendar.png
          :alt: dCalendar


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dCalendar.dCalendar

   .. automethod:: dabo.ui.uiwx.dCalendar.dCalendar.__init__

|method_summary| Properties Summary
===================================


=========================================== ========================
:ref:`Application <no-21402>`               Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-21403>`                 Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-21404>`                 The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-21405>`               Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-21406>`               Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-21407>`           Style of line for the border drawn around the control.
:ref:`BorderStyle <no-21408>`               Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-21409>`               Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-21410>`                    The position of the bottom side of the object. This is a
:ref:`Caption <no-21411>`                   The caption of the object. (str)
:ref:`Children <no-21412>`                  Returns a list of object references to the children of
:ref:`Class <no-21413>`                     The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-21414>`          Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-21415>`      Reference to the sizer item that control's this control's layout.
:ref:`Date <no-21416>`                      The current Date of the calendar  (datetime.date)
:ref:`DroppedFileHandler <no-21417>`        Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-21418>`        Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-21419>`          Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-21420>`        Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-21421>`    Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-21422>`        Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-21423>`        Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-21424>`            Dynamically determine the value of the Caption property.
:ref:`DynamicDate <no-21425>`               Dynamically determine the value of the Date property.
:ref:`DynamicEnabled <no-21426>`            Dynamically determine the value of the Enabled property.
:ref:`DynamicFirstDayOfWeek <no-21427>`     Dynamically determine the value of the FirstDayOfWeek property.
:ref:`DynamicFixedMonth <no-21428>`         Dynamically determine the value of the FixedMonth property.
:ref:`DynamicFixedYear <no-21429>`          Dynamically determine the value of the FixedYear property.
:ref:`DynamicFont <no-21430>`               Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-21431>`           Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-21432>`           Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-21433>`         Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-21434>`           Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-21435>`      Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-21436>`          Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeaderBackColor <no-21437>`    Dynamically determine the value of the HeaderBackColor property.
:ref:`DynamicHeaderForeColor <no-21438>`    Dynamically determine the value of the HeaderForeColor property.
:ref:`DynamicHeight <no-21439>`             Dynamically determine the value of the Height property.
:ref:`DynamicHighlightBackColor <no-21440>` Dynamically determine the value of the HighlightBackColor property.
:ref:`DynamicHighlightForeColor <no-21441>` Dynamically determine the value of the HighlightForeColor property.
:ref:`DynamicHighlightHolidays <no-21442>`  Dynamically determine the value of the HighlightHolidays property.
:ref:`DynamicHolidayBackColor <no-21443>`   Dynamically determine the value of the HolidayBackColor property.
:ref:`DynamicHolidayForeColor <no-21444>`   Dynamically determine the value of the HolidayForeColor property.
:ref:`DynamicLeft <no-21445>`               Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-21446>`       Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-21447>`           Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-21448>`               Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-21449>`         Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-21450>`                Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-21451>`        Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-21452>`                Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-21453>`       Dynamically determine the value of the Transparency property.
:ref:`DynamicValue <no-21454>`              Dynamically determine the value of the Date property.
:ref:`DynamicVisible <no-21455>`            Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-21456>`              Dynamically determine the value of the Width property.
:ref:`Enabled <no-21457>`                   Specifies whether the object and children can get user input. (bool)
:ref:`FirstDayOfWeek <no-21458>`            Can be one of either 'Sunday' or 'Monday'. Determines which day
:ref:`FixedMonth <no-21459>`                When True, the user cannot change the displayed month.
:ref:`FixedYear <no-21460>`                 When True, the user cannot change the displayed month.
:ref:`Font <no-21461>`                      Specifies font object for this control. (dFont)
:ref:`FontBold <no-21462>`                  Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-21463>`           Human-readable description of the current font settings. (str)
:ref:`FontFace <no-21464>`                  Specifies the font face. (str)
:ref:`FontInfo <no-21465>`                  Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-21466>`                Specifies whether font is italicized. (bool)
:ref:`FontSize <no-21467>`                  Specifies the point size of the font. (int)
:ref:`FontUnderline <no-21468>`             Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-21469>`                 Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-21470>`                      Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`HeaderBackColor <no-21471>`           Background color of the calendar header  (str or tuple)
:ref:`HeaderForeColor <no-21472>`           Forecolor of the calendar header  (str or tuple)
:ref:`Height <no-21473>`                    Specifies the height of the object. (int)
:ref:`HelpContextText <no-21474>`           Specifies the context-sensitive help text associated with this
:ref:`HighlightBackColor <no-21475>`        Background color of the calendar highlight  (str or tuple)
:ref:`HighlightForeColor <no-21476>`        Forecolor of the calendar highlight  (str or tuple)
:ref:`HighlightHolidays <no-21477>`         Determines whether holidays are displayed as highlighted.
:ref:`HolidayBackColor <no-21478>`          Background color of the calendar holiday  (str or tuple)
:ref:`HolidayForeColor <no-21479>`          Forecolor of the calendar holiday  (str or tuple)
:ref:`Hover <no-21480>`                     When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-21481>`                      Specifies the left position of the object. (int)
:ref:`LogEvents <no-21482>`                 Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-21483>`             Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-21484>`               Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-21485>`              Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-21486>`             Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-21487>`               Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-21488>`              Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-21489>`              Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-21490>`                      Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-21491>`                  Specifies the base name of the object.
:ref:`Parent <no-21492>`                    The containing object. (obj)
:ref:`Position <no-21493>`                  The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-21494>`         Reference to the Preference Management object  (dPref)
:ref:`RegID <no-21495>`                     A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-21496>`                     The position of the right side of the object. This is a
:ref:`Size <no-21497>`                      The size of the object. (tuple)
:ref:`Sizer <no-21498>`                     The sizer for the object.
:ref:`StatusText <no-21499>`                Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-21500>`                   Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-21501>`                       A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-21502>`               Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-21503>`                       The top position of the object. (int)
:ref:`Transparency <no-21504>`              Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-21505>`         Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Value <no-21506>`                     The current Date of the calendar  (datetime.date)
:ref:`Visible <no-21507>`                   Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-21508>`           Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-21509>`                     The width of the object. (int)
:ref:`WindowHandle <no-21510>`              The platform-specific handle for the window. Read-only. (long)

=========================================== ========================


Properties - inherited
========================

.. _no-21402:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21403:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21404:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21405:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21406:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21407:

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

.. _no-21408:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21409:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21410:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-21411:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21412:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-21413:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21414:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21415:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21416:

**Date** 

The current Date of the calendar  (datetime.date)


Inherited from: 'wx.calendar.CalendarCtrl - can not provide a link

-------

.. _no-21417:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21418:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21419:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21420:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21421:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21422:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21423:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21424:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21425:

**DynamicDate** 

Dynamically determine the value of the Date property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Date property. If DynamicDate is set to None (the default), Date
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21426:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21427:

**DynamicFirstDayOfWeek** 

Dynamically determine the value of the FirstDayOfWeek property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FirstDayOfWeek property. If DynamicFirstDayOfWeek is set to None (the default), FirstDayOfWeek
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21428:

**DynamicFixedMonth** 

Dynamically determine the value of the FixedMonth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FixedMonth property. If DynamicFixedMonth is set to None (the default), FixedMonth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21429:

**DynamicFixedYear** 

Dynamically determine the value of the FixedYear property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FixedYear property. If DynamicFixedYear is set to None (the default), FixedYear
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21430:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21431:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21432:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21433:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21434:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21435:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21436:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21437:

**DynamicHeaderBackColor** 

Dynamically determine the value of the HeaderBackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HeaderBackColor property. If DynamicHeaderBackColor is set to None (the default), HeaderBackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21438:

**DynamicHeaderForeColor** 

Dynamically determine the value of the HeaderForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HeaderForeColor property. If DynamicHeaderForeColor is set to None (the default), HeaderForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21439:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21440:

**DynamicHighlightBackColor** 

Dynamically determine the value of the HighlightBackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HighlightBackColor property. If DynamicHighlightBackColor is set to None (the default), HighlightBackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21441:

**DynamicHighlightForeColor** 

Dynamically determine the value of the HighlightForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HighlightForeColor property. If DynamicHighlightForeColor is set to None (the default), HighlightForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21442:

**DynamicHighlightHolidays** 

Dynamically determine the value of the HighlightHolidays property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HighlightHolidays property. If DynamicHighlightHolidays is set to None (the default), HighlightHolidays
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21443:

**DynamicHolidayBackColor** 

Dynamically determine the value of the HolidayBackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HolidayBackColor property. If DynamicHolidayBackColor is set to None (the default), HolidayBackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21444:

**DynamicHolidayForeColor** 

Dynamically determine the value of the HolidayForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
HolidayForeColor property. If DynamicHolidayForeColor is set to None (the default), HolidayForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21445:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21446:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21447:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21448:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21449:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21450:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21451:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21452:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21453:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21454:

**DynamicValue** 

Dynamically determine the value of the Date property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Date property. If DynamicDate is set to None (the default), Date
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21455:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21456:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21457:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-21458:

**FirstDayOfWeek** 

Can be one of either 'Sunday' or 'Monday'. Determines which day
    of the week appears in the first column. Defaults to the value set
    in dabo.firstDayOfWeek. Read-only at runtime.  (str)


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21459:

**FixedMonth** 

When True, the user cannot change the displayed month.
    Default=False  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21460:

**FixedYear** 

When True, the user cannot change the displayed month.
    Default=False  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21461:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-21462:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21463:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21464:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21465:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21466:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21467:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21468:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21469:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21470:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-21471:

**HeaderBackColor** 

Background color of the calendar header  (str or tuple)


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21472:

**HeaderForeColor** 

Forecolor of the calendar header  (str or tuple)


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21473:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21474:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21475:

**HighlightBackColor** 

Background color of the calendar highlight  (str or tuple)


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21476:

**HighlightForeColor** 

Forecolor of the calendar highlight  (str or tuple)


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21477:

**HighlightHolidays** 

Determines whether holidays are displayed as highlighted.
    Default=False.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21478:

**HolidayBackColor** 

Background color of the calendar holiday  (str or tuple)


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21479:

**HolidayForeColor** 

Forecolor of the calendar holiday  (str or tuple)


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21480:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21481:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21482:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21483:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21484:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21485:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21486:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21487:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21488:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21489:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21490:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-21491:

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

.. _no-21492:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-21493:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-21494:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21495:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21496:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-21497:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-21498:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-21499:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21500:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-21501:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21502:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21503:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21504:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21505:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21506:

**Value** 

The current Date of the calendar  (datetime.date)


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21507:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21508:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21509:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21510:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


========================================== ========================
:ref:`BackgroundErased <no-21511>`         Occurs when a window background has been erased and needs repainting.
:ref:`CalendarDateChanged <no-21512>`      Occurs when the date on a calendar is changed.
:ref:`CalendarDayChanged <no-21513>`       Occurs when the day of the month on a calendar is changed.
:ref:`CalendarDayHeaderClicked <no-21514>` Occurs when the day of week header is clicked.
:ref:`CalendarEvent <no-21515>`            
:ref:`CalendarMonthChanged <no-21516>`     Occurs when the month on a calendar is changed.
:ref:`CalendarYearChanged <no-21517>`      Occurs when the year on a calendar is changed.
:ref:`Create <no-21518>`                   Occurs after the control or form is created.
:ref:`Destroy <no-21519>`                  Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-21520>`    Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-21521>`                 Occurs when the control gets the focus.
:ref:`Idle <no-21522>`                     Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-21523>`                  Occurs when a key is depressed and released on the
:ref:`KeyDown <no-21524>`                  Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-21525>`                 
:ref:`KeyUp <no-21526>`                    Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-21527>`                Occurs when the control loses the focus.
:ref:`MenuClose <no-21528>`                Occurs when a menu has just been closed.
:ref:`MenuOpen <no-21529>`                 Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-21530>`               Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-21531>`               
:ref:`MouseLeave <no-21532>`               Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-21533>`           Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-21534>`     Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-21535>`            Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-21536>`              Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-21537>`         Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-21538>`   Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-21539>`          Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-21540>`            Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-21541>`                Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-21542>`          Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-21543>`    Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-21544>`           Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-21545>`             Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-21546>`               Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-21547>`                     Occurs when the control's position changes.
:ref:`Paint <no-21548>`                    Occurs when it is time to paint the control.
:ref:`Resize <no-21549>`                   Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-21550>`            Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-21551>`              Occurs when a drag operation ends in a tree.
:ref:`Update <no-21552>`                   Occurs when a container wants its controls to update

========================================== ========================


Events
=======

.. _no-21511:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-21512:

**CalendarDateChanged** 

Occurs when the date on a calendar is changed.



-------

.. _no-21513:

**CalendarDayChanged** 

Occurs when the day of the month on a calendar is changed.



-------

.. _no-21514:

**CalendarDayHeaderClicked** 

Occurs when the day of week header is clicked.



-------

.. _no-21515:

**CalendarEvent** 



-------

.. _no-21516:

**CalendarMonthChanged** 

Occurs when the month on a calendar is changed.



-------

.. _no-21517:

**CalendarYearChanged** 

Occurs when the year on a calendar is changed.



-------

.. _no-21518:

**Create** 

Occurs after the control or form is created.



-------

.. _no-21519:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-21520:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-21521:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-21522:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-21523:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-21524:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-21525:

**KeyEvent** 



-------

.. _no-21526:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-21527:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-21528:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-21529:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-21530:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-21531:

**MouseEvent** 



-------

.. _no-21532:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-21533:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-21534:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-21535:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-21536:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-21537:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-21538:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-21539:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-21540:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-21541:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-21542:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-21543:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-21544:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-21545:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-21546:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-21547:

**Move** 

Occurs when the control's position changes.



-------

.. _no-21548:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-21549:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-21550:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-21551:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-21552:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-21553>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-21554>`             Instantiate object as a child of self.
:ref:`afterInit <no-21555>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-21556>`          
:ref:`afterSetProperties <no-21557>`    
:ref:`autoBindEvents <no-21558>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-21559>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-21560>`   
:ref:`bindEvent <no-21561>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-21562>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-21563>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-21564>`          Makes this object topmost
:ref:`clear <no-21565>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-21566>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-21567>`  Given a position relative to this control, return a position relative
:ref:`copy <no-21568>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-21569>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-21570>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-21571>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-21572>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-21573>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-21574>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-21575>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-21576>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-21577>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-21578>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-21579>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-21580>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-21581>`              Draws text on the object at the specified position
:ref:`endHover <no-21582>`              
:ref:`fitToSizer <no-21583>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-21584>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-21585>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-21586>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-21587>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-21588>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-21589>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-21590>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-21591>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-21592>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-21593>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-21594>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-21595>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-21596>`         Returns a dict containing the object's sizer property info. The
:ref:`goDays <no-21597>`                
:ref:`goMonths <no-21598>`              
:ref:`hide <no-21599>`                  Make the object invisible.
:ref:`initEvents <no-21600>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-21601>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-21602>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-21603>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-21604>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-21605>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-21606>`    Moves this object's tab order before the passed obj.
:ref:`nextDay <no-21607>`               
:ref:`objectCoordinates <no-21608>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-21609>`               
:ref:`paste <no-21610>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-21611>`           
:ref:`priorDay <no-21612>`              
:ref:`processDroppedFiles <no-21613>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-21614>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-21615>`            Raise the passed Dabo event.
:ref:`reCreate <no-21616>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-21617>`              Recreate the object.
:ref:`redraw <no-21618>`                Called when the object is (re)drawn.
:ref:`refresh <no-21619>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-21620>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-21621>`               Destroys the object.
:ref:`removeDrawnObject <no-21622>`     
:ref:`sendToBack <no-21623>`            Places this object behind all others.
:ref:`setAll <no-21624>`                Set all child object properties to the passed value.
:ref:`setFocus <no-21625>`              Sets focus to the object.
:ref:`setHoliday <no-21626>`            Adds the specified date to the list of holidays. This should be
:ref:`setHolidays <no-21627>`           
:ref:`setPositionInSizer <no-21628>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-21629>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-21630>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-21631>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-21632>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-21633>`                  Make the object visible.
:ref:`showContainingPage <no-21634>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-21635>`       Display a context menu (popup) at the specified position.
:ref:`super <no-21636>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-21637>`           Remove a previously registered event binding.
:ref:`unbindKey <no-21638>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-21639>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-21640>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-21641>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods - inherited
=====================

.. _no-21553:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21554:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-21555:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21556:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21557:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21558:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.autoBindEvents(self, force=True)
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

.. _no-21559:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21560:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21561:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-21562:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-21563:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-21564:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21565:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21566:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21567:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21568:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21569:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21570:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21571:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21572:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-21573:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21574:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21575:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21576:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21577:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21578:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21579:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21580:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21581:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21582:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21583:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21584:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-21585:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-21586:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-21587:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21588:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21589:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21590:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21591:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21592:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21593:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21594:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-21595:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21596:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21597:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.goDays(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21598:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.goMonths(self, val)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21599:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21600:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21601:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21602:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21603:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-21604:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.lockDisplay(self)
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

.. _no-21605:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21606:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21607:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.nextDay(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21608:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21609:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21610:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21611:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21612:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.priorDay(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21613:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21614:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21615:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21616:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-21617:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21618:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21619:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21620:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21621:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21622:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21623:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21624:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-21625:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21626:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.setHoliday(self, val)
   :noindex:


   
   Adds the specified date to the list of holidays. This should be
   a tuple in the format (Y, M, D). If this is a holiday that is to apply
   to every year, pass the year as None (e.g.: (None, 12, 25)
   


Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21627:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.setHolidays(self, dtList)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dCalendar.BaseCalendar`

-------

.. _no-21628:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21629:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-21630:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-21631:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21632:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21633:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21634:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21635:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21636:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21637:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-21638:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21639:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21640:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21641:

.. function:: dabo.ui.uiwx.dCalendar.dCalendar.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
