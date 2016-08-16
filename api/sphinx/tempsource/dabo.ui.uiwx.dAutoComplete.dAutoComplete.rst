
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dAutoComplete

.. _dabo.ui.uiwx.dAutoComplete.dAutoComplete:

====================================================
|doc_title|  **dAutoComplete.dAutoComplete** - class
====================================================


Creates a text box with a dropdown list that has the ability to filter
multiple records or choices in the list based on entered text.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dAutoComplete**

.. inheritance-diagram:: dAutoComplete


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dAutoComplete.TextCtrlAutoComplete`
* :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dAutoComplete.dAutoComplete

   .. automethod:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.__init__

|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`Application <no-24062>`            Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-24063>`              Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-24064>`              The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-24065>`            Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-24066>`            Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-24067>`        Style of line for the border drawn around the control.
:ref:`BorderStyle <no-24068>`            Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-24069>`            Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-24070>`                 The position of the bottom side of the object. This is a
:ref:`Caption <no-24071>`                The caption of the object. (str)
:ref:`Children <no-24072>`               Returns a list of object references to the children of
:ref:`Choices <no-24073>`                The choices to put in the dropdown list when no DataSource or
:ref:`Class <no-24074>`                  The class the object is based on. Read-only.  (class)
:ref:`ColNames <no-24075>`               The names used to label columns.  (list of strs)
:ref:`ControllingSizer <no-24076>`       Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-24077>`   Reference to the sizer item that control's this control's layout.
:ref:`DataFields <no-24078>`             The fields from the data set to display in the list.  (list of strs)
:ref:`DataSet <no-24079>`                The set of data displayed in the list.  (set of dicts)
:ref:`DataSource <no-24080>`             The source of the data to display in the list.  (str)
:ref:`DroppedFileHandler <no-24081>`     Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-24082>`     Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-24083>`       Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-24084>`     Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-24085>` Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-24086>`     Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-24087>`     Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-24088>`         Dynamically determine the value of the Caption property.
:ref:`DynamicEnabled <no-24089>`         Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-24090>`            Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-24091>`        Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-24092>`        Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-24093>`      Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-24094>`        Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-24095>`   Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-24096>`       Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-24097>`          Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-24098>`            Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-24099>`    Dynamically determine the value of the MousePointer property.
:ref:`DynamicPosition <no-24100>`        Dynamically determine the value of the Position property.
:ref:`DynamicSize <no-24101>`            Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-24102>`      Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-24103>`             Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-24104>`     Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-24105>`             Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-24106>`    Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-24107>`         Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-24108>`           Dynamically determine the value of the Width property.
:ref:`Enabled <no-24109>`                Specifies whether the object and children can get user input. (bool)
:ref:`FetchField <no-24110>`             The field or column displayed in the text box when a value is
:ref:`Font <no-24111>`                   Specifies font object for this control. (dFont)
:ref:`FontBold <no-24112>`               Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-24113>`        Human-readable description of the current font settings. (str)
:ref:`FontFace <no-24114>`               Specifies the font face. (str)
:ref:`FontInfo <no-24115>`               Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-24116>`             Specifies whether font is italicized. (bool)
:ref:`FontSize <no-24117>`               Specifies the point size of the font. (int)
:ref:`FontUnderline <no-24118>`          Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-24119>`              Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-24120>`                   Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-24121>`                 Specifies the height of the object. (int)
:ref:`HelpContextText <no-24122>`        Specifies the context-sensitive help text associated with this
:ref:`Hover <no-24123>`                  When True, Mouse Enter events fire the onHover method, and
:ref:`Left <no-24124>`                   Specifies the left position of the object. (int)
:ref:`LogEvents <no-24125>`              Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-24126>`          Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-24127>`            Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-24128>`           Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-24129>`          Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-24130>`            Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-24131>`           Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-24132>`           Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`Name <no-24133>`                   Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-24134>`               Specifies the base name of the object.
:ref:`Parent <no-24135>`                 The containing object. (obj)
:ref:`Position <no-24136>`               The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-24137>`      Reference to the Preference Management object  (dPref)
:ref:`RegID <no-24138>`                  A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-24139>`                  The position of the right side of the object. This is a
:ref:`SearchField <no-24140>`            The field or column used to compare with user-entered text.  (str or int)
:ref:`Size <no-24141>`                   The size of the object. (tuple)
:ref:`Sizer <no-24142>`                  The sizer for the object.
:ref:`StatusText <no-24143>`             Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-24144>`                Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-24145>`                    A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-24146>`            Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-24147>`                    The top position of the object. (int)
:ref:`Transparency <no-24148>`           Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-24149>`      Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`Visible <no-24150>`                Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-24151>`        Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-24152>`                  The width of the object. (int)
:ref:`WindowHandle <no-24153>`           The platform-specific handle for the window. Read-only. (long)

======================================== ========================


Properties
==========

.. _no-24073:

**Choices** 

The choices to put in the dropdown list when no DataSource or
    DataSet is provided.  (list)

    This list can consist of strings (one-dimensional) or sublists of
    strings (two-dimensional) and the number of columns in the list
    will be set accordingly. All sublists must be of the same length.

    If DataSource or DataSet are defined, this field becomes read-only
    and returns the choices currently in the list.



-------

.. _no-24075:

**ColNames** 

The names used to label columns.  (list of strs)

    If this list is of a different length than the number of columns,
    blank column names will be added or extra column names ignored as
    appropriate.



-------

.. _no-24078:

**DataFields** 

The fields from the data set to display in the list.  (list of strs)

    Fields will be displayed in order of this list. If not set, all
    fields in the data set will be displayed in default order.



-------

.. _no-24079:

**DataSet** 

The set of data displayed in the list.  (set of dicts)

    When DataSource isn't defined, setting DataSet to a set of dicts,
    such as what you get from calling dBizobj.getDataSet(), will
    define the source of the data that the list displays.

    If DataSource is defined, DataSet is read-only and returns the data set
    from the bizobj.



-------

.. _no-24080:

**DataSource** 

The source of the data to display in the list.  (str)

    This corresponds to a bizobj with a matching DataSource on the form,
    and setting this makes it impossible to set DataSet.



-------

.. _no-24110:

**FetchField** 

The field or column displayed in the text box when a value is
    selected from the list. (str or int)

    When given a field name, selecting an entry in the dropdown list
    will diplay the corresponding field's value for that entry in the
    text box. If an int is provided, columns are chosen by index
    (starting with 0). If not set, the field specified by SearchField
    will be used.



-------

.. _no-24140:

**SearchField** 

The field or column used to compare with user-entered text.  (str or int)

    When given a field name, strings in the text box will be matched
    with the corresponding field's value. If an int is provided,
    columns are chosen by index (starting with 0). If not set, the
    search will be done on the leftmost field (index 0).



-------


Properties - inherited
========================

.. _no-24062:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24063:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24064:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24065:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24066:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24067:

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

.. _no-24068:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24069:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24070:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24071:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24072:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-24074:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24076:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24077:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24081:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24082:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24083:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24084:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24085:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24086:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24087:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24088:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24089:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24090:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24091:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24092:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24093:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24094:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24095:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24096:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24097:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24098:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24099:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24100:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24101:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24102:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24103:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24104:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24105:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24106:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24107:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24108:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24109:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-24111:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-24112:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24113:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24114:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24115:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24116:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24117:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24118:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24119:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24120:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24121:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24122:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24123:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24124:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24125:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24126:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24127:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24128:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24129:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24130:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24131:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24132:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24133:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-24134:

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

.. _no-24135:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-24136:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-24137:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24138:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24139:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24141:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-24142:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-24143:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24144:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-24145:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24146:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24147:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24148:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24149:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24150:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24151:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24152:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24153:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-24154>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-24155>`                 Occurs after the control or form is created.
:ref:`Destroy <no-24156>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-24157>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-24158>`               Occurs when the control gets the focus.
:ref:`Idle <no-24159>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-24160>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-24161>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-24162>`               
:ref:`KeyUp <no-24163>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-24164>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-24165>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-24166>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-24167>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-24168>`             
:ref:`MouseLeave <no-24169>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-24170>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-24171>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-24172>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-24173>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-24174>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-24175>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-24176>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-24177>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-24178>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-24179>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-24180>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-24181>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-24182>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-24183>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-24184>`                   Occurs when the control's position changes.
:ref:`Paint <no-24185>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-24186>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-24187>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-24188>`            Occurs when a drag operation ends in a tree.
:ref:`Update <no-24189>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-24154:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-24155:

**Create** 

Occurs after the control or form is created.



-------

.. _no-24156:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-24157:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-24158:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-24159:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-24160:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-24161:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-24162:

**KeyEvent** 



-------

.. _no-24163:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-24164:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-24165:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-24166:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-24167:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-24168:

**MouseEvent** 



-------

.. _no-24169:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-24170:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-24171:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-24172:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-24173:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-24174:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-24175:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-24176:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-24177:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-24178:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-24179:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-24180:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-24181:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-24182:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-24183:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-24184:

**Move** 

Occurs when the control's position changes.



-------

.. _no-24185:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-24186:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-24187:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-24188:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-24189:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-24190>`   Translates a position value for a control to absolute screen position.
:ref:`addObject <no-24191>`             Instantiate object as a child of self.
:ref:`afterInit <no-24192>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-24193>`          
:ref:`afterSetProperties <no-24194>`    
:ref:`autoBindEvents <no-24195>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-24196>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-24197>`   
:ref:`bindEvent <no-24198>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-24199>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-24200>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-24201>`          Makes this object topmost
:ref:`clear <no-24202>`                 Clears the background of custom-drawn objects.
:ref:`clone <no-24203>`                 Create another object just like the passed object. It assumes that the
:ref:`containerCoordinates <no-24204>`  Given a position relative to this control, return a position relative
:ref:`copy <no-24205>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-24206>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-24207>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-24208>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-24209>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-24210>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-24211>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-24212>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-24213>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-24214>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-24215>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-24216>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-24217>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-24218>`              Draws text on the object at the specified position
:ref:`endHover <no-24219>`              
:ref:`fillDynamicChoices <no-24220>`    The default entry callback function: takes the user-entered text from
:ref:`fitToSizer <no-24221>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-24222>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-24223>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-24224>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-24225>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-24226>`       Return the fully qualified name of the object.
:ref:`getBizobj <no-24227>`             
:ref:`getCaptureBitmap <no-24228>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getContainingPage <no-24229>`     Return the dPage or WizardPage that contains self.
:ref:`getDisplayLocker <no-24230>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-24231>`      Returns the current mouse position on the entire screen
:ref:`getPositionInSizer <no-24232>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-24233>`         Returns a dictionary of property name/value pairs.
:ref:`getSizerProp <no-24234>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-24235>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-24236>`                  Make the object invisible.
:ref:`initEvents <no-24237>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-24238>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-24239>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-24240>`           Call the given function on this object and all of its Children. If
:ref:`listFromDS <no-24241>`            Takes a data set from the DataSource bizobj or the DataSet property
:ref:`lockDisplay <no-24242>`           Locks the visual updates to the control.
:ref:`moveTabOrderAfter <no-24243>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-24244>`    Moves this object's tab order before the passed obj.
:ref:`objectCoordinates <no-24245>`     Given a position relative to the form, return a position relative
:ref:`onClickToggleDown <no-24246>`     
:ref:`onClickToggleUp <no-24247>`       
:ref:`onControlChanged <no-24248>`      
:ref:`onEnteredText <no-24249>`         
:ref:`onHover <no-24250>`               
:ref:`onKeyDown <no-24251>`             This prevents dEvents from being passed to autocomplete's onKeyDown
:ref:`onKeyUp <no-24252>`               
:ref:`onListClick <no-24253>`           
:ref:`onListColClick <no-24254>`        
:ref:`onListDClick <no-24255>`          
:ref:`onListItemSelected <no-24256>`    
:ref:`paste <no-24257>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-24258>`           
:ref:`processDroppedFiles <no-24259>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-24260>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-24261>`            Raise the passed Dabo event.
:ref:`reCreate <no-24262>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-24263>`              Recreate the object.
:ref:`redraw <no-24264>`                Called when the object is (re)drawn.
:ref:`refresh <no-24265>`               Repaints this control and all contained objects.
:ref:`relativeCoordinates <no-24266>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-24267>`               Destroys the object.
:ref:`removeDrawnObject <no-24268>`     
:ref:`sendToBack <no-24269>`            Places this object behind all others.
:ref:`setAll <no-24270>`                Set all child object properties to the passed value.
:ref:`setFocus <no-24271>`              Sets focus to the object.
:ref:`setPositionInSizer <no-24272>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-24273>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-24274>` Sets a group of properties on the object all at once. This
:ref:`setSizerProp <no-24275>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-24276>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-24277>`                  Make the object visible.
:ref:`showContainingPage <no-24278>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-24279>`       Display a context menu (popup) at the specified position.
:ref:`super <no-24280>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-24281>`           Remove a previously registered event binding.
:ref:`unbindKey <no-24282>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-24283>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-24284>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-24285>`                Call this when your datasource or dataset has changed to get the list showing
:ref:`write <no-24286>`                 write(self, String text)

