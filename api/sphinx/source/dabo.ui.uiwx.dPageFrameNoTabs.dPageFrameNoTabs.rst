
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dPageFrameNoTabs

.. _dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs:

==========================================================
|doc_title|  **dPageFrameNoTabs.dPageFrameNoTabs** - class
==========================================================


Creates a pageframe with no tabs or other way for the user to select a
page. Your code will have to programatically set the page.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dPageFrameNoTabs**

.. inheritance-diagram:: dPageFrameNoTabs


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dPanel.dPanel`



|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - no image available



     - .. image:: _static/winWidgets/dPageFrameNoTabs.png
          :scale: 75 %
          :target: _static/winWidgets/dPageFrameNoTabs.png
          :alt: dPageFrameNoTabs



     - .. image:: _static/nixWidgets/dPageFrameNoTabs.png
          :scale: 75 %
          :target: _static/nixWidgets/dPageFrameNoTabs.png
          :alt: dPageFrameNoTabs


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs

   .. automethod:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.__init__

|method_summary| Properties Summary
===================================


=========================================== ========================
:ref:`Application <no-20940>`               Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-20941>`                 Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-20942>`                 The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-20943>`               Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-20944>`               Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-20945>`           Style of line for the border drawn around the control.
:ref:`BorderStyle <no-20946>`               Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-20947>`               Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-20948>`                    The position of the bottom side of the object. This is a
:ref:`Caption <no-20949>`                   The caption of the object. (str)
:ref:`Children <no-20950>`                  Returns a list of object references to the children of
:ref:`Class <no-20951>`                     The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-20952>`          Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-20953>`      Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-20954>`        Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-20955>`        Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-20956>`          Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-20957>`        Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-20958>`    Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-20959>`        Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-20960>`        Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-20961>`            Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-20962>`            Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-20963>`               Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-20964>`           Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-20965>`           Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-20966>`         Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-20967>`           Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-20968>`      Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-20969>`          Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-20970>`             Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-20971>`               Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-20972>`       Dynamically determine the value of the MousePointer property.
:ref:`DynamicPageClass <no-20973>`          Dynamically determine the value of the PageClass property.
:ref:`DynamicPageCount <no-20974>`          Dynamically determine the value of the PageCount property.
:ref:`DynamicPosition <no-20975>`           Dynamically determine the value of the Position property.
:ref:`DynamicSelectedPage <no-20976>`       Dynamically determine the value of the SelectedPage property.
:ref:`DynamicSelectedPageNumber <no-20977>` Dynamically determine the value of the SelectedPageNumber property.
:ref:`DynamicSize <no-20978>`               Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-20979>`         Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-20980>`                Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-20981>`        Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-20982>`                Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-20983>`       Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-20984>`            Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-20985>`              Dynamically determine the value of the Width property.
:ref:`Enabled <no-20986>`                   Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-20987>`                      Specifies font object for this control. (dFont)
:ref:`FontBold <no-20988>`                  Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-20989>`           Human-readable description of the current font settings. (str)
:ref:`FontFace <no-20990>`                  Specifies the font face. (str)
:ref:`FontInfo <no-20991>`                  Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-20992>`                Specifies whether font is italicized. (bool)
:ref:`FontSize <no-20993>`                  Specifies the point size of the font. (int)
:ref:`FontUnderline <no-20994>`             Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-20995>`                 Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-20996>`                      Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-20997>`                    Specifies the height of the object. (int)
:ref:`HelpContextText <no-20998>`           Specifies the context-sensitive help text associated with this
:ref:`Hover <no-20999>`                     When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-21000>`                      Specifies the left position of the object. (int)
:ref:`LogEvents <no-21001>`                 Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-21002>`             Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-21003>`               Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-21004>`              Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-21005>`             Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-21006>`               Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-21007>`              Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-21008>`              Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-21009>`                      Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-21010>`                  Specifies the base name of the object.
:ref:`PageClass <no-21011>`                 The default class used when adding new pages.  (dPage)
:ref:`PageCount <no-21012>`                 Returns the number of pages in this pageframe  (int)
:ref:`PageSizerClass <no-21013>`            Default sizer class for pages added automatically to this control. Set
:ref:`Pages <no-21014>`                     List of all the pages.   (list)
:ref:`Parent <no-21015>`                    The containing object. (obj)
:ref:`Position <no-21016>`                  The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-21017>`         Reference to the Preference Management object  (dPref)
:ref:`RegID <no-21018>`                     A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-21019>`                     The position of the right side of the object. This is a
:ref:`SelectedPage <no-21020>`              Returns a reference to the currently displayed page  (dPage | dPanel)
:ref:`SelectedPageNumber <no-21021>`        Returns a reference to the index of the currently displayed page  (int)
:ref:`Size <no-21022>`                      The size of the object. (tuple)
:ref:`Sizer <no-21023>`                     The sizer for the object.
:ref:`StatusText <no-21024>`                Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-21025>`                   Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-21026>`                       A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-21027>`               Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-21028>`                       The top position of the object. (int)
:ref:`Transparency <no-21029>`              Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-21030>`         Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-21031>`                   Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-21032>`           Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-21033>`                     The width of the object. (int)
:ref:`WindowHandle <no-21034>`              The platform-specific handle for the window. Read-only. (long)

