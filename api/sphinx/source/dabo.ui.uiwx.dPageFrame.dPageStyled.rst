
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dPageFrame

.. _dabo.ui.uiwx.dPageFrame.dPageStyled:

===============================================
|doc_title|  **dPageFrame.dPageStyled** - class
===============================================


Creates a pageframe, which can contain an unlimited number of pages,
each of which should be a subclass/instance of the dPage class. Note that there
is no visible border around the pages.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dPageStyled**

.. inheritance-diagram:: dPageStyled


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`
* :ref:`wx.lib.agw.flatnotebook.FlatNotebook`



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



   * - .. image:: _static/macWidgets/dPageStyled.png
          :scale: 75 %
          :target: _static/macWidgets/dPageStyled.png
          :alt: dPageStyled



     - .. image:: _static/winWidgets/dPageStyled.png
          :scale: 75 %
          :target: _static/winWidgets/dPageStyled.png
          :alt: dPageStyled



     - .. image:: _static/nixWidgets/dPageStyled.png
          :scale: 75 %
          :target: _static/nixWidgets/dPageStyled.png
          :alt: dPageStyled


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dPageFrame.dPageStyled

   .. automethod:: dabo.ui.uiwx.dPageFrame.dPageStyled.__init__

|method_summary| Properties Summary
===================================


============================================ ========================
:ref:`ActiveTabColor <no-17835>`             Specifies the color of the active tab (str or 3-tuple) (Default=None)
:ref:`ActiveTabTextColor <no-17836>`         Specifies the color of the text of the active tab (str or 3-tuple) (Default=None)
:ref:`Application <no-17837>`                Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-17838>`                  Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-17839>`                  The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-17840>`                Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-17841>`                Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-17842>`            Style of line for the border drawn around the control.
:ref:`BorderStyle <no-17843>`                Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-17844>`                Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-17845>`                     The position of the bottom side of the object. This is a
:ref:`Caption <no-17846>`                    The caption of the object. (str)
:ref:`Children <no-17847>`                   Returns a list of object references to the children of
:ref:`Class <no-17848>`                      The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-17849>`           Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-17850>`       Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-17851>`         Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-17852>`         Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-17853>`           Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-17854>`         Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-17855>`     Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-17856>`         Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-17857>`         Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-17858>`             Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-17859>`             Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-17860>`                Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-17861>`            Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-17862>`            Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-17863>`          Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-17864>`            Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-17865>`       Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-17866>`           Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-17867>`              Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-17868>`                Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-17869>`        Dynamically determine the value of the MousePointer property.
:ref:`DynamicPageClass <no-17870>`           Dynamically determine the value of the PageClass property.
:ref:`DynamicPageCount <no-17871>`           Dynamically determine the value of the PageCount property.
:ref:`DynamicPosition <no-17872>`            Dynamically determine the value of the Position property.
:ref:`DynamicSelectedPage <no-17873>`        Dynamically determine the value of the SelectedPage property.
:ref:`DynamicSelectedPageNumber <no-17874>`  Dynamically determine the value of the SelectedPageNumber property.
:ref:`DynamicSize <no-17875>`                Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-17876>`          Dynamically determine the value of the StatusText property.
:ref:`DynamicTabPosition <no-17877>`         Dynamically determine the value of the TabPosition property.
:ref:`DynamicTag <no-17878>`                 Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-17879>`         Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-17880>`                 Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-17881>`        Dynamically determine the value of the Transparency property.
:ref:`DynamicUpdateInactivePages <no-17882>` Dynamically determine the value of the UpdateInactivePages property.
:ref:`DynamicVisible <no-17883>`             Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-17884>`               Dynamically determine the value of the Width property.
:ref:`Enabled <no-17885>`                    Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-17886>`                       Specifies font object for this control. (dFont)
:ref:`FontBold <no-17887>`                   Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-17888>`            Human-readable description of the current font settings. (str)
:ref:`FontFace <no-17889>`                   Specifies the font face. (str)
:ref:`FontInfo <no-17890>`                   Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-17891>`                 Specifies whether font is italicized. (bool)
:ref:`FontSize <no-17892>`                   Specifies the point size of the font. (int)
:ref:`FontUnderline <no-17893>`              Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-17894>`                  Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-17895>`                       Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-17896>`                     Specifies the height of the object. (int)
:ref:`HelpContextText <no-17897>`            Specifies the context-sensitive help text associated with this
:ref:`Hover <no-17898>`                      When True, Mouse Enter events fire the onHover method, and
:ref:`InactiveTabTextColor <no-17899>`       Specifies the color of the text of non active tabs (str or 3-tuple) (Default=None)
:ref:`Left <no-17900>`                       Specifies the left position of the object. (int)
:ref:`LogEvents <no-17901>`                  Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-17902>`              Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-17903>`                Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-17904>`               Maximum allowable width for the control in pixels.  (int)
:ref:`MenuBackColor <no-17905>`              Specifies the background color of the tab area. This is exactly the same as
:ref:`MinimumHeight <no-17906>`              Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-17907>`                Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-17908>`               Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-17909>`               Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-17910>`                       Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-17911>`                   Specifies the base name of the object.
:ref:`PageClass <no-17912>`                  Specifies the class of control to use for pages by default. (classRef)
:ref:`PageCount <no-17913>`                  Specifies the number of pages in the pageframe. (int)
:ref:`PageSizerClass <no-17914>`             Default sizer class for pages added automatically to this control. Set
:ref:`Pages <no-17915>`                      Returns a list of the contained pages.  (list)
:ref:`Parent <no-17916>`                     The containing object. (obj)
:ref:`Position <no-17917>`                   The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-17918>`          Reference to the Preference Management object  (dPref)
:ref:`RegID <no-17919>`                      A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-17920>`                      The position of the right side of the object. This is a
:ref:`SelectedPage <no-17921>`               References the current frontmost page.  (dPage)
:ref:`SelectedPageNumber <no-17922>`         Returns the index of the current frontmost page.  (int)
:ref:`ShowDropdownTabList <no-17923>`        Specifies whether the dropdown tab list button is visible in the menu (bool) (Default=False)
:ref:`ShowMenuCloseButton <no-17924>`        Specifies whether the close button is visible in the menu (bool) (Default=True)
:ref:`ShowMenuOnSingleTab <no-17925>`        Specifies whether the tab thumbs and nav buttons are shown when there is a single tab. (bool) (Defau
:ref:`ShowNavButtons <no-17926>`             Specifies whether the left and right nav buttons are visible in the menu (bool) (Default=True)
:ref:`ShowPageCloseButtons <no-17927>`       Specifies whether the close button is visible on the page tab (bool) (Default=False)
:ref:`Size <no-17928>`                       The size of the object. (tuple)
:ref:`Sizer <no-17929>`                      The sizer for the object.
:ref:`StatusText <no-17930>`                 Specifies the text that displays in the form's status bar, if any.
:ref:`TabAreaColor <no-17931>`               Specifies the background color of the tab area. This is exactly the same as
:ref:`TabPosition <no-17932>`                Specifies where the page tabs are located. (string)
:ref:`TabSideIncline <no-17933>`             Specifies the incline of the sides of the tab in degrees (int) (Default=0)
:ref:`TabStop <no-17934>`                    Specifies whether this control can receive focus from keyboard navigation.
:ref:`TabStyle <no-17935>`                   Specifies the style of the display tabs. (string)
:ref:`Tag <no-17936>`                        A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-17937>`                Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-17938>`                        The top position of the object. (int)
:ref:`Transparency <no-17939>`               Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-17940>`          Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`UpdateInactivePages <no-17941>`        Determines if the inactive pages are updated too. (bool)
:ref:`UseSmartFocus <no-17942>`              Determines if focus has to be restored to the last active
:ref:`Visible <no-17943>`                    Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-17944>`            Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-17945>`                      The width of the object. (int)
:ref:`WindowHandle <no-17946>`               The platform-specific handle for the window. Read-only. (long)

============================================ ========================


Properties
==========

.. _no-17835:

**ActiveTabColor** 

Specifies the color of the active tab (str or 3-tuple) (Default=None)
        Note: is not visible with the 'VC8' TabStyle



-------

.. _no-17836:

**ActiveTabTextColor** 

Specifies the color of the text of the active tab (str or 3-tuple) (Default=None)
        Note: is not visible with the 'VC8' TabStyle



-------

.. _no-17899:

**InactiveTabTextColor** 

Specifies the color of the text of non active tabs (str or 3-tuple) (Default=None)
        Note: is not visible with the 'VC8' TabStyle



-------

.. _no-17905:

**MenuBackColor** 

Specifies the background color of the tab area. This is exactly the same as
        the 'TabAreaColor' property, but is maintained for backwards compatibility.
        Default = None.  (str or 3-tuple) Note: is not visible with 'VC71' TabStyle.



-------

.. _no-17923:

**ShowDropdownTabList** 

Specifies whether the dropdown tab list button is visible in the menu (bool) (Default=False)
        Setting this property to True will set ShowNavButtons to False



-------

.. _no-17924:

**ShowMenuCloseButton** 

Specifies whether the close button is visible in the menu (bool) (Default=True)



-------

.. _no-17925:

**ShowMenuOnSingleTab** 

Specifies whether the tab thumbs and nav buttons are shown when there is a single tab. (bool) (Default=True)



-------

.. _no-17926:

**ShowNavButtons** 

Specifies whether the left and right nav buttons are visible in the menu (bool) (Default=True)
        Setting this property to True will set ShowDropdownTabList to False



-------

.. _no-17927:

**ShowPageCloseButtons** 

Specifies whether the close button is visible on the page tab (bool) (Default=False)



-------

.. _no-17931:

**TabAreaColor** 

Specifies the background color of the tab area. This is exactly the same as
        the 'MenuBackColor' property, but with a more intuitive name.  (str or 3-tuple)
        (Default=None) Note: is not visible with 'VC71' TabStyle.



-------

.. _no-17933:

**TabSideIncline** 

Specifies the incline of the sides of the tab in degrees (int) (Default=0)
            Acceptable values are 0  - 15.
            Note: this property will have no effect on TabStyles other than Default.
            



-------

.. _no-17935:

**TabStyle** 

Specifies the style of the display tabs. (string)
            "Default" (default)
            "VC8"
            "VC71"
            "Fancy"
            "Firefox"
            



-------


Properties - inherited
========================

.. _no-17837:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17838:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17839:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17840:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17841:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17842:

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

.. _no-17843:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17844:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17845:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-17846:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17847:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-17848:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17849:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17850:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17851:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17852:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17853:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17854:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17855:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17856:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17857:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17858:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17859:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17860:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17861:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17862:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17863:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17864:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17865:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17866:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17867:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17868:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17869:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17870:

**DynamicPageClass** 

Dynamically determine the value of the PageClass property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
PageClass property. If DynamicPageClass is set to None (the default), PageClass
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17871:

**DynamicPageCount** 

Dynamically determine the value of the PageCount property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
PageCount property. If DynamicPageCount is set to None (the default), PageCount
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17872:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17873:

**DynamicSelectedPage** 

Dynamically determine the value of the SelectedPage property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectedPage property. If DynamicSelectedPage is set to None (the default), SelectedPage
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17874:

**DynamicSelectedPageNumber** 

Dynamically determine the value of the SelectedPageNumber property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
SelectedPageNumber property. If DynamicSelectedPageNumber is set to None (the default), SelectedPageNumber
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17875:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17876:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17877:

**DynamicTabPosition** 

Dynamically determine the value of the TabPosition property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
TabPosition property. If DynamicTabPosition is set to None (the default), TabPosition
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17878:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17879:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17880:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17881:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17882:

**DynamicUpdateInactivePages** 

Dynamically determine the value of the UpdateInactivePages property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
UpdateInactivePages property. If DynamicUpdateInactivePages is set to None (the default), UpdateInactivePages
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17883:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17884:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17885:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-17886:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-17887:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17888:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17889:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17890:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17891:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17892:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17893:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17894:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17895:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-17896:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17897:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17898:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17900:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17901:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17902:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17903:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17904:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17906:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17907:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17908:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17909:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17910:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-17911:

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

.. _no-17912:

**PageClass** 

Specifies the class of control to use for pages by default. (classRef)
    This really only applies when using the PageCount property to set the
    number of pages. If you instead use AddPage() you still need to send
    an instance as usual. Class must descend from a dabo base class.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17913:

**PageCount** 

Specifies the number of pages in the pageframe. (int)
    When using this to increase the number of pages, PageClass
    will be queried as the object to use as the page object.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17914:

**PageSizerClass** 

Default sizer class for pages added automatically to this control. Set
    this to None to prevent sizers from being automatically added to child
    pages. (dSizer or None)


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17915:

**Pages** 

Returns a list of the contained pages.  (list)


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17916:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-17917:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-17918:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17919:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17920:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-17921:

**SelectedPage** 

References the current frontmost page.  (dPage)


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17922:

**SelectedPageNumber** 

Returns the index of the current frontmost page.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17928:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-17929:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-17930:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17932:

**TabPosition** 

Specifies where the page tabs are located. (string)
            Top (default)
            Bottom
            


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17934:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-17936:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17937:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17938:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17939:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17940:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17941:

**UpdateInactivePages** 

Determines if the inactive pages are updated too. (bool)
    Setting it to False can significantly improve update performance
    of multipage forms. Default=True.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17942:

**UseSmartFocus** 

Determines if focus has to be restored to the last active
    control on page when it become selected. (bool) Default=False.
    


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17943:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17944:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17945:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17946:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-17947>`       Occurs when a window background has been erased and needs repainting.
:ref:`ChildBorn <no-17948>`              Occurs when a child control is created.
:ref:`Create <no-17949>`                 Occurs after the control or form is created.
:ref:`Destroy <no-17950>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-17951>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-17952>`               Occurs when the control gets the focus.
:ref:`Idle <no-17953>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-17954>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-17955>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-17956>`               
:ref:`KeyUp <no-17957>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-17958>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-17959>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-17960>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-17961>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-17962>`             
:ref:`MouseLeave <no-17963>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-17964>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-17965>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-17966>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-17967>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-17968>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-17969>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-17970>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-17971>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-17972>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-17973>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-17974>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-17975>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-17976>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-17977>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-17978>`                   Occurs when the control's position changes.
:ref:`PageChanged <no-17979>`            Occurs when a page in a pageframe-like control changes
:ref:`PageChanging <no-17980>`           Occurs when the current page in a pageframe-like control is about to change
:ref:`PageClosed <no-17981>`             Occurs when a page in a dPageStyled control is closed
:ref:`PageClosing <no-17982>`            Occurs when a page in a dPageStyled control is about to close
:ref:`Paint <no-17983>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-17984>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-17985>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-17986>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-17987>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-17947:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-17948:

**ChildBorn** 

Occurs when a child control is created.



-------

.. _no-17949:

**Create** 

Occurs after the control or form is created.



-------

.. _no-17950:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-17951:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-17952:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-17953:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-17954:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-17955:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-17956:

**KeyEvent** 



-------

.. _no-17957:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-17958:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-17959:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-17960:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-17961:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-17962:

**MouseEvent** 



-------

.. _no-17963:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-17964:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-17965:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-17966:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-17967:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-17968:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-17969:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-17970:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-17971:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-17972:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-17973:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-17974:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-17975:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-17976:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-17977:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-17978:

**Move** 

Occurs when the control's position changes.



-------

.. _no-17979:

**PageChanged** 

Occurs when a page in a pageframe-like control changes



-------

.. _no-17980:

**PageChanging** 

Occurs when the current page in a pageframe-like control is about to change



-------

.. _no-17981:

**PageClosed** 

Occurs when a page in a dPageStyled control is closed



-------

.. _no-17982:

**PageClosing** 

Occurs when a page in a dPageStyled control is about to close



-------

.. _no-17983:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-17984:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-17985:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-17986:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-17987:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


=============================================== ========================
:ref:`absoluteCoordinates <no-17988>`           Translates a position value for a control to absolute screen position.
:ref:`addImage <no-17989>`                      Adds the passed image to the control's ImageList, and maintains
:ref:`addObject <no-17990>`                     Instantiate object as a child of self.
:ref:`afterInit <no-17991>`                     Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-17992>`                  
:ref:`afterSetProperties <no-17993>`            
:ref:`appendPage <no-17994>`                    Appends the page to the pageframe, and optionally sets
:ref:`autoBindEvents <no-17995>`                Automatically bind any on*() methods to the associated event.
:ref:`base_AcceptsFocus <no-17996>`             Please use PyPanel.AcceptsFocus instead.
:ref:`base_AcceptsFocusFromKeyboard <no-17997>` Please use PyPanel.AcceptsFocusFromKeyboard instead.
:ref:`base_AddChild <no-17998>`                 Please use PyPanel.AddChild instead.
:ref:`base_DoGetBestSize <no-17999>`            Please use PyPanel.DoGetBestSize instead.
:ref:`base_DoGetClientSize <no-18000>`          Please use PyPanel.DoGetClientSize instead.
:ref:`base_DoGetPosition <no-18001>`            Please use PyPanel.DoGetPosition instead.
:ref:`base_DoGetSize <no-18002>`                Please use PyPanel.DoGetSize instead.
:ref:`base_DoGetVirtualSize <no-18003>`         Please use PyPanel.DoGetVirtualSize instead.
:ref:`base_DoMoveWindow <no-18004>`             Please use PyPanel.DoMoveWindow instead.
:ref:`base_DoSetClientSize <no-18005>`          Please use PyPanel.DoSetClientSize instead.
:ref:`base_DoSetSize <no-18006>`                Please use PyPanel.DoSetSize instead.
:ref:`base_DoSetVirtualSize <no-18007>`         Please use PyPanel.DoSetVirtualSize instead.
:ref:`base_Enable <no-18008>`                   Please use PyPanel.Enable instead.
:ref:`base_GetDefaultAttributes <no-18009>`     Please use PyPanel.GetDefaultAttributes instead.
:ref:`base_GetMaxSize <no-18010>`               Please use PyPanel.GetMaxSize instead.
:ref:`base_InitDialog <no-18011>`               Please use PyPanel.InitDialog instead.
:ref:`base_OnInternalIdle <no-18012>`           Please use PyPanel.OnInternalIdle instead.
:ref:`base_RemoveChild <no-18013>`              Please use PyPanel.RemoveChild instead.
:ref:`base_ShouldInheritColours <no-18014>`     Please use PyPanel.ShouldInheritColours instead.
:ref:`base_TransferDataFromWindow <no-18015>`   Please use PyPanel.TransferDataFromWindow instead.
:ref:`base_TransferDataToWindow <no-18016>`     Please use PyPanel.TransferDataToWindow instead.
:ref:`base_Validate <no-18017>`                 Please use PyPanel.Validate instead.
:ref:`beforeInit <no-18018>`                    Subclass hook. Called before the object is fully instantiated.
:ref:`beforePageChange <no-18019>`              Return False from this method to prevent the page from changing.
:ref:`beforePageClose <no-18020>`               Return False from this method to prevent the page from closing.
:ref:`beforeSetProperties <no-18021>`           
:ref:`bindEvent <no-18022>`                     Bind a dEvent to a callback function.
:ref:`bindEvents <no-18023>`                    Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-18024>`                       Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-18025>`                  Makes this object topmost
:ref:`clear <no-18026>`                         Clears the background of custom-drawn objects.
:ref:`clone <no-18027>`                         Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-18028>`          Given a position relative to this control, return a position relative
:ref:`copy <no-18029>`                          Called by uiApp when the user requests a copy operation.
:ref:`cut <no-18030>`                           Called by uiApp when the user requests a cut operation.
:ref:`cyclePages <no-18031>`                    Moves through the pages by the specified amount, wrapping
:ref:`drawArc <no-18032>`                       Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-18033>`                    Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-18034>`                    Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-18035>`                   Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-18036>`               Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-18037>`                  Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-18038>`                      Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-18039>`                 Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-18040>`                   Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-18041>`                 Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-18042>`          Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-18043>`                      Draws text on the object at the specified position
:ref:`endHover <no-18044>`                      
:ref:`fitToSizer <no-18045>`                    Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-18046>`                    Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-18047>`                Reset the font zoom back to zero.
:ref:`fontZoomOut <no-18048>`                   Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-18049>`               Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-18050>`               Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-18051>`              Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-18052>`             Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-18053>`              Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-18054>`              Returns the current mouse position on the entire screen
:ref:`getPageImage <no-18055>`                  Returns the index of the specified page's image in the
:ref:`getPositionInSizer <no-18056>`            Convenience method to let you call this directly on the object.
:ref:`getProperties <no-18057>`                 Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-18058>`                  Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-18059>`                 Returns a dict containing the object's sizer property info. The
:ref:`hide <no-18060>`                          Make the object invisible.
:ref:`initEvents <no-18061>`                    Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-18062>`                Hook for subclasses. User subclasses should set properties
:ref:`insertPage <no-18063>`                    
:ref:`isContainedBy <no-18064>`                 Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-18065>`                   Call the given function on this object and all of its Children. If
:ref:`layout <no-18066>`                        Wrap the wx version of the call, if possible.
:ref:`lockDisplay <no-18067>`                   Locks the visual updates to the control.
:ref:`movePage <no-18068>`                      Moves the specified 'old' page to the new position and
:ref:`moveTabOrderAfter <no-18069>`             Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-18070>`            Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-18071>`             Given a position relative to the form, return a position relative
:ref:`onHover <no-18072>`                       
:ref:`paste <no-18073>`                         Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-18074>`                   
:ref:`processDroppedFiles <no-18075>`           Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-18076>`            Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-18077>`                    Raise the passed Dabo event.
:ref:`reCreate <no-18078>`                      Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-18079>`                      Recreate the object.
:ref:`redraw <no-18080>`                        Called when the object is (re)drawn.
:ref:`refresh <no-18081>`                       Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-18082>`           Translates an absolute screen position to position value for a control.
:ref:`release <no-18083>`                       Destroys the object.
:ref:`removeDrawnObject <no-18084>`             
:ref:`removePage <no-18085>`                    Removes the specified page. You can specify a page by either
:ref:`sendToBack <no-18086>`                    Places this object behind all others.
:ref:`setAll <no-18087>`                        Set all child object properties to the passed value.
:ref:`setFocus <no-18088>`                      Sets focus to the object.
:ref:`setPageImage <no-18089>`                  Sets the specified page's image to the image corresponding
:ref:`setPositionInSizer <no-18090>`            Convenience method to let you call this directly on the object.
:ref:`setProperties <no-18091>`                 Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-18092>`         Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-18093>`                  Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-18094>`                 Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-18095>`                          Make the object visible.
:ref:`showContainingPage <no-18096>`            If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-18097>`               Display a context menu (popup) at the specified position.
:ref:`super <no-18098>`                         This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-18099>`                   Remove a previously registered event binding.
:ref:`unbindKey <no-18100>`                     Unbind a previously bound key combination.
:ref:`unlockDisplay <no-18101>`                 Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-18102>`              Immediately unlocks the display, no matter how many previous
:ref:`update <no-18103>`                        Update the properties of this object and all contained objects.

=============================================== ========================


Methods
=======

.. _no-18020:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.beforePageClose(self, page)

   Return False from this method to prevent the page from closing.



-------

.. _no-18063:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.insertPage(self, \*args, \**kwargs)



-------


Methods - inherited
=====================

.. _no-17988:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17989:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.addImage(self, img, key=None)
   :noindex:


   
   Adds the passed image to the control's ImageList, and maintains
   a reference to it that is retrievable via the key value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17990:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-17991:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-17992:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17993:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-17994:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.appendPage(self, pgCls=None, caption='', imgKey=None, \**kwargs)
   :noindex:


   
   Appends the page to the pageframe, and optionally sets
   the page caption and image. The image should have already
   been added to the pageframe if it is going to be set here.
   
   Any kwargs sent will be passed on to the constructor of the
   page class.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-17995:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.autoBindEvents(self, force=True)
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

.. _no-17996:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.base_AcceptsFocus(*args, \**kwargs)
   :noindex:


   Please use PyPanel.AcceptsFocus instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-17997:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.base_AcceptsFocusFromKeyboard(*args, \**kwargs)
   :noindex:


   Please use PyPanel.AcceptsFocusFromKeyboard instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-17998:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.base_AddChild(*args, \**kwargs)
   :noindex:


   Please use PyPanel.AddChild instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-17999:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.base_DoGetBestSize(*args, \**kwargs)
   :noindex:


   Please use PyPanel.DoGetBestSize instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-18000:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.base_DoGetClientSize(*args, \**kwargs)
   :noindex:


   Please use PyPanel.DoGetClientSize instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-18001:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.base_DoGetPosition(*args, \**kwargs)
   :noindex:


   Please use PyPanel.DoGetPosition instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-18002:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.base_DoGetSize(*args, \**kwargs)
   :noindex:


   Please use PyPanel.DoGetSize instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-18003:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.base_DoGetVirtualSize(*args, \**kwargs)
   :noindex:


   Please use PyPanel.DoGetVirtualSize instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-18004:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.base_DoMoveWindow(*args, \**kwargs)
   :noindex:


   Please use PyPanel.DoMoveWindow instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-18005:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.base_DoSetClientSize(*args, \**kwargs)
   :noindex:


   Please use PyPanel.DoSetClientSize instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-18006:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.base_DoSetSize(*args, \**kwargs)
   :noindex:


   Please use PyPanel.DoSetSize instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-18007:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.base_DoSetVirtualSize(*args, \**kwargs)
   :noindex:


   Please use PyPanel.DoSetVirtualSize instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-18008:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.base_Enable(*args, \**kwargs)
   :noindex:


   Please use PyPanel.Enable instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-18009:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.base_GetDefaultAttributes(*args, \**kwargs)
   :noindex:


   Please use PyPanel.GetDefaultAttributes instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-18010:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.base_GetMaxSize(*args, \**kwargs)
   :noindex:


   Please use PyPanel.GetMaxSize instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-18011:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.base_InitDialog(*args, \**kwargs)
   :noindex:


   Please use PyPanel.InitDialog instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-18012:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.base_OnInternalIdle(*args, \**kwargs)
   :noindex:


   Please use PyPanel.OnInternalIdle instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-18013:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.base_RemoveChild(*args, \**kwargs)
   :noindex:


   Please use PyPanel.RemoveChild instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-18014:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.base_ShouldInheritColours(*args, \**kwargs)
   :noindex:


   Please use PyPanel.ShouldInheritColours instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-18015:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.base_TransferDataFromWindow(*args, \**kwargs)
   :noindex:


   Please use PyPanel.TransferDataFromWindow instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-18016:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.base_TransferDataToWindow(*args, \**kwargs)
   :noindex:


   Please use PyPanel.TransferDataToWindow instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-18017:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.base_Validate(*args, \**kwargs)
   :noindex:


   Please use PyPanel.Validate instead.


Inherited from: 'wx._windows.PyPanel - can not provide a link

-------

.. _no-18018:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18019:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.beforePageChange(self, fromPage, toPage)
   :noindex:


   Return False from this method to prevent the page from changing.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-18021:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18022:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-18023:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-18024:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-18025:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18026:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18027:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18028:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18029:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18030:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18031:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.cyclePages(self, num)
   :noindex:


   
   Moves through the pages by the specified amount, wrapping
   around the ends. Negative values move to previous pages; positive
   move through the next pages.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-18032:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18033:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18034:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-18035:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18036:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18037:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18038:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18039:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18040:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18041:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18042:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18043:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18044:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18045:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18046:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-18047:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-18048:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-18049:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18050:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18051:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18052:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18053:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18054:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18055:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.getPageImage(self, pg)
   :noindex:


   
   Returns the index of the specified page's image in the
   current image list, or -1 if no image is set for the page.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-18056:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18057:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-18058:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18059:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18060:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18061:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18062:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18064:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18065:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-18066:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.layout(self)
   :noindex:


   Wrap the wx version of the call, if possible.


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-18067:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.lockDisplay(self)
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

.. _no-18068:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.movePage(self, oldPgOrPos, newPos, selecting=True)
   :noindex:


   
   Moves the specified 'old' page to the new position and
   optionally selects it. If an invalid page number is passed,
   it returns False without changing anything.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-18069:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18070:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18071:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18072:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18073:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18074:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18075:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18076:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18077:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18078:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-18079:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18080:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18081:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18082:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18083:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18084:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18085:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.removePage(self, pgOrPos, delPage=True)
   :noindex:


   
   Removes the specified page. You can specify a page by either
   passing the page itself, or a position. If delPage is True (default),
   the page is released, and None is returned. If delPage is
   False, the page is returned.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-18086:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18087:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-18088:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18089:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.setPageImage(self, pg, imgKey)
   :noindex:


   
   Sets the specified page's image to the image corresponding
   to the specified key. May also optionally pass the index of the
   image in the ImageList rather than the key.
   


Inherited from: :ref:`dabo.ui.uiwx.dPageFrameMixin.dPageFrameMixin`

-------

.. _no-18090:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18091:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-18092:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-18093:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18094:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18095:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18096:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18097:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18098:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-18099:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-18100:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18101:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18102:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-18103:

.. function:: dabo.ui.uiwx.dPageFrame.dPageStyled.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