======================================= ========================


Methods
=======

.. _no-24220:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.fillDynamicChoices(self)

   
   The default entry callback function: takes the user-entered text from
   the text box and updates the dropdown list to include only entries in
   which the value of the search field starts with the given string.i
   



-------

.. _no-24227:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.getBizobj(self)



-------

.. _no-24241:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.listFromDS(self)

   
   Takes a data set from the DataSource bizobj or the DataSet property
   directly and formats it as a choice list for autocomplete, using field
   names as column headers by default or the ColNames property as column
   headers if defined.
   



-------

.. _no-24251:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.onKeyDown(self, evt)

   This prevents dEvents from being passed to autocomplete's onKeyDown



-------

.. _no-24252:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.onKeyUp(self, evt)



-------

.. _no-24285:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.update(self)

   
   Call this when your datasource or dataset has changed to get the list showing
   the proper number of rows with current data.
   



-------


Methods - inherited
=====================

.. _no-24190:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24191:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-24192:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24193:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24194:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24195:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.autoBindEvents(self, force=True)
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

.. _no-24196:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24197:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24198:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-24199:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-24200:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-24201:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24202:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.clear(self)
   :noindex:


   Clears the background of custom-drawn objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24203:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24204:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24205:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24206:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24207:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24208:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24209:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-24210:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24211:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24212:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24213:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24214:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24215:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24216:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24217:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24218:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24219:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24221:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24222:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24223:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24224:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24225:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24226:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24228:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24229:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24230:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24231:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24232:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24233:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-24234:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24235:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24236:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24237:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24238:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24239:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24240:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24242:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.lockDisplay(self)
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