=========================================== ========================


Properties
==========

.. _no-20973:

**DynamicPageClass** 

Dynamically determine the value of the PageClass property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
PageClass property. If DynamicPageClass is set to None (the default), PageClass
will not be dynamically evaluated.



-------

.. _no-20974:

**DynamicPageCount** 

Dynamically determine the value of the PageCount property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
PageCount property. If DynamicPageCount is set to None (the default), PageCount
will not be dynamically evaluated.



-------

.. _no-20976:

**DynamicSelectedPage** 

Dynamically determine the value of the SelectedPage property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectedPage property. If DynamicSelectedPage is set to None (the default), SelectedPage
will not be dynamically evaluated.



-------

.. _no-20977:

**DynamicSelectedPageNumber** 

Dynamically determine the value of the SelectedPageNumber property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectedPageNumber property. If DynamicSelectedPageNumber is set to None (the default), SelectedPageNumber
will not be dynamically evaluated.



-------

.. _no-21011:

**PageClass** 

The default class used when adding new pages.  (dPage)



-------

.. _no-21012:

**PageCount** 

Returns the number of pages in this pageframe  (int)



-------

.. _no-21013:

**PageSizerClass** 

Default sizer class for pages added automatically to this control. Set
    this to None to prevent sizers from being automatically added to child
    pages. (dSizer or None)



-------

.. _no-21014:

**Pages** 

List of all the pages.   (list)



-------

.. _no-21020:

**SelectedPage** 

Returns a reference to the currently displayed page  (dPage | dPanel)



-------

.. _no-21021:

**SelectedPageNumber** 

Returns a reference to the index of the currently displayed page  (int)



-------


Properties - inherited
========================

.. _no-20940:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20941:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20942:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20943:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20944:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20945:

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

.. _no-20946:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20947:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20948:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-20949:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20950:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-20951:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-20952:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20953:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20954:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20955:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20956:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20957:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20958:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20959:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20960:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20961:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20962:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20963:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20964:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20965:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20966:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20967:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20968:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20969:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20970:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20971:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20972:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20975:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20978:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20979:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20980:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20981:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20982:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20983:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20984:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20985:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20986:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-20987:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-20988:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20989:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20990:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20991:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20992:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20993:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20994:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20995:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20996:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-20997:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20998:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-20999:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21000:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21001:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21002:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21003:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21004:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21005:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21006:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21007:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21008:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21009:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-21010:

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

