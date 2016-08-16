
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dButton

.. _dabo.ui.uiwx.dButton.dButton:

========================================
|doc_title|  **dButton.dButton** - class
========================================


Creates a button that can be pressed by the user to trigger an action.

Example::

        class MyButton(dabo.ui.dButton):
            def initProperties(self):
                self.Caption = "Press Me"

            def onHit(self, evt):
                self.Caption = "Press Me one more time"





|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dButton**

.. inheritance-diagram:: dButton


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`



|subclasses| Known Subclasses
=============================

* :ref:`dabo.lib.EasyDialogBuilder.fileButton`



|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - .. image:: _static/macWidgets/dButton.png
          :scale: 75 %
          :target: _static/macWidgets/dButton.png
          :alt: dButton



     - .. image:: _static/winWidgets/dButton.png
          :scale: 75 %
          :target: _static/winWidgets/dButton.png
          :alt: dButton



     - .. image:: _static/nixWidgets/dButton.png
          :scale: 75 %
          :target: _static/nixWidgets/dButton.png
          :alt: dButton


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dButton.dButton

   .. automethod:: dabo.ui.uiwx.dButton.dButton.__init__

|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-15634>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-15635>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-15636>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-15637>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-15638>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-15639>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-15640>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-15641>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-15642>`                 The position of the bottom side of the object. This is a
:ref:`CancelButton <no-15643>`           Specifies whether this command button gets clicked on -Escape-.
:ref:`Caption <no-15644>`                The caption of the object. (str)
:ref:`Children <no-15645>`               Returns a list of object references to the children of
:ref:`Class <no-15646>`                  The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-15647>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-15648>`   Reference to the sizer item that control's this control's layout.
:ref:`DefaultButton <no-15649>`          Specifies whether this command button gets clicked on -Enter-.
:ref:`DroppedFileHandler <no-15650>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-15651>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-15652>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-15653>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-15654>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-15655>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-15656>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCancelButton <no-15657>`    Dynamically determine the value of the CancelButton property.
:ref:`DynamicCaption <no-15658>`         Dynamically determine the value of the Caption property.
:ref:`DynamicDefaultButton <no-15659>`   Dynamically determine the value of the DefaultButton property.
:ref:`DynamicEnabled <no-15660>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-15661>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-15662>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-15663>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-15664>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-15665>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-15666>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-15667>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-15668>`          Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-15669>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-15670>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-15671>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-15672>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-15673>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-15674>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-15675>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-15676>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-15677>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-15678>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-15679>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-15680>`                Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-15681>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-15682>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-15683>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-15684>`               Specifies the font face. (str)
:ref:`FontInfo <no-15685>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-15686>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-15687>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-15688>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-15689>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-15690>`                   Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-15691>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-15692>`        Specifies the context-sensitive help text associated with this
:ref:`Hover <no-15693>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-15694>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-15695>`              Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-15696>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-15697>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-15698>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-15699>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-15700>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-15701>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-15702>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-15703>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-15704>`               Specifies the base name of the object.
:ref:`Parent <no-15705>`                 The containing object. (obj)
:ref:`Position <no-15706>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-15707>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-15708>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-15709>`                  The position of the right side of the object. This is a
:ref:`Size <no-15710>`                   The size of the object. (tuple)
:ref:`Sizer <no-15711>`                  The sizer for the object.
:ref:`StatusText <no-15712>`             Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-15713>`                Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-15714>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-15715>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-15716>`                    The top position of the object. (int)
:ref:`Transparency <no-15717>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-15718>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-15719>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-15720>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-15721>`                  The width of the object. (int)
:ref:`WindowHandle <no-15722>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties
==========

.. _no-15643:

**CancelButton** 

Specifies whether this command button gets clicked on -Escape-.



-------

.. _no-15649:

**DefaultButton** 

Specifies whether this command button gets clicked on -Enter-.



-------

.. _no-15657:

**DynamicCancelButton** 

Dynamically determine the value of the CancelButton property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
CancelButton property. If DynamicCancelButton is set to None (the default), CancelButton
will not be dynamically evaluated.



-------

.. _no-15659:

**DynamicDefaultButton** 

Dynamically determine the value of the DefaultButton property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
DefaultButton property. If DynamicDefaultButton is set to None (the default), DefaultButton
will not be dynamically evaluated.



-------


Properties - inherited
========================

.. _no-15634:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15635:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15636:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15637:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15638:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15639:

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

.. _no-15640:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15641:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15642:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-15644:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15645:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-15646:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15647:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15648:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15650:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15651:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15652:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15653:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15654:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15655:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15656:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15658:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15660:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15661:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15662:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15663:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15664:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15665:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15666:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15667:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15668:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15669:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15670:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15671:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15672:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15673:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15674:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15675:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15676:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15677:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15678:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15679:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15680:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-15681:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-15682:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15683:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15684:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15685:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15686:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15687:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15688:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15689:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15690:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-15691:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15692:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15693:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15694:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15695:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15696:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15697:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15698:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15699:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15700:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15701:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15702:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15703:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-15704:

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

.. _no-15705:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-15706:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-15707:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15708:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15709:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-15710:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-15711:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-15712:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15713:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-15714:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15715:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15716:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15717:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15718:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15719:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15720:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15721:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15722:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-15723>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-15724>`                 Occurs after the control or form is created.
:ref:`Destroy <no-15725>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-15726>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-15727>`               Occurs when the control gets the focus.
:ref:`Hit <no-15728>`                    Occurs with the control's default event (button click,
:ref:`Idle <no-15729>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-15730>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-15731>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-15732>`               
:ref:`KeyUp <no-15733>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-15734>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-15735>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-15736>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-15737>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-15738>`             
:ref:`MouseLeave <no-15739>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-15740>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-15741>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-15742>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-15743>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-15744>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-15745>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-15746>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-15747>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-15748>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-15749>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-15750>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-15751>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-15752>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-15753>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-15754>`                   Occurs when the control's position changes.
:ref:`Paint <no-15755>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-15756>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-15757>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-15758>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-15759>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-15723:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-15724:

**Create** 

Occurs after the control or form is created.



-------

.. _no-15725:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-15726:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-15727:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-15728:

**Hit** 

Occurs with the control's default event (button click,
listbox pick, checkbox, etc.)




-------

.. _no-15729:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-15730:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-15731:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-15732:

**KeyEvent** 



-------

.. _no-15733:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-15734:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-15735:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-15736:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-15737:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-15738:

**MouseEvent** 



-------

.. _no-15739:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-15740:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-15741:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-15742:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-15743:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-15744:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-15745:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-15746:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-15747:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-15748:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-15749:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-15750:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-15751:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-15752:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-15753:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-15754:

**Move** 

Occurs when the control's position changes.



-------

