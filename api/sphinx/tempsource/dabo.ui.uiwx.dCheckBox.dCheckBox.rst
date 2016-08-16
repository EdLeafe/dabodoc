
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dCheckBox

.. _dabo.ui.uiwx.dCheckBox.dCheckBox:

============================================
|doc_title|  **dCheckBox.dCheckBox** - class
============================================

Creates a checkbox, allowing editing boolean values.



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dCheckBox**

.. inheritance-diagram:: dCheckBox


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`



|subclasses| Known Subclasses
=============================

* :ref:`dabo.lib.datanav.Page.SelectCheckBox`



|appearance| Control Appearance
===============================

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - .. image:: _static/macWidgets/dCheckBox.png
          :scale: 75 %
          :target: _static/macWidgets/dCheckBox.png
          :alt: dCheckBox



     - .. image:: _static/winWidgets/dCheckBox.png
          :scale: 75 %
          :target: _static/winWidgets/dCheckBox.png
          :alt: dCheckBox



     - .. image:: _static/nixWidgets/dCheckBox.png
          :scale: 75 %
          :target: _static/nixWidgets/dCheckBox.png
          :alt: dCheckBox


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dCheckBox.dCheckBox

   .. automethod:: dabo.ui.uiwx.dCheckBox.dCheckBox.__init__

|method_summary| Properties Summary
===================================


========================================== ========================
:ref:`Alignment <no-28980>`                Specifies the alignment of the text.
:ref:`Application <no-28981>`              Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-28982>`                Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-28983>`                The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-28984>`              Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-28985>`              Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-28986>`          Style of line for the border drawn around the control.
:ref:`BorderStyle <no-28987>`              Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-28988>`              Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-28989>`                   The position of the bottom side of the object. This is a
:ref:`Caption <no-28990>`                  The caption of the object. (str)
:ref:`Children <no-28991>`                 Returns a list of object references to the children of
:ref:`Class <no-28992>`                    The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-28993>`         Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-28994>`     Reference to the sizer item that control's this control's layout.
:ref:`DataField <no-28995>`                Specifies the data field of the dataset to use as the source
:ref:`DataSource <no-28996>`               Specifies the dataset to use as the source of data.  (str)
:ref:`DisableOnEmptyDataSource <no-28997>` When True and the DataSource is an empty dataset (it must be a dBizobj instance),
:ref:`DroppedFileHandler <no-28998>`       Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-28999>`       Reference to the object that will handle text dropped on this control.
:ref:`DynamicAlignment <no-29000>`         Dynamically determine the value of the Alignment property.
:ref:`DynamicBackColor <no-29001>`         Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-29002>`       Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-29003>`   Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-29004>`       Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-29005>`       Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-29006>`           Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-29007>`           Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-29008>`              Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-29009>`          Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-29010>`          Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-29011>`        Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-29012>`          Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-29013>`     Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-29014>`         Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-29015>`            Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-29016>`              Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-29017>`      Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-29018>`          Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-29019>`              Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-29020>`        Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-29021>`               Dynamically determine the value of the Tag property.
:ref:`DynamicThreeState <no-29022>`        Dynamically determine the value of the ThreeState property.
:ref:`DynamicToolTipText <no-29023>`       Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-29024>`               Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-29025>`      Dynamically determine the value of the Transparency property.
:ref:`DynamicUserThreeState <no-29026>`    Dynamically determine the value of the UserThreeState property.
:ref:`DynamicValue <no-29027>`             Dynamically determine the value of the Value property.
:ref:`DynamicVisible <no-29028>`           Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-29029>`             Dynamically determine the value of the Width property.
:ref:`Enabled <no-29030>`                  Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-29031>`                     Specifies font object for this control. (dFont)
:ref:`FontBold <no-29032>`                 Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-29033>`          Human-readable description of the current font settings. (str)
:ref:`FontFace <no-29034>`                 Specifies the font face. (str)
:ref:`FontInfo <no-29035>`                 Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-29036>`               Specifies whether font is italicized. (bool)
:ref:`FontSize <no-29037>`                 Specifies the point size of the font. (int)
:ref:`FontUnderline <no-29038>`            Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-29039>`                Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-29040>`                     Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-29041>`                   Specifies the height of the object. (int)
:ref:`HelpContextText <no-29042>`          Specifies the context-sensitive help text associated with this
:ref:`Hover <no-29043>`                    When True, Mouse Enter events fire the onHover method, and
:ref:`IsSecret <no-29044>`                 Flag for indicating sensitive data, such as Password field, that is not
:ref:`Left <no-29045>`                     Specifies the left position of the object. (int)
:ref:`LogEvents <no-29046>`                Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-29047>`            Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-29048>`              Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-29049>`             Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-29050>`            Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-29051>`              Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-29052>`             Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-29053>`             Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-29054>`                     Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-29055>`                 Specifies the base name of the object.
:ref:`Parent <no-29056>`                   The containing object. (obj)
:ref:`PersistSecretData <no-29057>`        If True, allow persisting the secret data in encrypted form.
:ref:`Position <no-29058>`                 The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-29059>`        Reference to the Preference Management object  (dPref)
:ref:`RegID <no-29060>`                    A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-29061>`                    The position of the right side of the object. This is a
:ref:`SaveRestoreValue <no-29062>`         Specifies whether the Value of the control gets saved when
:ref:`Size <no-29063>`                     The size of the object. (tuple)
:ref:`Sizer <no-29064>`                    The sizer for the object.
:ref:`Source <no-29065>`                   Reference to the object to which this control's Value is bound  (object)
:ref:`StatusText <no-29066>`               Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-29067>`                  Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-29068>`                      A property that user code can safely use for specific purposes.
:ref:`ThreeState <no-29069>`               Specifies wether the checkbox support 3 states.
:ref:`ToolTipText <no-29070>`              Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-29071>`                      The top position of the object. (int)
:ref:`Transparency <no-29072>`             Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-29073>`        Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`UserThreeState <no-29074>`           Specifies whether the user is allowed to set the third state.
:ref:`Value <no-29075>`                    Specifies the current state of the control (the value of the field). (varies)
:ref:`Visible <no-29076>`                  Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-29077>`          Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-29078>`                    The width of the object. (int)
:ref:`WindowHandle <no-29079>`             The platform-specific handle for the window. Read-only. (long)

========================================== ========================


Properties
==========

.. _no-29000:

**DynamicAlignment** 

Dynamically determine the value of the Alignment property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Alignment property. If DynamicAlignment is set to None (the default), Alignment
will not be dynamically evaluated.



-------

.. _no-29022:

**DynamicThreeState** 

Dynamically determine the value of the ThreeState property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ThreeState property. If DynamicThreeState is set to None (the default), ThreeState
will not be dynamically evaluated.



-------

.. _no-29026:

**DynamicUserThreeState** 

Dynamically determine the value of the UserThreeState property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
UserThreeState property. If DynamicUserThreeState is set to None (the default), UserThreeState
will not be dynamically evaluated.



-------

.. _no-29069:

**ThreeState** 

Specifies wether the checkbox support 3 states.

        True  : Checkbox supports 3 states
        False : Checkbox supports 2 states (default)



-------

.. _no-29074:

**UserThreeState** 

Specifies whether the user is allowed to set the third state.

        True  : User is allowed to set the third state.
        False : User isn't allowed to set the third state.(default)



-------


Properties - inherited
========================

.. _no-28980:

**Alignment** 

Specifies the alignment of the text.

        Left  : Checkbox to left of text (default)
        Right : Checkbox to right of text


Inherited from: 'wx._core.Control - can not provide a link

-------

.. _no-28981:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28982:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28983:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28984:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28985:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28986:

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

.. _no-28987:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28988:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28989:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-28990:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28991:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-28992:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-28993:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28994:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28995:

**DataField** 

Specifies the data field of the dataset to use as the source
    of data. (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-28996:

**DataSource** 

Specifies the dataset to use as the source of data.  (str)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-28997:

**DisableOnEmptyDataSource** 

When True and the DataSource is an empty dataset (it must be a dBizobj instance),
    control is disabled for interactive editing. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-28998:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-28999:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29001:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29002:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29003:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29004:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29005:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29006:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29007:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29008:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29009:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29010:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29011:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29012:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29013:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29014:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29015:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29016:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29017:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29018:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29019:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29020:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29021:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29023:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29024:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29025:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29027:

**DynamicValue** 

Dynamically determine the value of the Value property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Value property. If DynamicValue is set to None (the default), Value
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-29028:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29029:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29030:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-29031:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-29032:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29033:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29034:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29035:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29036:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29037:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29038:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29039:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29040:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29041:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29042:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29043:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29044:

**IsSecret** 

Flag for indicating sensitive data, such as Password field, that is not
    to be persisted. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-29045:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29046:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29047:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29048:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29049:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29050:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29051:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29052:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29053:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29054:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-29055:

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

.. _no-29056:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-29057:

**PersistSecretData** 

If True, allow persisting the secret data in encrypted form.
    Warning! Security of your data strongly depends on used encryption algorithms!
    Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-29058:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-29059:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29060:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29061:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29062:

**SaveRestoreValue** 

Specifies whether the Value of the control gets saved when
    destroyed and restored when created. Use when the control isn't
    bound to a dataSource and you want to persist the value, as in
    an options dialog. Default=False.  (bool)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-29063:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-29064:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-29065:

**Source** 

Reference to the object to which this control's Value is bound  (object)


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-29066:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29067:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-29068:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29070:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29071:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29072:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29073:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29075:

**Value** 

Specifies the current state of the control (the value of the field). (varies)


Inherited from: 'wx._controls.CheckBox - can not provide a link

-------

.. _no-29076:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29077:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29078:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29079:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-29080>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-29081>`                 Occurs after the control or form is created.
:ref:`Destroy <no-29082>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-29083>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-29084>`               Occurs when the control gets the focus.
:ref:`Hit <no-29085>`                    Occurs with the control's default event (button click,
:ref:`Idle <no-29086>`                   Occurs when the event loop has no active events to process.
:ref:`InteractiveChange <no-29087>`      Occurs when the user interactively changes the control's value.
:ref:`KeyChar <no-29088>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-29089>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-29090>`               
:ref:`KeyUp <no-29091>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-29092>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-29093>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-29094>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-29095>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-29096>`             
:ref:`MouseLeave <no-29097>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-29098>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-29099>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-29100>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-29101>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-29102>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-29103>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-29104>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-29105>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-29106>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-29107>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-29108>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-29109>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-29110>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-29111>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-29112>`                   Occurs when the control's position changes.
:ref:`Paint <no-29113>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-29114>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-29115>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-29116>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-29117>`                 Occurs when a container wants its controls to update
:ref:`ValueChanged <no-29118>`           Occurs when the control's value has changed, whether