.. _no-21015:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-21016:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-21017:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21018:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21019:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-21022:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-21023:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-21024:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21025:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-21026:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21027:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21028:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21029:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21030:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21031:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21032:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21033:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21034:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-21035>`       Occurs when a window background has been erased and needs repainting.
:ref:`ChildBorn <no-21036>`              Occurs when a child control is created.
:ref:`Create <no-21037>`                 Occurs after the control or form is created.
:ref:`Destroy <no-21038>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-21039>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-21040>`               Occurs when the control gets the focus.
:ref:`Idle <no-21041>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-21042>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-21043>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-21044>`               
:ref:`KeyUp <no-21045>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-21046>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-21047>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-21048>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-21049>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-21050>`             
:ref:`MouseLeave <no-21051>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-21052>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-21053>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-21054>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-21055>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-21056>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-21057>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-21058>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-21059>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-21060>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-21061>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-21062>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-21063>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-21064>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-21065>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-21066>`                   Occurs when the control's position changes.
:ref:`PageChanged <no-21067>`            Occurs when a page in a pageframe-like control changes
:ref:`PageChanging <no-21068>`           Occurs when the current page in a pageframe-like control is about to change
:ref:`Paint <no-21069>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-21070>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-21071>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-21072>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-21073>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-21035:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-21036:

**ChildBorn** 

Occurs when a child control is created.



-------

.. _no-21037:

**Create** 

Occurs after the control or form is created.



-------

.. _no-21038:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-21039:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-21040:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-21041:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-21042:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-21043:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-21044:

**KeyEvent** 



-------

.. _no-21045:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-21046:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-21047:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-21048:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-21049:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-21050:

**MouseEvent** 



-------

.. _no-21051:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-21052:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-21053:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-21054:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-21055:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-21056:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-21057:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-21058:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-21059:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-21060:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-21061:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-21062:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-21063:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-21064:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-21065:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-21066:

**Move** 

Occurs when the control's position changes.



-------

.. _no-21067:

**PageChanged** 

Occurs when a page in a pageframe-like control changes



-------

.. _no-21068:

**PageChanging** 

Occurs when the current page in a pageframe-like control is about to change



-------

.. _no-21069:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-21070:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-21071:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-21072:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-21073:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-21074>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-21075>`             Instantiate object as a child of self.
:ref:`afterInit <no-21076>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-21077>`          
:ref:`afterSetProperties <no-21078>`    
:ref:`appendPage <no-21079>`            Creates a new page, which should be a subclass of dPage. If makeActive
:ref:`autoBindEvents <no-21080>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-21081>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-21082>`   
:ref:`bindEvent <no-21083>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-21084>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-21085>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-21086>`          Makes this object topmost
:ref:`clear <no-21087>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-21088>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-21089>`  Given a position relative to this control, return a position relative
:ref:`copy <no-21090>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-21091>`                   Called by uiApp when the user requests a cut operation.
:ref:`cyclePages <no-21092>`            Moves through the pages by the specified amount, wrapping
:ref:`drawArc <no-21093>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-21094>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-21095>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-21096>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-21097>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-21098>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-21099>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-21100>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-21101>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-21102>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-21103>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-21104>`              Draws text on the object at the specified position
:ref:`endHover <no-21105>`              
:ref:`fitToSizer <no-21106>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-21107>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-21108>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-21109>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-21110>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-21111>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-21112>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-21113>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-21114>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-21115>`      Returns the current mouse position on the entire screen
:ref:`getPageImage <no-21116>`          
:ref:`getPageNumber <no-21117>`         Given a page, returns its position.
:ref:`getPositionInSizer <no-21118>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-21119>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-21120>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-21121>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-21122>`                  Make the object invisible.
:ref:`initEvents <no-21123>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-21124>`        Hook for subclasses. User subclasses should set properties
:ref:`insertPage <no-21125>`            Inserts the page into the pageframe at the specified position,
:ref:`isContainedBy <no-21126>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-21127>`           Call the given function on this object and all of its Children. If
:ref:`layout <no-21128>`                Wrap the wx version of the call, if possible.
:ref:`lockDisplay <no-21129>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-21130>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-21131>`    Moves this object's tab order before the passed obj.
:ref:`nextPage <no-21132>`              Selects the next page. If the last page is selected,
:ref:`objectCoordinates <no-21133>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-21134>`               
:ref:`paste <no-21135>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-21136>`           
:ref:`priorPage <no-21137>`             Selects the previous page. If the first page is selected,
:ref:`processDroppedFiles <no-21138>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-21139>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-21140>`            Raise the passed Dabo event.
:ref:`reCreate <no-21141>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-21142>`              Recreate the object.
:ref:`redraw <no-21143>`                Called when the object is (re)drawn.
:ref:`refresh <no-21144>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-21145>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-21146>`               Destroys the object.
:ref:`removeDrawnObject <no-21147>`     
:ref:`removePage <no-21148>`            Removes the specified page. You can specify a page by either
:ref:`sendToBack <no-21149>`            Places this object behind all others.
:ref:`setAll <no-21150>`                Set all child object properties to the passed value.
:ref:`setFocus <no-21151>`              Sets focus to the object.
:ref:`setPageImage <no-21152>`          
:ref:`setPositionInSizer <no-21153>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-21154>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-21155>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-21156>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-21157>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-21158>`                  Make the object visible.
:ref:`showContainingPage <no-21159>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-21160>`       Display a context menu (popup) at the specified position.
:ref:`showPage <no-21161>`              
:ref:`super <no-21162>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-21163>`           Remove a previously registered event binding.
:ref:`unbindKey <no-21164>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-21165>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-21166>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-21167>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods
=======