.. _no-15755:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-15756:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-15757:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-15758:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-15759:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-15760>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-15761>`             Instantiate object as a child of self.
:ref:`afterInit <no-15762>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-15763>`          
:ref:`afterSetProperties <no-15764>`    
:ref:`autoBindEvents <no-15765>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-15766>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-15767>`   
:ref:`bindEvent <no-15768>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-15769>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-15770>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-15771>`          Makes this object topmost
:ref:`clear <no-15772>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-15773>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-15774>`  Given a position relative to this control, return a position relative
:ref:`copy <no-15775>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-15776>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-15777>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-15778>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-15779>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-15780>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-15781>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-15782>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-15783>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-15784>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-15785>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-15786>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-15787>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-15788>`              Draws text on the object at the specified position
:ref:`endHover <no-15789>`              
:ref:`fitToSizer <no-15790>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-15791>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-15792>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-15793>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-15794>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-15795>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-15796>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-15797>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-15798>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-15799>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-15800>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-15801>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-15802>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-15803>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-15804>`                  Make the object invisible.
:ref:`initEvents <no-15805>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-15806>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-15807>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-15808>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-15809>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-15810>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-15811>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-15812>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-15813>`               
:ref:`paste <no-15814>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-15815>`           
:ref:`processDroppedFiles <no-15816>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-15817>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-15818>`            Raise the passed Dabo event.
:ref:`reCreate <no-15819>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-15820>`              Recreate the object.
:ref:`redraw <no-15821>`                Called when the object is (re)drawn.
:ref:`refresh <no-15822>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-15823>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-15824>`               Destroys the object.
:ref:`removeDrawnObject <no-15825>`     
:ref:`sendToBack <no-15826>`            Places this object behind all others.
:ref:`setAll <no-15827>`                Set all child object properties to the passed value.
:ref:`setFocus <no-15828>`              Sets focus to the object.
:ref:`setPositionInSizer <no-15829>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-15830>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-15831>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-15832>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-15833>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-15834>`                  Make the object visible.
:ref:`showContainingPage <no-15835>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-15836>`       Display a context menu (popup) at the specified position.
:ref:`super <no-15837>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-15838>`           Remove a previously registered event binding.
:ref:`unbindKey <no-15839>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-15840>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-15841>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-15842>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods - inherited
=====================

.. _no-15760:

.. function:: dabo.ui.uiwx.dButton.dButton.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15761:

.. function:: dabo.ui.uiwx.dButton.dButton.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-15762:

.. function:: dabo.ui.uiwx.dButton.dButton.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15763:

.. function:: dabo.ui.uiwx.dButton.dButton.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15764:

.. function:: dabo.ui.uiwx.dButton.dButton.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15765:

.. function:: dabo.ui.uiwx.dButton.dButton.autoBindEvents(self, force=True)
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

.. _no-15766:

.. function:: dabo.ui.uiwx.dButton.dButton.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15767:

.. function:: dabo.ui.uiwx.dButton.dButton.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15768:

.. function:: dabo.ui.uiwx.dButton.dButton.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-15769:

.. function:: dabo.ui.uiwx.dButton.dButton.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-15770:

.. function:: dabo.ui.uiwx.dButton.dButton.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-15771:

.. function:: dabo.ui.uiwx.dButton.dButton.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15772:

.. function:: dabo.ui.uiwx.dButton.dButton.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15773:

.. function:: dabo.ui.uiwx.dButton.dButton.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15774:

.. function:: dabo.ui.uiwx.dButton.dButton.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15775:

.. function:: dabo.ui.uiwx.dButton.dButton.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15776:

.. function:: dabo.ui.uiwx.dButton.dButton.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15777:

.. function:: dabo.ui.uiwx.dButton.dButton.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15778:

.. function:: dabo.ui.uiwx.dButton.dButton.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15779:

.. function:: dabo.ui.uiwx.dButton.dButton.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-15780:

.. function:: dabo.ui.uiwx.dButton.dButton.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15781:

.. function:: dabo.ui.uiwx.dButton.dButton.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15782:

.. function:: dabo.ui.uiwx.dButton.dButton.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15783:

.. function:: dabo.ui.uiwx.dButton.dButton.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15784:

.. function:: dabo.ui.uiwx.dButton.dButton.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15785:

.. function:: dabo.ui.uiwx.dButton.dButton.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15786:

.. function:: dabo.ui.uiwx.dButton.dButton.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15787:

.. function:: dabo.ui.uiwx.dButton.dButton.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15788:

.. function:: dabo.ui.uiwx.dButton.dButton.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15789:

.. function:: dabo.ui.uiwx.dButton.dButton.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15790:

.. function:: dabo.ui.uiwx.dButton.dButton.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15791:

.. function:: dabo.ui.uiwx.dButton.dButton.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-15792:

.. function:: dabo.ui.uiwx.dButton.dButton.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-15793:

.. function:: dabo.ui.uiwx.dButton.dButton.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-15794:

.. function:: dabo.ui.uiwx.dButton.dButton.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15795:

.. function:: dabo.ui.uiwx.dButton.dButton.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15796:

.. function:: dabo.ui.uiwx.dButton.dButton.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15797:

.. function:: dabo.ui.uiwx.dButton.dButton.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15798:

.. function:: dabo.ui.uiwx.dButton.dButton.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15799:

.. function:: dabo.ui.uiwx.dButton.dButton.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15800:

.. function:: dabo.ui.uiwx.dButton.dButton.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15801:

.. function:: dabo.ui.uiwx.dButton.dButton.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-15802:

.. function:: dabo.ui.uiwx.dButton.dButton.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15803:

.. function:: dabo.ui.uiwx.dButton.dButton.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15804:

.. function:: dabo.ui.uiwx.dButton.dButton.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15805:

.. function:: dabo.ui.uiwx.dButton.dButton.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15806:

.. function:: dabo.ui.uiwx.dButton.dButton.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15807:

.. function:: dabo.ui.uiwx.dButton.dButton.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15808:

.. function:: dabo.ui.uiwx.dButton.dButton.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-15809:

.. function:: dabo.ui.uiwx.dButton.dButton.lockDisplay(self)
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

.. _no-15810:

.. function:: dabo.ui.uiwx.dButton.dButton.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15811:

.. function:: dabo.ui.uiwx.dButton.dButton.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15812:

.. function:: dabo.ui.uiwx.dButton.dButton.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15813:

.. function:: dabo.ui.uiwx.dButton.dButton.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15814:

.. function:: dabo.ui.uiwx.dButton.dButton.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15815:

.. function:: dabo.ui.uiwx.dButton.dButton.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15816:

.. function:: dabo.ui.uiwx.dButton.dButton.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15817:

.. function:: dabo.ui.uiwx.dButton.dButton.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15818:

.. function:: dabo.ui.uiwx.dButton.dButton.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15819:

.. function:: dabo.ui.uiwx.dButton.dButton.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-15820:

.. function:: dabo.ui.uiwx.dButton.dButton.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15821:

.. function:: dabo.ui.uiwx.dButton.dButton.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15822:

.. function:: dabo.ui.uiwx.dButton.dButton.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15823:

.. function:: dabo.ui.uiwx.dButton.dButton.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15824:

.. function:: dabo.ui.uiwx.dButton.dButton.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15825:

.. function:: dabo.ui.uiwx.dButton.dButton.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15826:

.. function:: dabo.ui.uiwx.dButton.dButton.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15827:

.. function:: dabo.ui.uiwx.dButton.dButton.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-15828:

.. function:: dabo.ui.uiwx.dButton.dButton.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15829:

.. function:: dabo.ui.uiwx.dButton.dButton.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15830:

.. function:: dabo.ui.uiwx.dButton.dButton.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-15831:

.. function:: dabo.ui.uiwx.dButton.dButton.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-15832:

.. function:: dabo.ui.uiwx.dButton.dButton.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15833:

.. function:: dabo.ui.uiwx.dButton.dButton.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15834:

.. function:: dabo.ui.uiwx.dButton.dButton.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15835:

.. function:: dabo.ui.uiwx.dButton.dButton.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15836:

.. function:: dabo.ui.uiwx.dButton.dButton.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15837:

.. function:: dabo.ui.uiwx.dButton.dButton.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-15838:

.. function:: dabo.ui.uiwx.dButton.dButton.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-15839:

.. function:: dabo.ui.uiwx.dButton.dButton.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15840:

.. function:: dabo.ui.uiwx.dButton.dButton.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15841:

.. function:: dabo.ui.uiwx.dButton.dButton.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-15842:

.. function:: dabo.ui.uiwx.dButton.dButton.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