.. _no-24243:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24244:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24245:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24246:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.onClickToggleDown(self, event)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dAutoComplete.TextCtrlAutoComplete`

-------

.. _no-24247:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.onClickToggleUp(self, event)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dAutoComplete.TextCtrlAutoComplete`

-------

.. _no-24248:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.onControlChanged(self, event)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dAutoComplete.TextCtrlAutoComplete`

-------

.. _no-24249:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.onEnteredText(self, event)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dAutoComplete.TextCtrlAutoComplete`

-------

.. _no-24250:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24253:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.onListClick(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dAutoComplete.TextCtrlAutoComplete`

-------

.. _no-24254:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.onListColClick(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dAutoComplete.TextCtrlAutoComplete`

-------

.. _no-24255:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.onListDClick(self, evt)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dAutoComplete.TextCtrlAutoComplete`

-------

.. _no-24256:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.onListItemSelected(self, event)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dAutoComplete.TextCtrlAutoComplete`

-------

.. _no-24257:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24258:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24259:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24260:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24261:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24262:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-24263:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24264:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24265:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24266:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24267:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24268:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24269:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24270:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-24271:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24272:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24273:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-24274:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-24275:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24276:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24277:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24278:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24279:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24280:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-24281:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-24282:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24283:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24284:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-24286:

.. function:: dabo.ui.uiwx.dAutoComplete.dAutoComplete.write(*args, \**kwargs)
   :noindex:


   write(self, String text)


Inherited from: 'wx._controls.TextCtrl - can not provide a link

-------


|