======================================== ========================


Events
=======

.. _no-29080:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-29081:

**Create** 

Occurs after the control or form is created.



-------

.. _no-29082:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-29083:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-29084:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-29085:

**Hit** 

Occurs with the control's default event (button click,
listbox pick, checkbox, etc.)




-------

.. _no-29086:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-29087:

**InteractiveChange** 

Occurs when the user interactively changes the control's value.



-------

.. _no-29088:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-29089:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-29090:

**KeyEvent** 



-------

.. _no-29091:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-29092:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-29093:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-29094:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-29095:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-29096:

**MouseEvent** 



-------

.. _no-29097:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-29098:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-29099:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-29100:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-29101:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-29102:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-29103:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-29104:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-29105:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-29106:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-29107:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-29108:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-29109:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-29110:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-29111:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-29112:

**Move** 

Occurs when the control's position changes.



-------

.. _no-29113:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-29114:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-29115:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-29116:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-29117:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------

.. _no-29118:

**ValueChanged** 

Occurs when the control's value has changed, whether
programmatically or interactively.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-29119>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-29120>`             Instantiate object as a child of self.
:ref:`afterInit <no-29121>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-29122>`          
:ref:`afterSetProperties <no-29123>`    
:ref:`autoBindEvents <no-29124>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-29125>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-29126>`   
:ref:`bindEvent <no-29127>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-29128>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-29129>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-29130>`          Makes this object topmost
:ref:`clear <no-29131>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-29132>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-29133>`  Given a position relative to this control, return a position relative
:ref:`copy <no-29134>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-29135>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-29136>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-29137>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-29138>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-29139>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-29140>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-29141>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-29142>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-29143>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-29144>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-29145>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-29146>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-29147>`              Draws text on the object at the specified position
:ref:`endHover <no-29148>`              
:ref:`fitToSizer <no-29149>`            Resize the control to fit the size required by its sizer.
:ref:`flushValue <no-29150>`            Save any changes to the underlying source field. First check to make sure
:ref:`fontZoomIn <no-29151>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-29152>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-29153>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-29154>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-29155>`       Return the fully qualified name of the object.
:ref:`getBlankValue <no-29156>`         
:ref:`getCaptureBitmap <no-29157>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-29158>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-29159>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-29160>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-29161>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-29162>`         Returns a dictionary of property name/value pairs.
:ref:`getShortDataType <no-29163>`      
:ref:`getSizerProp <no-29164>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-29165>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-29166>`                  Make the object invisible.
:ref:`initEvents <no-29167>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-29168>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-29169>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-29170>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-29171>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-29172>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-29173>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-29174>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-29175>`               
:ref:`paste <no-29176>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-29177>`           
:ref:`processDroppedFiles <no-29178>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-29179>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-29180>`            Raise the passed Dabo event.
:ref:`reCreate <no-29181>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-29182>`              Recreate the object.
:ref:`redraw <no-29183>`                Called when the object is (re)drawn.
:ref:`refresh <no-29184>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-29185>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-29186>`               Destroys the object.
:ref:`removeDrawnObject <no-29187>`     
:ref:`restoreValue <no-29188>`          Set the control's value to the value in dApp's user settings table.
:ref:`saveValue <no-29189>`             Save control's value to dApp's user settings table.
:ref:`select <no-29190>`                Select all text from <position> for <length> or end of string.
:ref:`selectAll <no-29191>`             Select all text in the control.
:ref:`selectNone <no-29192>`            Select no text in the control.
:ref:`sendToBack <no-29193>`            Places this object behind all others.
:ref:`setAll <no-29194>`                Set all child object properties to the passed value.
:ref:`setFocus <no-29195>`              Sets focus to the object.
:ref:`setPositionInSizer <no-29196>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-29197>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-29198>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-29199>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-29200>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-29201>`                  Make the object visible.
:ref:`showContainingPage <no-29202>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-29203>`       Display a context menu (popup) at the specified position.
:ref:`super <no-29204>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-29205>`           Remove a previously registered event binding.
:ref:`unbindKey <no-29206>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-29207>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-29208>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-29209>`                Update control's value to match the current value from the source.

======================================= ========================


Methods
=======

.. _no-29156:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.getBlankValue(self)



-------


Methods - inherited
=====================

.. _no-29119:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29120:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-29121:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29122:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29123:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29124:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.autoBindEvents(self, force=True)
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

.. _no-29125:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29126:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29127:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-29128:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-29129:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-29130:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29131:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29132:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29133:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29134:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29135:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29136:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29137:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29138:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-29139:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29140:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29141:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29142:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29143:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29144:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29145:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29146:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29147:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29148:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29149:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29150:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.flushValue(self)
   :noindex:


   
   Save any changes to the underlying source field. First check to make sure
   that any changes are validated.
   


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-29151:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29152:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29153:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29154:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29155:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29157:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29158:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29159:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29160:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29161:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29162:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-29163:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.getShortDataType(self, value)
   :noindex:



Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-29164:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29165:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29166:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29167:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29168:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29169:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29170:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29171:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.lockDisplay(self)
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

.. _no-29172:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29173:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29174:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29175:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29176:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29177:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29178:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29179:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29180:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29181:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-29182:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29183:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29184:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29185:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29186:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29187:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29188:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.restoreValue(self)
   :noindex:


   Set the control's value to the value in dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-29189:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.saveValue(self)
   :noindex:


   Save control's value to dApp's user settings table.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------

.. _no-29190:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.select(self, position, length)
   :noindex:


   Select all text from <position> for <length> or end of string.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-29191:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.selectAll(self)
   :noindex:


   Select all text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-29192:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.selectNone(self)
   :noindex:


   Select no text in the control.


Inherited from: :ref:`dabo.ui.uiwx.dDataControlMixin.dDataControlMixin`

-------

.. _no-29193:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29194:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-29195:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29196:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29197:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-29198:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-29199:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29200:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29201:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29202:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29203:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29204:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-29205:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-29206:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29207:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29208:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-29209:

.. function:: dabo.ui.uiwx.dCheckBox.dCheckBox.update(self)
   :noindex:


   Update control's value to match the current value from the source.


Inherited from: :ref:`dabo.ui.dDataControlMixinBase.dDataControlMixinBase`

-------


|