.. _no-21079:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.appendPage(self, pgCls=None, makeActive=False)

   
   Creates a new page, which should be a subclass of dPage. If makeActive
   is True, the page is displayed; otherwise, it is added without changing
   the SelectedPage.
   



-------

.. _no-21092:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.cyclePages(self, num)

   
   Moves through the pages by the specified amount, wrapping
   around the ends. Negative values move to previous pages; positive
   move through the next pages.
   



-------

.. _no-21116:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.getPageImage(self, pg)



-------

.. _no-21117:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.getPageNumber(self, pg)

   Given a page, returns its position.



-------

.. _no-21125:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.insertPage(self, pos, pgCls=None, makeActive=False, ignoreOverride=False)

   
   Inserts the page into the pageframe at the specified position,
   and makes it the active (displayed) page if makeActive is True.
   



-------

.. _no-21128:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.layout(self)

   Wrap the wx version of the call, if possible.



-------

.. _no-21132:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.nextPage(self)

   
   Selects the next page. If the last page is selected,
   it will select the first page.
   



-------

.. _no-21137:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.priorPage(self)

   
   Selects the previous page. If the first page is selected,
   it will select the last page.
   



-------

.. _no-21148:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.removePage(self, pgOrPos, delPage=True)

   
   Removes the specified page. You can specify a page by either
   passing the page itself, or a position. If delPage is True (default),
   the page is released, and None is returned. If delPage is
   False, the page is returned.
   



-------

.. _no-21152:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.setPageImage(self, pg, img)



-------

.. _no-21161:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.showPage(self, pg)



-------


Methods - inherited
=====================

.. _no-21074:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21075:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-21076:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21077:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21078:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21080:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.autoBindEvents(self, force=True)
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

.. _no-21081:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21082:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21083:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-21084:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-21085:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-21086:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21087:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21088:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21089:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21090:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21091:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21093:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21094:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21095:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-21096:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21097:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21098:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21099:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21100:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21101:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21102:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21103:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21104:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21105:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21106:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21107:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-21108:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-21109:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-21110:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21111:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21112:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21113:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21114:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21115:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21118:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21119:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-21120:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21121:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21122:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21123:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21124:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21126:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21127:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-21129:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.lockDisplay(self)
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

.. _no-21130:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21131:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21133:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21134:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21135:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21136:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21138:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21139:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21140:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21141:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-21142:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21143:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21144:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21145:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21146:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21147:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21149:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21150:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-21151:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21153:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21154:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-21155:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-21156:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21157:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21158:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21159:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21160:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21162:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-21163:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-21164:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21165:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21166:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-21167:

.. function:: dabo.ui.uiwx.dPageFrameNoTabs.dPageFrameNoTabs.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
