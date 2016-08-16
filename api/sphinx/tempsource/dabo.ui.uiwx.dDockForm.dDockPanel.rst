
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dDockForm

.. _dabo.ui.uiwx.dDockForm.dDockPanel:

=============================================
|doc_title|  **dDockForm.dDockPanel** - class
=============================================



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dDockPanel**

.. inheritance-diagram:: dDockPanel


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dPanel.dPanel`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dDockForm.dDockPanel

   .. automethod:: dabo.ui.uiwx.dDockForm.dDockPanel.__init__

|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-16419>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-16420>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-16421>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-16422>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-16423>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-16424>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-16425>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-16426>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-16427>`                 Position in pixels of the bottom side of the panel. Read-only when docked; read-write when floating
:ref:`BottomDockable <no-16428>`         Can the panel be docked to the bottom edge of the form? Default=True  (bool)
:ref:`Caption <no-16429>`                Text that appears in the title bar  (str)
:ref:`Children <no-16430>`               Returns a list of object references to the children of
:ref:`Class <no-16431>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-16432>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-16433>`   Reference to the sizer item that control's this control's layout.
:ref:`DestroyOnClose <no-16434>`         When the panel's Close button is clicked, does the panel get destroyed (True) or just hidden (False,
:ref:`DockSide <no-16435>`               Side of the form that the panel is either currently docked to,
:ref:`Dockable <no-16436>`               Can the panel be docked to the form? Default=True  (bool)
:ref:`Docked <no-16437>`                 Determines whether the pane is floating (False) or docked (True)  (bool)
:ref:`DroppedFileHandler <no-16438>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-16439>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-16440>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-16441>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-16442>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-16443>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-16444>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-16445>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-16446>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-16447>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-16448>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-16449>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-16450>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-16451>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-16452>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-16453>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-16454>`          Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-16455>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-16456>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-16457>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-16458>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-16459>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-16460>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-16461>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-16462>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-16463>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-16464>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-16465>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-16466>`                Specifies whether the object and children can get user input. (bool)
:ref:`Floatable <no-16467>`              Can the panel be undocked from the form and float independently? Default=True  (bool)
:ref:`Floating <no-16468>`               Determines whether the pane is floating (True) or docked (False)  (bool)
:ref:`FloatingBottom <no-16469>`         Bottom coordinate of the panel when floating  (int)
:ref:`FloatingHeight <no-16470>`         Height of the panel when floating  (int)
:ref:`FloatingLeft <no-16471>`           Left coordinate of the panel when floating  (int)
:ref:`FloatingPosition <no-16472>`       Position of the panel when floating  (2-tuple of ints)
:ref:`FloatingRight <no-16473>`          Right coordinate of the panel when floating  (int)
:ref:`FloatingSize <no-16474>`           Size of the panel when floating  (2-tuple of ints)
:ref:`FloatingTop <no-16475>`            Top coordinate of the panel when floating  (int)
:ref:`FloatingWidth <no-16476>`          Width of the panel when floating  (int)
:ref:`Font <no-16477>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-16478>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-16479>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-16480>`               Specifies the font face. (str)
:ref:`FontInfo <no-16481>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-16482>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-16483>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-16484>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-16485>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-16486>`                   Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`GripperPosition <no-16487>`        If a gripper is shown, is it on the Top or Left side? Default = 'Left'  ('Top' or 'Left')
:ref:`Height <no-16488>`                 Position in pixels of the height of the panel. Read-only when docked; read-write when floating  (int
:ref:`HelpContextText <no-16489>`        Specifies the context-sensitive help text associated with this
:ref:`Hover <no-16490>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-16491>`                   Position in pixels of the left side of the panel. Read-only when docked; read-write when floating  (
:ref:`LeftDockable <no-16492>`           Can the panel be docked to the left edge of the form? Default=True  (bool)
:ref:`LogEvents <no-16493>`              Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-16494>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-16495>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-16496>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-16497>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-16498>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-16499>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-16500>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Movable <no-16501>`                Can the panel be moved (True, default), or is it in a fixed position (False).  (bool)
:ref:`Name <no-16502>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-16503>`               Specifies the base name of the object.
:ref:`Parent <no-16504>`                 The containing object. (obj)
:ref:`Position <no-16505>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-16506>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-16507>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Resizable <no-16508>`              Can the panel be resized? Default=True  (bool)
:ref:`Right <no-16509>`                  Position in pixels of the right side of the panel. Read-only when docked; read-write when floating
:ref:`RightDockable <no-16510>`          Can the panel be docked to the right edge of the form? Default=True  (bool)
:ref:`ShowBorder <no-16511>`             Should the panel's border be shown when floating?  (bool)
:ref:`ShowCaption <no-16512>`            Should the panel's Caption be shown when it is docked? Default=True  (bool)
:ref:`ShowCloseButton <no-16513>`        Does the panel display a close button when floating? Default=True  (bool)
:ref:`ShowGripper <no-16514>`            Does the panel display a draggable gripper? Default=False  (bool)
:ref:`ShowMaximizeButton <no-16515>`     Does the panel display a maximize button when floating? Default=False  (bool)
:ref:`ShowMinimizeButton <no-16516>`     Does the panel display a minimize button when floating? Default=False  (bool)
:ref:`ShowPinButton <no-16517>`          Does the panel display a pin button when floating? Default=False  (bool)
:ref:`Size <no-16518>`                   The size of the object. (tuple)
:ref:`Sizer <no-16519>`                  The sizer for the object.
:ref:`StatusText <no-16520>`             Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-16521>`                Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-16522>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-16523>`            Specifies the tooltip text associated with this window. (str)
:ref:`Toolbar <no-16524>`                Returns True if this is a Toolbar pane. Default=False  (bool)
:ref:`Top <no-16525>`                    Position in pixels of the top side of the panel. Read-only when docked; read-write when floating  (i
:ref:`TopDockable <no-16526>`            Can the panel be docked to the top edge of the form? Default=True  (bool)
:ref:`Transparency <no-16527>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-16528>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-16529>`                Is the panel shown?  (bool)
:ref:`VisibleOnScreen <no-16530>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-16531>`                  Position in pixels of the width of the panel. Read-only when docked; read-write when floating  (int)
:ref:`WindowHandle <no-16532>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties
==========

.. _no-16428:

**BottomDockable** 

Can the panel be docked to the bottom edge of the form? Default=True  (bool)



-------

.. _no-16434:

**DestroyOnClose** 

When the panel's Close button is clicked, does the panel get destroyed (True) or just hidden (False, default)  (bool)



-------

.. _no-16435:

**DockSide** 

Side of the form that the panel is either currently docked to,
    or would be if dock() were to be called. Possible values are
    'Left', 'Right', 'Top' and 'Bottom'.  (str)



-------

.. _no-16436:

**Dockable** 

Can the panel be docked to the form? Default=True  (bool)



-------

.. _no-16437:

**Docked** 

Determines whether the pane is floating (False) or docked (True)  (bool)



-------

.. _no-16467:

**Floatable** 

Can the panel be undocked from the form and float independently? Default=True  (bool)



-------

.. _no-16468:

**Floating** 

Determines whether the pane is floating (True) or docked (False)  (bool)



-------

.. _no-16469:

**FloatingBottom** 

Bottom coordinate of the panel when floating  (int)



-------

.. _no-16470:

**FloatingHeight** 

Height of the panel when floating  (int)



-------

.. _no-16471:

**FloatingLeft** 

Left coordinate of the panel when floating  (int)



-------

.. _no-16472:

**FloatingPosition** 

Position of the panel when floating  (2-tuple of ints)



-------

.. _no-16473:

**FloatingRight** 

Right coordinate of the panel when floating  (int)



-------

.. _no-16474:

**FloatingSize** 

Size of the panel when floating  (2-tuple of ints)



-------

.. _no-16475:

**FloatingTop** 

Top coordinate of the panel when floating  (int)



-------

.. _no-16476:

**FloatingWidth** 

Width of the panel when floating  (int)



-------

.. _no-16487:

**GripperPosition** 

If a gripper is shown, is it on the Top or Left side? Default = 'Left'  ('Top' or 'Left')



-------

.. _no-16492:

**LeftDockable** 

Can the panel be docked to the left edge of the form? Default=True  (bool)



-------

.. _no-16501:

**Movable** 

Can the panel be moved (True, default), or is it in a fixed position (False).  (bool)



-------

.. _no-16508:

**Resizable** 

Can the panel be resized? Default=True  (bool)



-------

.. _no-16510:

**RightDockable** 

Can the panel be docked to the right edge of the form? Default=True  (bool)



-------

.. _no-16511:

**ShowBorder** 

Should the panel's border be shown when floating?  (bool)



-------

.. _no-16512:

**ShowCaption** 

Should the panel's Caption be shown when it is docked? Default=True  (bool)



-------

.. _no-16513:

**ShowCloseButton** 

Does the panel display a close button when floating? Default=True  (bool)



-------

.. _no-16514:

**ShowGripper** 

Does the panel display a draggable gripper? Default=False  (bool)



-------

.. _no-16515:

**ShowMaximizeButton** 

Does the panel display a maximize button when floating? Default=False  (bool)



-------

.. _no-16516:

**ShowMinimizeButton** 

Does the panel display a minimize button when floating? Default=False  (bool)



-------

.. _no-16517:

**ShowPinButton** 

Does the panel display a pin button when floating? Default=False  (bool)



-------

.. _no-16524:

**Toolbar** 

Returns True if this is a Toolbar pane. Default=False  (bool)



-------

.. _no-16526:

**TopDockable** 

Can the panel be docked to the top edge of the form? Default=True  (bool)



-------


Properties - inherited
========================

.. _no-16419:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16420:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16421:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16422:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16423:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16424:

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

.. _no-16425:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16426:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16427:

**Bottom** 

Position in pixels of the bottom side of the panel. Read-only when docked; read-write when floating  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-16429:

**Caption** 

Text that appears in the title bar  (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16430:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-16431:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16432:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16433:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16438:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16439:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16440:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16441:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16442:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16443:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16444:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16445:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16446:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16447:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16448:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16449:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16450:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16451:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16452:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16453:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16454:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16455:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16456:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16457:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16458:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16459:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16460:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16461:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16462:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16463:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16464:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16465:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16466:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-16477:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-16478:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16479:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16480:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16481:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16482:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16483:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16484:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16485:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16486:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-16488:

**Height** 

Position in pixels of the height of the panel. Read-only when docked; read-write when floating  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16489:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16490:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16491:

**Left** 

Position in pixels of the left side of the panel. Read-only when docked; read-write when floating  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16493:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16494:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16495:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16496:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16497:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16498:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16499:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16500:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16502:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-16503:

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

.. _no-16504:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-16505:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-16506:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16507:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16509:

**Right** 

Position in pixels of the right side of the panel. Read-only when docked; read-write when floating  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-16518:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-16519:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-16520:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16521:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-16522:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16523:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16525:

**Top** 

Position in pixels of the top side of the panel. Read-only when docked; read-write when floating  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16527:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16528:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16529:

**Visible** 

Is the panel shown?  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16530:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16531:

**Width** 

Position in pixels of the width of the panel. Read-only when docked; read-write when floating  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16532:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-16533>`       Occurs when a window background has been erased and needs repainting.
:ref:`ChildBorn <no-16534>`              Occurs when a child control is created.
:ref:`Create <no-16535>`                 Occurs after the control or form is created.
:ref:`Destroy <no-16536>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-16537>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-16538>`               Occurs when the control gets the focus.
:ref:`Idle <no-16539>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-16540>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-16541>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-16542>`               
:ref:`KeyUp <no-16543>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-16544>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-16545>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-16546>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-16547>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-16548>`             
:ref:`MouseLeave <no-16549>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-16550>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-16551>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-16552>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-16553>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-16554>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-16555>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-16556>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-16557>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-16558>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-16559>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-16560>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-16561>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-16562>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-16563>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-16564>`                   Occurs when the control's position changes.
:ref:`Paint <no-16565>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-16566>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-16567>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-16568>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-16569>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-16533:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-16534:

**ChildBorn** 

Occurs when a child control is created.



-------

.. _no-16535:

**Create** 

Occurs after the control or form is created.



-------

.. _no-16536:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-16537:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-16538:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-16539:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-16540:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-16541:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-16542:

**KeyEvent** 



-------

.. _no-16543:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-16544:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-16545:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-16546:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-16547:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-16548:

**MouseEvent** 



-------

.. _no-16549:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-16550:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-16551:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-16552:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-16553:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-16554:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-16555:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-16556:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-16557:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-16558:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-16559:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-16560:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-16561:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-16562:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-16563:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-16564:

**Move** 

Occurs when the control's position changes.



-------

.. _no-16565:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-16566:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-16567:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-16568:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-16569:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-16570>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-16571>`             Instantiate object as a child of self.
:ref:`afterInit <no-16572>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-16573>`          
:ref:`afterSetProperties <no-16574>`    
:ref:`autoBindEvents <no-16575>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-16576>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-16577>`   
:ref:`bindEvent <no-16578>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-16579>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-16580>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-16581>`          Makes this object topmost
:ref:`clear <no-16582>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-16583>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-16584>`  Given a position relative to this control, return a position relative
:ref:`copy <no-16585>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-16586>`                   Called by uiApp when the user requests a cut operation.
:ref:`dock <no-16587>`                  Dock the panel. If side is specified, it is docked on that side of the
:ref:`drawArc <no-16588>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-16589>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-16590>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-16591>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-16592>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-16593>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-16594>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-16595>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-16596>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-16597>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-16598>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-16599>`              Draws text on the object at the specified position
:ref:`endHover <no-16600>`              
:ref:`fitToSizer <no-16601>`            Resize the control to fit the size required by its sizer.
:ref:`float <no-16602>`                 Float the panel if it isn't already floating.
:ref:`fontZoomIn <no-16603>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-16604>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-16605>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-16606>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-16607>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-16608>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-16609>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-16610>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-16611>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-16612>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-16613>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-16614>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-16615>`         Returns a dict containing the object's sizer property info. The
:ref:`getState <no-16616>`              Returns the local name and a string that can be used to restore the state of this pane.
:ref:`hide <no-16617>`                  Make the object invisible.
:ref:`initEvents <no-16618>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-16619>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-16620>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-16621>`           Call the given function on this object and all of its Children. If
:ref:`layout <no-16622>`                Wrap the wx version of the call, if possible.
:ref:`lockDisplay <no-16623>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-16624>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-16625>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-16626>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-16627>`               
:ref:`paste <no-16628>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-16629>`           
:ref:`processDroppedFiles <no-16630>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-16631>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-16632>`            Raise the passed Dabo event.
:ref:`reCreate <no-16633>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-16634>`              Recreate the object.
:ref:`redraw <no-16635>`                Called when the object is (re)drawn.
:ref:`refresh <no-16636>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-16637>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-16638>`               Destroys the object.
:ref:`removeDrawnObject <no-16639>`     
:ref:`sendToBack <no-16640>`            Places this object behind all others.
:ref:`setAll <no-16641>`                Set all child object properties to the passed value.
:ref:`setFocus <no-16642>`              Sets focus to the object.
:ref:`setPositionInSizer <no-16643>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-16644>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-16645>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-16646>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-16647>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-16648>`                  Make the object visible.
:ref:`showContainingPage <no-16649>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-16650>`       Display a context menu (popup) at the specified position.
:ref:`super <no-16651>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-16652>`           Remove a previously registered event binding.
:ref:`unbindKey <no-16653>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-16654>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-16655>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-16656>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods
=======

.. _no-16587:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.dock(self, side=None)

   
   Dock the panel. If side is specified, it is docked on that side of the
   form. If no side is specified, it is docked in its default location.
   



-------

.. _no-16602:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.float(self)

   Float the panel if it isn't already floating.



-------

.. _no-16616:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.getState(self)

   Returns the local name and a string that can be used to restore the state of this pane.



-------


Methods - inherited
=====================

.. _no-16570:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16571:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-16572:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16573:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16574:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16575:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.autoBindEvents(self, force=True)
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

.. _no-16576:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16577:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16578:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-16579:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-16580:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-16581:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16582:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16583:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16584:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16585:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16586:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16588:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16589:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16590:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-16591:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16592:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16593:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16594:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16595:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16596:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16597:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16598:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16599:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16600:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16601:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16603:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-16604:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-16605:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-16606:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16607:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16608:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16609:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16610:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16611:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16612:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16613:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-16614:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16615:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16617:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16618:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16619:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16620:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16621:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-16622:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.layout(self, resetMin=False)
   :noindex:


   Wrap the wx version of the call, if possible.


Inherited from: 'dabo.ui.uiwx.dPanel._BasePanelMixin - can not provide a link

-------

.. _no-16623:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.lockDisplay(self)
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

.. _no-16624:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16625:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16626:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16627:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16628:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16629:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16630:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16631:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16632:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16633:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-16634:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16635:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16636:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16637:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16638:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16639:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16640:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16641:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-16642:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16643:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16644:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-16645:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-16646:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16647:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16648:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16649:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16650:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16651:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-16652:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-16653:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16654:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16655:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-16656:

.. function:: dabo.ui.uiwx.dDockForm.dDockPanel.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
