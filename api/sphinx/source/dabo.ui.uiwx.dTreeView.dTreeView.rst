
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dTreeView

.. _dabo.ui.uiwx.dTreeView.dTreeView:

============================================
|doc_title|  **dTreeView.dTreeView** - class
============================================

Creates a treeview, which allows display of hierarchical data.



|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dTreeView**

.. inheritance-diagram:: dTreeView


|supclasses| Known Superclasses
===============================

* :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`



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



   * - .. image:: _static/macWidgets/dTreeView.png
          :scale: 75 %
          :target: _static/macWidgets/dTreeView.png
          :alt: dTreeView



     - .. image:: _static/winWidgets/dTreeView.png
          :scale: 75 %
          :target: _static/winWidgets/dTreeView.png
          :alt: dTreeView



     - .. image:: _static/nixWidgets/dTreeView.png
          :scale: 75 %
          :target: _static/nixWidgets/dTreeView.png
          :alt: dTreeView


|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dTreeView.dTreeView

   .. automethod:: dabo.ui.uiwx.dTreeView.dTreeView.__init__

|method_summary| Properties Summary
===================================


========================================== ========================
:ref:`Application <no-26136>`              Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-26137>`                Specifies the background color of the object. (str, 3-tuple, or wx.Colour)
:ref:`BaseClass <no-26138>`                The base Dabo class of the object. Read-only.  (class)
:ref:`BaseNodes <no-26139>`                Returns the root node if ShowRootNode is True; otherwise,
:ref:`BasePrefKey <no-26140>`              Base key used when saving/restoring preferences  (str)
:ref:`BorderColor <no-26141>`              Specifies the color of the border drawn around the control, if any.
:ref:`BorderLineStyle <no-26142>`          Style of line for the border drawn around the control.
:ref:`BorderStyle <no-26143>`              Specifies the type of border for this window. (str).
:ref:`BorderWidth <no-26144>`              Width of the border drawn around the control, if any. (int)
:ref:`Bottom <no-26145>`                   The position of the bottom side of the object. This is a
:ref:`Caption <no-26146>`                  The caption of the object. (str)
:ref:`Children <no-26147>`                 Returns a list of object references to the children of
:ref:`Class <no-26148>`                    The class the object is based on. Read-only.  (class)
:ref:`ControllingSizer <no-26149>`         Reference to the sizer that controls this control's layout.  (dSizer)
:ref:`ControllingSizerItem <no-26150>`     Reference to the sizer item that control's this control's layout.
:ref:`DroppedFileHandler <no-26151>`       Reference to the object that will handle files dropped on this control.
:ref:`DroppedTextHandler <no-26152>`       Reference to the object that will handle text dropped on this control.
:ref:`DynamicBackColor <no-26153>`         Dynamically determine the value of the BackColor property.
:ref:`DynamicBorderColor <no-26154>`       Dynamically determine the value of the BorderColor property.
:ref:`DynamicBorderLineStyle <no-26155>`   Dynamically determine the value of the BorderLineStyle property.
:ref:`DynamicBorderStyle <no-26156>`       Dynamically determine the value of the BorderStyle property.
:ref:`DynamicBorderWidth <no-26157>`       Dynamically determine the value of the BorderWidth property.
:ref:`DynamicCaption <no-26158>`           Dynamically determine the value of the Caption property.
:ref:`DynamicEditable <no-26159>`          Dynamically determine the value of the Editable property.
:ref:`DynamicEnabled <no-26160>`           Dynamically determine the value of the Enabled property.
:ref:`DynamicFont <no-26161>`              Dynamically determine the value of the Font property.
:ref:`DynamicFontBold <no-26162>`          Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-26163>`          Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-26164>`        Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-26165>`          Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-26166>`     Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-26167>`         Dynamically determine the value of the ForeColor property.
:ref:`DynamicHeight <no-26168>`            Dynamically determine the value of the Height property.
:ref:`DynamicLeft <no-26169>`              Dynamically determine the value of the Left property.
:ref:`DynamicMousePointer <no-26170>`      Dynamically determine the value of the MousePointer property.
:ref:`DynamicMultipleSelect <no-26171>`    Dynamically determine the value of the MultipleSelect property.
:ref:`DynamicPosition <no-26172>`          Dynamically determine the value of the Position property.
:ref:`DynamicSelection <no-26173>`         Dynamically determine the value of the Selection property.
:ref:`DynamicShowButtons <no-26174>`       Dynamically determine the value of the ShowButtons property.
:ref:`DynamicShowLines <no-26175>`         Dynamically determine the value of the ShowLines property.
:ref:`DynamicShowRootNode <no-26176>`      Dynamically determine the value of the ShowRootNode property.
:ref:`DynamicShowRootNodeLines <no-26177>` Dynamically determine the value of the ShowRootNodeLines property.
:ref:`DynamicSize <no-26178>`              Dynamically determine the value of the Size property.
:ref:`DynamicStatusText <no-26179>`        Dynamically determine the value of the StatusText property.
:ref:`DynamicTag <no-26180>`               Dynamically determine the value of the Tag property.
:ref:`DynamicToolTipText <no-26181>`       Dynamically determine the value of the ToolTipText property.
:ref:`DynamicTop <no-26182>`               Dynamically determine the value of the Top property.
:ref:`DynamicTransparency <no-26183>`      Dynamically determine the value of the Transparency property.
:ref:`DynamicVisible <no-26184>`           Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-26185>`             Dynamically determine the value of the Width property.
:ref:`Editable <no-26186>`                 Specifies whether the tree labels can be edited by the user.
:ref:`Enabled <no-26187>`                  Specifies whether the object and children can get user input. (bool)
:ref:`Font <no-26188>`                     Specifies font object for this control. (dFont)
:ref:`FontBold <no-26189>`                 Specifies if the font is bold-faced. (bool)
:ref:`FontDescription <no-26190>`          Human-readable description of the current font settings. (str)
:ref:`FontFace <no-26191>`                 Specifies the font face. (str)
:ref:`FontInfo <no-26192>`                 Specifies the platform-native font info string. Read-only. (str)
:ref:`FontItalic <no-26193>`               Specifies whether font is italicized. (bool)
:ref:`FontSize <no-26194>`                 Specifies the point size of the font. (int)
:ref:`FontUnderline <no-26195>`            Specifies whether text is underlined. (bool)
:ref:`ForeColor <no-26196>`                Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)
:ref:`Form <no-26197>`                     Object reference to the dForm containing the object. Read-only. (dForm).
:ref:`Height <no-26198>`                   Specifies the height of the object. (int)
:ref:`HelpContextText <no-26199>`          Specifies the context-sensitive help text associated with this
:ref:`Hover <no-26200>`                    When True, Mouse Enter events fire the onHover method, and
:ref:`ImageSize <no-26201>`                Size of images added to the tree. Default=(15, 15)  (2-tuple of int)
:ref:`Left <no-26202>`                     Specifies the left position of the object. (int)
:ref:`LogEvents <no-26203>`                Specifies which events to log.  (list of strings)
:ref:`MaximumHeight <no-26204>`            Maximum allowable height for the control in pixels.  (int)
:ref:`MaximumSize <no-26205>`              Maximum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MaximumWidth <no-26206>`             Maximum allowable width for the control in pixels.  (int)
:ref:`MinimumHeight <no-26207>`            Minimum allowable height for the control in pixels.  (int)
:ref:`MinimumSize <no-26208>`              Minimum allowable size for the control in pixels.  (2-tuple of int)
:ref:`MinimumWidth <no-26209>`             Minimum allowable width for the control in pixels.  (int)
:ref:`MousePointer <no-26210>`             Specifies the shape of the mouse pointer when it enters this window. (obj)
:ref:`MultipleSelect <no-26211>`           Specifies whether more than one node may be selected at once.
:ref:`Name <no-26212>`                     Specifies the name of the object, which must be unique among siblings.
:ref:`NameBase <no-26213>`                 Specifies the base name of the object.
:ref:`NodeClass <no-26214>`                Class to use when creating nodes  (dNode)
:ref:`Parent <no-26215>`                   The containing object. (obj)
:ref:`Position <no-26216>`                 The (x,y) position of the object. (tuple)
:ref:`PreferenceManager <no-26217>`        Reference to the Preference Management object  (dPref)
:ref:`RegID <no-26218>`                    A unique identifier used for referencing by other objects. (str)
:ref:`Right <no-26219>`                    The position of the right side of the object. This is a
:ref:`Selection <no-26220>`                Specifies which node or nodes are selected.
:ref:`ShowButtons <no-26221>`              Specifies whether +/- indicators are show at the left of parent nodes.
:ref:`ShowLines <no-26222>`                Specifies whether lines are drawn between nodes.  (bool)
:ref:`ShowRootNode <no-26223>`             Specifies whether the root node is included in the treeview.
:ref:`ShowRootNodeLines <no-26224>`        Specifies whether vertical lines are shown between root siblings.
:ref:`Size <no-26225>`                     The size of the object. (tuple)
:ref:`Sizer <no-26226>`                    The sizer for the object.
:ref:`StatusText <no-26227>`               Specifies the text that displays in the form's status bar, if any.
:ref:`TabStop <no-26228>`                  Specifies whether this control can receive focus from keyboard navigation.
:ref:`Tag <no-26229>`                      A property that user code can safely use for specific purposes.
:ref:`ToolTipText <no-26230>`              Specifies the tooltip text associated with this window. (str)
:ref:`Top <no-26231>`                      The top position of the object. (int)
:ref:`Transparency <no-26232>`             Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
:ref:`TransparencyDelay <no-26233>`        Time in seconds to change transparency. Set it to zero to see instant changes.
:ref:`UseNodeToolTips <no-26234>`          When True, the ToolTipText displayed is taken from the node.
:ref:`Visible <no-26235>`                  Specifies whether the object is visible at runtime.  (bool)
:ref:`VisibleOnScreen <no-26236>`          Specifies whether the object is physically visible at runtime.  (bool)
:ref:`Width <no-26237>`                    The width of the object. (int)
:ref:`WindowHandle <no-26238>`             The platform-specific handle for the window. Read-only. (long)

========================================== ========================


Properties
==========

.. _no-26139:

**BaseNodes** 

Returns the root node if ShowRootNode is True; otherwise,
    returns all the nodes who are not children of other nodes
    (read-only) (list of nodes)



-------

.. _no-26159:

**DynamicEditable** 

Dynamically determine the value of the Editable property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Editable property. If DynamicEditable is set to None (the default), Editable
will not be dynamically evaluated.



-------

.. _no-26171:

**DynamicMultipleSelect** 

Dynamically determine the value of the MultipleSelect property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MultipleSelect property. If DynamicMultipleSelect is set to None (the default), MultipleSelect
will not be dynamically evaluated.



-------

.. _no-26173:

**DynamicSelection** 

Dynamically determine the value of the Selection property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Selection property. If DynamicSelection is set to None (the default), Selection
will not be dynamically evaluated.



-------

.. _no-26174:

**DynamicShowButtons** 

Dynamically determine the value of the ShowButtons property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowButtons property. If DynamicShowButtons is set to None (the default), ShowButtons
will not be dynamically evaluated.



-------

.. _no-26175:

**DynamicShowLines** 

Dynamically determine the value of the ShowLines property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowLines property. If DynamicShowLines is set to None (the default), ShowLines
will not be dynamically evaluated.



-------

.. _no-26176:

**DynamicShowRootNode** 

Dynamically determine the value of the ShowRootNode property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowRootNode property. If DynamicShowRootNode is set to None (the default), ShowRootNode
will not be dynamically evaluated.



-------

.. _no-26177:

**DynamicShowRootNodeLines** 

Dynamically determine the value of the ShowRootNodeLines property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ShowRootNodeLines property. If DynamicShowRootNodeLines is set to None (the default), ShowRootNodeLines
will not be dynamically evaluated.



-------

.. _no-26186:

**Editable** 

Specifies whether the tree labels can be edited by the user.



-------

.. _no-26201:

**ImageSize** 

Size of images added to the tree. Default=(15, 15)  (2-tuple of int)



-------

.. _no-26211:

**MultipleSelect** 

Specifies whether more than one node may be selected at once.



-------

.. _no-26214:

**NodeClass** 

Class to use when creating nodes  (dNode)



-------

.. _no-26221:

**ShowButtons** 

Specifies whether +/- indicators are show at the left of parent nodes.



-------

.. _no-26222:

**ShowLines** 

Specifies whether lines are drawn between nodes.  (bool)



-------

.. _no-26223:

**ShowRootNode** 

Specifies whether the root node is included in the treeview.

There can be only one root node, so if you want several root nodes you can
fake it by setting ShowRootNode to False. Now, your top child nodes have
the visual indication of being sibling root nodes.



-------

.. _no-26224:

**ShowRootNodeLines** 

Specifies whether vertical lines are shown between root siblings.



-------

.. _no-26234:

**UseNodeToolTips** 

When True, the ToolTipText displayed is taken from the node.
    Default=False  (bool)



-------


Properties - inherited
========================

.. _no-26136:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26137:

**BackColor** 

Specifies the background color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26138:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26140:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26141:

**BorderColor** 

Specifies the color of the border drawn around the control, if any.

    Default='black'  (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26142:

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

.. _no-26143:

**BorderStyle** 

Specifies the type of border for this window. (str).

        Possible choices are:
            "None"
            "Simple"
            "Sunken"
            "Raised"
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26144:

**BorderWidth** 

Width of the border drawn around the control, if any. (int)

        Default=0 (no border)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26145:

**Bottom** 

The position of the bottom side of the object. This is a
    convenience property, and is equivalent to setting the Top property
    to this value minus the Height of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-26146:

**Caption** 

The caption of the object. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26147:

**Children** 

Returns a list of object references to the children of
    this object. Only applies to containers. Children will be None for
    non-containers.  (list or None)
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-26148:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26149:

**ControllingSizer** 

Reference to the sizer that controls this control's layout.  (dSizer)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26150:

**ControllingSizerItem** 

Reference to the sizer item that control's this control's layout.

        This is useful for getting information about how the item is being
        sized, and for changing those settings.  (SizerItem)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26151:

**DroppedFileHandler** 

Reference to the object that will handle files dropped on this control.
    When files are dropped, a list of them will be passed to this object's
    'processDroppedFiles()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26152:

**DroppedTextHandler** 

Reference to the object that will handle text dropped on this control.
    When text is dropped, that text will be passed to this object's
    'processDroppedText()' method. Default=None  (object or None)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26153:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26154:

**DynamicBorderColor** 

Dynamically determine the value of the BorderColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderColor property. If DynamicBorderColor is set to None (the default), BorderColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26155:

**DynamicBorderLineStyle** 

Dynamically determine the value of the BorderLineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderLineStyle property. If DynamicBorderLineStyle is set to None (the default), BorderLineStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26156:

**DynamicBorderStyle** 

Dynamically determine the value of the BorderStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderStyle property. If DynamicBorderStyle is set to None (the default), BorderStyle
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26157:

**DynamicBorderWidth** 

Dynamically determine the value of the BorderWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BorderWidth property. If DynamicBorderWidth is set to None (the default), BorderWidth
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26158:

**DynamicCaption** 

Dynamically determine the value of the Caption property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Caption property. If DynamicCaption is set to None (the default), Caption
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26160:

**DynamicEnabled** 

Dynamically determine the value of the Enabled property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Enabled property. If DynamicEnabled is set to None (the default), Enabled
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26161:

**DynamicFont** 

Dynamically determine the value of the Font property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Font property. If DynamicFont is set to None (the default), Font
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26162:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26163:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26164:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26165:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26166:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26167:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26168:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26169:

**DynamicLeft** 

Dynamically determine the value of the Left property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Left property. If DynamicLeft is set to None (the default), Left
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26170:

**DynamicMousePointer** 

Dynamically determine the value of the MousePointer property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
MousePointer property. If DynamicMousePointer is set to None (the default), MousePointer
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26172:

**DynamicPosition** 

Dynamically determine the value of the Position property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Position property. If DynamicPosition is set to None (the default), Position
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26178:

**DynamicSize** 

Dynamically determine the value of the Size property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Size property. If DynamicSize is set to None (the default), Size
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26179:

**DynamicStatusText** 

Dynamically determine the value of the StatusText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
StatusText property. If DynamicStatusText is set to None (the default), StatusText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26180:

**DynamicTag** 

Dynamically determine the value of the Tag property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Tag property. If DynamicTag is set to None (the default), Tag
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26181:

**DynamicToolTipText** 

Dynamically determine the value of the ToolTipText property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ToolTipText property. If DynamicToolTipText is set to None (the default), ToolTipText
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26182:

**DynamicTop** 

Dynamically determine the value of the Top property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Top property. If DynamicTop is set to None (the default), Top
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26183:

**DynamicTransparency** 

Dynamically determine the value of the Transparency property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparency property. If DynamicTransparency is set to None (the default), Transparency
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26184:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26185:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26187:

**Enabled** 

Specifies whether the object and children can get user input. (bool)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-26188:

**Font** 

Specifies font object for this control. (dFont)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-26189:

**FontBold** 

Specifies if the font is bold-faced. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26190:

**FontDescription** 

Human-readable description of the current font settings. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26191:

**FontFace** 

Specifies the font face. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26192:

**FontInfo** 

Specifies the platform-native font info string. Read-only. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26193:

**FontItalic** 

Specifies whether font is italicized. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26194:

**FontSize** 

Specifies the point size of the font. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26195:

**FontUnderline** 

Specifies whether text is underlined. (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26196:

**ForeColor** 

Specifies the foreground color of the object. (str, 3-tuple, or wx.Colour)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26197:

**Form** 

Object reference to the dForm containing the object. Read-only. (dForm).


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-26198:

**Height** 

Specifies the height of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26199:

**HelpContextText** 

Specifies the context-sensitive help text associated with this
        window. (str)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26200:

**Hover** 

When True, Mouse Enter events fire the onHover method, and
    MouseLeave events fire the endHover method  (bool)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26202:

**Left** 

Specifies the left position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26203:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26204:

**MaximumHeight** 

Maximum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26205:

**MaximumSize** 

Maximum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26206:

**MaximumWidth** 

Maximum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26207:

**MinimumHeight** 

Minimum allowable height for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26208:

**MinimumSize** 

Minimum allowable size for the control in pixels.  (2-tuple of int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26209:

**MinimumWidth** 

Minimum allowable width for the control in pixels.  (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26210:

**MousePointer** 

Specifies the shape of the mouse pointer when it enters this window. (obj)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26212:

**Name** 

Specifies the name of the object, which must be unique among siblings.

    If the specified name isn't unique, an exception will be raised. See also
    NameBase, which let's you set a base name and Dabo will automatically append
    integers to make it unique.
    


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-26213:

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

.. _no-26215:

**Parent** 

The containing object. (obj)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-26216:

**Position** 

The (x,y) position of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-26217:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26218:

**RegID** 

A unique identifier used for referencing by other objects. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26219:

**Right** 

The position of the right side of the object. This is a
    convenience property, and is equivalent to setting the Left property
    to this value minus the Width of the control.  (int)


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-26220:

**Selection** 

Specifies which node or nodes are selected.

If MultipleSelect is False, the currently selected node is specified. If MultipleSelect
is True, a list of selected nodes is specified.


Inherited from: 'wx._controls.TreeCtrl - can not provide a link

-------

.. _no-26225:

**Size** 

The size of the object. (tuple)


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-26226:

**Sizer** 

The sizer for the object.


Inherited from: 'wx._core.Window - can not provide a link

-------

.. _no-26227:

**StatusText** 

Specifies the text that displays in the form's status bar, if any.

    The text will appear when the control gets the focus, or when the
    mouse hovers over the control, and will clear when the control loses
    the focus, or when the mouse is no longer hovering.

    For forms, set StatusText whenever you want to display a message.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26228:

**TabStop** 

Specifies whether this control can receive focus from keyboard navigation.


Inherited from: :ref:`dabo.ui.uiwx.dControlMixin.dControlMixin`

-------

.. _no-26229:

**Tag** 

A property that user code can safely use for specific purposes.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26230:

**ToolTipText** 

Specifies the tooltip text associated with this window. (str)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26231:

**Top** 

The top position of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26232:

**Transparency** 

Transparency level of the control; ranges from 0 (transparent) to 255 (opaque).
    Default=0. Does not currently work on Gtk/Linux.  (int)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26233:

**TransparencyDelay** 

Time in seconds to change transparency. Set it to zero to see instant changes.
    Default=0.25 (float)
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26235:

**Visible** 

Specifies whether the object is visible at runtime.  (bool)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26236:

**VisibleOnScreen** 

Specifies whether the object is physically visible at runtime.  (bool)

    The Visible property could return True even if the object isn't actually
    shown on screen, due to a parent object or sizer being invisible.

    The VisibleOnScreen property will return True only if the object and all
    parents are visible.
    


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26237:

**Width** 

The width of the object. (int)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26238:

**WindowHandle** 

The platform-specific handle for the window. Read-only. (long)


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|method_summary| Events Summary
===============================


======================================== ========================
:ref:`BackgroundErased <no-26239>`       Occurs when a window background has been erased and needs repainting.
:ref:`Create <no-26240>`                 Occurs after the control or form is created.
:ref:`Destroy <no-26241>`                Occurs when the control or form is destroyed.
:ref:`FontPropertiesChanged <no-26242>`  Occurs when the properties of a dFont have changed.
:ref:`GotFocus <no-26243>`               Occurs when the control gets the focus.
:ref:`Idle <no-26244>`                   Occurs when the event loop has no active events to process.
:ref:`KeyChar <no-26245>`                Occurs when a key is depressed and released on the
:ref:`KeyDown <no-26246>`                Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-26247>`               
:ref:`KeyUp <no-26248>`                  Occurs when any key is released on the focused control or form.
:ref:`LostFocus <no-26249>`              Occurs when the control loses the focus.
:ref:`MenuClose <no-26250>`              Occurs when a menu has just been closed.
:ref:`MenuOpen <no-26251>`               Occurs when a menu is about to be opened.
:ref:`MouseEnter <no-26252>`             Occurs when the mouse pointer enters the form or control.
:ref:`MouseEvent <no-26253>`             
:ref:`MouseLeave <no-26254>`             Occurs when the mouse pointer leaves the form or control.
:ref:`MouseLeftClick <no-26255>`         Occurs when the mouse's left button is depressed
:ref:`MouseLeftDoubleClick <no-26256>`   Occurs when the mouse's left button is double-clicked on the control.
:ref:`MouseLeftDown <no-26257>`          Occurs when the mouse's left button is depressed on the control.
:ref:`MouseLeftUp <no-26258>`            Occurs when the mouse's left button is released on the control.
:ref:`MouseMiddleClick <no-26259>`       Occurs when the mouse mouse's middle button is depressed
:ref:`MouseMiddleDoubleClick <no-26260>` Occurs when the mouse's middle button is double-clicked
:ref:`MouseMiddleDown <no-26261>`        Occurs when the mouse's middle button is depressed on the control.
:ref:`MouseMiddleUp <no-26262>`          Occurs when the mouse's middle button is released on the control.
:ref:`MouseMove <no-26263>`              Occurs when the mouse moves in the control.
:ref:`MouseRightClick <no-26264>`        Occurs when the mouse mouse's right button is depressed
:ref:`MouseRightDoubleClick <no-26265>`  Occurs when the mouse's right button is double-clicked on the control.
:ref:`MouseRightDown <no-26266>`         Occurs when the mouse's right button is depressed on the control.
:ref:`MouseRightUp <no-26267>`           Occurs when the mouse's right button is released on the control.
:ref:`MouseWheel <no-26268>`             Occurs when the user scrolls the mouse wheel.
:ref:`Move <no-26269>`                   Occurs when the control's position changes.
:ref:`Paint <no-26270>`                  Occurs when it is time to paint the control.
:ref:`Resize <no-26271>`                 Occurs when the control or form is resized.
:ref:`TreeBeginDrag <no-26272>`          Occurs when a drag operation begins in a tree.
:ref:`TreeEndDrag <no-26273>`            Occurs when a drag operation ends in a tree.
:ref:`TreeEvent <no-26274>`              
:ref:`TreeItemCollapse <no-26275>`       Occurs when an expanded item in a tree collapses.
:ref:`TreeItemContextMenu <no-26276>`    Occurs when a tree item receives a context menu event.
:ref:`TreeItemExpand <no-26277>`         Occurs when a collapsed item in a tree expands.
:ref:`TreeSelection <no-26278>`          Occurs when the selected item in a tree control changes.
:ref:`Update <no-26279>`                 Occurs when a container wants its controls to update

======================================== ========================


Events
=======

.. _no-26239:

**BackgroundErased** 

Occurs when a window background has been erased and needs repainting.



-------

.. _no-26240:

**Create** 

Occurs after the control or form is created.



-------

.. _no-26241:

**Destroy** 

Occurs when the control or form is destroyed.



-------

.. _no-26242:

**FontPropertiesChanged** 

Occurs when the properties of a dFont have changed.



-------

.. _no-26243:

**GotFocus** 

Occurs when the control gets the focus.



-------

.. _no-26244:

**Idle** 

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




-------

.. _no-26245:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-26246:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-26247:

**KeyEvent** 



-------

.. _no-26248:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------

.. _no-26249:

**LostFocus** 

Occurs when the control loses the focus.



-------

.. _no-26250:

**MenuClose** 

Occurs when a menu has just been closed.



-------

.. _no-26251:

**MenuOpen** 

Occurs when a menu is about to be opened.



-------

.. _no-26252:

**MouseEnter** 

Occurs when the mouse pointer enters the form or control.



-------

.. _no-26253:

**MouseEvent** 



-------

.. _no-26254:

**MouseLeave** 

Occurs when the mouse pointer leaves the form or control.



-------

.. _no-26255:

**MouseLeftClick** 

Occurs when the mouse's left button is depressed
and released on the control.




-------

.. _no-26256:

**MouseLeftDoubleClick** 

Occurs when the mouse's left button is double-clicked on the control.



-------

.. _no-26257:

**MouseLeftDown** 

Occurs when the mouse's left button is depressed on the control.



-------

.. _no-26258:

**MouseLeftUp** 

Occurs when the mouse's left button is released on the control.



-------

.. _no-26259:

**MouseMiddleClick** 

Occurs when the mouse mouse's middle button is depressed
and released on the control.




-------

.. _no-26260:

**MouseMiddleDoubleClick** 

Occurs when the mouse's middle button is double-clicked
on the control.




-------

.. _no-26261:

**MouseMiddleDown** 

Occurs when the mouse's middle button is depressed on the control.



-------

.. _no-26262:

**MouseMiddleUp** 

Occurs when the mouse's middle button is released on the control.



-------

.. _no-26263:

**MouseMove** 

Occurs when the mouse moves in the control.



-------

.. _no-26264:

**MouseRightClick** 

Occurs when the mouse mouse's right button is depressed
and released on the control.




-------

.. _no-26265:

**MouseRightDoubleClick** 

Occurs when the mouse's right button is double-clicked on the control.



-------

.. _no-26266:

**MouseRightDown** 

Occurs when the mouse's right button is depressed on the control.



-------

.. _no-26267:

**MouseRightUp** 

Occurs when the mouse's right button is released on the control.



-------

.. _no-26268:

**MouseWheel** 

Occurs when the user scrolls the mouse wheel.



-------

.. _no-26269:

**Move** 

Occurs when the control's position changes.



-------

.. _no-26270:

**Paint** 

Occurs when it is time to paint the control.



-------

.. _no-26271:

**Resize** 

Occurs when the control or form is resized.



-------

.. _no-26272:

**TreeBeginDrag** 

 Occurs when a drag operation begins in a tree.



-------

.. _no-26273:

**TreeEndDrag** 

 Occurs when a drag operation ends in a tree.



-------

.. _no-26274:

**TreeEvent** 



-------

.. _no-26275:

**TreeItemCollapse** 

 Occurs when an expanded item in a tree collapses.



-------

.. _no-26276:

**TreeItemContextMenu** 

 Occurs when a tree item receives a context menu event.



-------

.. _no-26277:

**TreeItemExpand** 

 Occurs when a collapsed item in a tree expands.



-------

.. _no-26278:

**TreeSelection** 

 Occurs when the selected item in a tree control changes.



-------

.. _no-26279:

**Update** 

Occurs when a container wants its controls to update
their properties.




-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`absoluteCoordinates <no-26280>`   Translates a position value for a control to absolute screen position.
:ref:`addDummyData <no-26281>`          For testing purposes!
:ref:`addImage <no-26282>`              Adds the passed image to the control's ImageList, and maintains
:ref:`addObject <no-26283>`             Instantiate object as a child of self.
:ref:`afterInit <no-26284>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterInitAll <no-26285>`          
:ref:`afterSetProperties <no-26286>`    
:ref:`allowDrag <no-26287>`             
:ref:`appendNode <no-26288>`            
:ref:`autoBindEvents <no-26289>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-26290>`            Subclass hook. Called before the object is fully instantiated.
:ref:`beforeSetProperties <no-26291>`   
:ref:`bindEvent <no-26292>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-26293>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bindKey <no-26294>`               Bind a key combination such as "ctrl+c" to a callback function.
:ref:`bringToFront <no-26295>`          Makes this object topmost
:ref:`clear <no-26296>`                 
:ref:`clone <no-26297>`                 Create another object just like the passed object. It assumes that the
:ref:`collapse <no-26298>`              
:ref:`collapseAll <no-26299>`           
:ref:`collapseBranch <no-26300>`        Collapses the specified node, as well as any of its child nodes.
:ref:`containerCoordinates <no-26301>`  Given a position relative to this control, return a position relative
:ref:`copy <no-26302>`                  Called by uiApp when the user requests a copy operation.
:ref:`cut <no-26303>`                   Called by uiApp when the user requests a cut operation.
:ref:`drawArc <no-26304>`               Draws an arc (pie slice) of a circle centered around the specified point,
:ref:`drawBitmap <no-26305>`            Draws a bitmap on the object at the specified position.
:ref:`drawCircle <no-26306>`            Draws a circle of the specified radius around the specified point.
:ref:`drawEllipse <no-26307>`           Draws an ellipse contained within the rectangular space defined by
:ref:`drawEllipticArc <no-26308>`       Draws an arc (pie slice) of a ellipse contained by the specified
:ref:`drawGradient <no-26309>`          Draws a horizontal or vertical gradient on the control. Default
:ref:`drawLine <no-26310>`              Draws a line between (x1,y1) and (x2, y2).
:ref:`drawPolyLines <no-26311>`         Draws a series of connected line segments defined by the specified points.
:ref:`drawPolygon <no-26312>`           Draws a polygon defined by the specified points.
:ref:`drawRectangle <no-26313>`         Draws a rectangle of the specified size beginning at the specified
:ref:`drawRoundedRectangle <no-26314>`  Draws a rounded rectangle of the specified size beginning at the specified
:ref:`drawText <no-26315>`              Draws text on the object at the specified position
:ref:`endHover <no-26316>`              
:ref:`expand <no-26317>`                
:ref:`expandAll <no-26318>`             
:ref:`expandBranch <no-26319>`          Expands the specified node, as well as any of its child nodes.
:ref:`find <no-26320>`                  Searches the nodes collection for all nodes that match
:ref:`findPattern <no-26321>`           Allows for regexp pattern matching in order to find matching
:ref:`fitToSizer <no-26322>`            Resize the control to fit the size required by its sizer.
:ref:`fontZoomIn <no-26323>`            Zoom in on the font, by setting a higher point size.
:ref:`fontZoomNormal <no-26324>`        Reset the font zoom back to zero.
:ref:`fontZoomOut <no-26325>`           Zoom out on the font, by setting a lower point size.
:ref:`formCoordinates <no-26326>`       Given a position relative to this control, return a position relative
:ref:`getAbsoluteName <no-26327>`       Return the fully qualified name of the object.
:ref:`getCaptureBitmap <no-26328>`      Return a bitmap snapshot of self as it appears in the UI at this moment.
:ref:`getChildren <no-26329>`           Returns a list of all nodes that are child nodes of this node.
:ref:`getContainingPage <no-26330>`     Return the dPage or WizardPage that contains self.
:ref:`getDescendents <no-26331>`        Returns a list of all nodes that are direct descendents of this node.
:ref:`getDisplayLocker <no-26332>`      Returns an object that locks the current display when created, and
:ref:`getMousePosition <no-26333>`      Returns the current mouse position on the entire screen
:ref:`getNodeForID <no-26334>`          Given a wx item ID, returns the corresponding node, or None.
:ref:`getNodeImg <no-26335>`            Returns the index of the specified node's image in the
:ref:`getNodeUnderMouse <no-26336>`     Returns the node directly under the mouse, or None if the mouse is not
:ref:`getParentNode <no-26337>`         Returns the node that is the parent of the given node, or
:ref:`getPositionInSizer <no-26338>`    Convenience method to let you call this directly on the object.
:ref:`getProperties <no-26339>`         Returns a dictionary of property name/value pairs.
:ref:`getRootNode <no-26340>`           
:ref:`getSiblings <no-26341>`           Returns a list of all nodes at the same level as the specified
:ref:`getSizerProp <no-26342>`          Gets the current setting for the given property from the object's
:ref:`getSizerProps <no-26343>`         Returns a dict containing the object's sizer property info. The
:ref:`hide <no-26344>`                  Make the object invisible.
:ref:`initEvents <no-26345>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-26346>`        Hook for subclasses. User subclasses should set properties
:ref:`isContainedBy <no-26347>`         Returns True if the containership hierarchy for this control
:ref:`iterateCall <no-26348>`           Call the given function on this object and all of its Children. If
:ref:`lockDisplay <no-26349>`           Locks the visual updates to the control.
:ref:`makeDirTree <no-26350>`           Make this dTreeView show a filesystem directory hierarchy. You
:ref:`moveTabOrderAfter <no-26351>`     Moves this object's tab order after the passed obj.
:ref:`moveTabOrderBefore <no-26352>`    Moves this object's tab order before the passed obj.
:ref:`nextNode <no-26353>`              If the current node has children, returns the first child node. If
:ref:`nextSibling <no-26354>`           Returns the next sibling node, or None if there are no more
:ref:`nodeForObject <no-26355>`         Given an object, returns the corresponding node.
:ref:`objectCoordinates <no-26356>`     Given a position relative to the form, return a position relative
:ref:`onHover <no-26357>`               
:ref:`paste <no-26358>`                 Called by uiApp when the user requests a paste operation.
:ref:`posIsWithin <no-26359>`           
:ref:`priorNode <no-26360>`             Returns last child of the prior sibling node. If there
:ref:`priorSibling <no-26361>`          Returns the prior sibling node, or None if there are no more
:ref:`processDroppedFiles <no-26362>`   Handler for files dropped on the control. Override in your
:ref:`processDroppedText <no-26363>`    Handler for text dropped on the control. Override in your
:ref:`raiseEvent <no-26364>`            Raise the passed Dabo event.
:ref:`reCreate <no-26365>`              Abstract method: subclasses MUST override for UI-specifics.
:ref:`recreate <no-26366>`              Recreate the object.
:ref:`redraw <no-26367>`                Called when the object is (re)drawn.
:ref:`refresh <no-26368>`               Repaints this control and all contained objects.
:ref:`refreshDisplay <no-26369>`        Changing some node appearance properties requires that the tree be
:ref:`relativeCoordinates <no-26370>`   Translates an absolute screen position to position value for a control.
:ref:`release <no-26371>`               Destroys the object.
:ref:`removeDrawnObject <no-26372>`     
:ref:`removeNode <no-26373>`            
:ref:`sendToBack <no-26374>`            Places this object behind all others.
:ref:`setAll <no-26375>`                Set all child object properties to the passed value.
:ref:`setFocus <no-26376>`              Sets focus to the object.
:ref:`setNodeImg <no-26377>`            Sets the specified node's image to the image corresponding to the
:ref:`setPositionInSizer <no-26378>`    Convenience method to let you call this directly on the object.
:ref:`setProperties <no-26379>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-26380>` Sets a group of properties on the object all at once. This
:ref:`setRootNode <no-26381>`           
:ref:`setSizerProp <no-26382>`          Tells the object's ControllingSizer to adjust the requested property.
:ref:`setSizerProps <no-26383>`         Convenience method for setting multiple sizer item properties at once. The
:ref:`show <no-26384>`                  Make the object visible.
:ref:`showContainingPage <no-26385>`    If this object is inside of any paged control, it will force all containing
:ref:`showContextMenu <no-26386>`       Display a context menu (popup) at the specified position.
:ref:`showNode <no-26387>`              
:ref:`super <no-26388>`                 This method used to call superclass code, but it's been removed.
:ref:`treeFromStructure <no-26389>`     Given a sequence of items with a standard format,
:ref:`unbindEvent <no-26390>`           Remove a previously registered event binding.
:ref:`unbindKey <no-26391>`             Unbind a previously bound key combination.
:ref:`unlockDisplay <no-26392>`         Unlocks the visual updates to the control.
:ref:`unlockDisplayAll <no-26393>`      Immediately unlocks the display, no matter how many previous
:ref:`update <no-26394>`                Update the properties of this object and all contained objects.

======================================= ========================


Methods
=======

.. _no-26281:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.addDummyData(self)

   For testing purposes!



-------

.. _no-26282:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.addImage(self, img, key=None)

   
   Adds the passed image to the control's ImageList, and maintains
   a reference to it that is retrievable via the key value.
   



-------

.. _no-26287:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.allowDrag(self, node)



-------

.. _no-26288:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.appendNode(self, node, txt)



-------

.. _no-26296:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.clear(self, clearImageList=False)



-------

.. _no-26298:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.collapse(self, node)



-------

.. _no-26299:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.collapseAll(self)



-------

.. _no-26300:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.collapseBranch(self, nd)

   Collapses the specified node, as well as any of its child nodes.



-------

.. _no-26317:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.expand(self, node)



-------

.. _no-26318:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.expandAll(self)



-------

.. _no-26319:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.expandBranch(self, nd)

   Expands the specified node, as well as any of its child nodes.



-------

.. _no-26320:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.find(self, srch, top=None)

   
   Searches the nodes collection for all nodes that match
   whose text matches the passed search value (if a text value
   was passed). If a wxPython TreeItemID object is passed, returns
   a list nodes matching that itemID value. If a specific node is passed
   in the top property, the search is limited to descendents of that
   node.
   Returns a list of matching nodes.
   



-------

.. _no-26321:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.findPattern(self, srchPat, top=None)

   
   Allows for regexp pattern matching in order to find matching
   nodes using less than exact matches. If a specific node is passed
   in the top property, the search is limited to descendents of that
   node.
   Returns a list of matching nodes.
   



-------

.. _no-26329:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.getChildren(self, node)

   Returns a list of all nodes that are child nodes of this node.



-------

.. _no-26331:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.getDescendents(self, node)

   Returns a list of all nodes that are direct descendents of this node.



-------

.. _no-26334:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.getNodeForID(self, idval)

   Given a wx item ID, returns the corresponding node, or None.



-------

.. _no-26335:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.getNodeImg(self, node, which='normal')

   
   Returns the index of the specified node's image in the
   current image list, or -1 if no image is set for the node.
   Which is the state of the node.
   
   Valid states are:
   
       'normal'
       'expanded'
       'selected'
       'selectedexpanded'
   
   



-------

.. _no-26336:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.getNodeUnderMouse(self, includeSpace=False, includeButton=True)

   
   Returns the node directly under the mouse, or None if the mouse is not
   over a node. If 'includeSpace' is True, the empty space to the right of the node
   is counted as part of the node. Likewise, if 'includeButton' is True, the
   area for the expanding/collapsing button is considered part of the node.
   Otherwise, it is considered to not be over any node.
   



-------

.. _no-26337:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.getParentNode(self, node)

   
   Returns the node that is the parent of the given node, or
   None if the node is the root.
   



-------

.. _no-26340:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.getRootNode(self)



-------

.. _no-26341:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.getSiblings(self, node)

   
   Returns a list of all nodes at the same level as the specified
   node. The specified node is included in the list.
   



-------

.. _no-26350:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.makeDirTree(self, dirPath, wildcard=None, ignored=None, showHidden=False, expand=False)

   
   Make this dTreeView show a filesystem directory hierarchy. You
   can specify a wildcard pattern: e.g., "\*py" will only include files
   ending in 'py'. You can also pass a list of wildcards, and files
   matching any of these will be included in the tree. If no wildcard
   is specified, all files will be included.
   
   You can also specify file patterns to ignore in the 'ignored' parameter.
   This can be a single string of a file pattern, or a list of such patterns.
   Any file matching any of these patterns will not be included in the tree.
   
   By default, hidden files (i.e., those beginning with a period) are ignored.
   You can optionally show them by passing True in the showHidden
   parameter.
   
   The tree defaults to fully collapsed; you can change it to fully
   expanded by passing True in the 'expand' parameter.
   
   Warning: Don't use this for huge hierarchies, as it blocks while
   filling the complete tree, instead of only filling the nodes as
   they are opened.
   



-------

.. _no-26353:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.nextNode(self, nd=None)

   
   If the current node has children, returns the first child node. If
   it has no children, returns the next sibling. If there are no next
   siblings, returns the next sibling of the parent node. If the parent
   node has no more siblings, returns the next sibling of the grand-
   parent node, etc. Returns None if we are at the absolute bottom
   of the flattened tree structure. Sometimes referred to as 'flatdown'
   navigation.
   



-------

.. _no-26354:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.nextSibling(self, nd=None)

   Returns the next sibling node, or None if there are no more



-------

.. _no-26355:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.nodeForObject(self, obj)

   Given an object, returns the corresponding node.



-------

.. _no-26360:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.priorNode(self, nd=None)

   
   Returns last child of the prior sibling node. If there
   are no prior siblings, returns the parent. Sometimes
   referred to as 'flatup' navigation.
   



-------

.. _no-26361:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.priorSibling(self, nd=None)

   Returns the prior sibling node, or None if there are no more



-------

.. _no-26369:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.refreshDisplay(self)

   
   Changing some node appearance properties requires that the tree be
   collapsed and re-opened in order to update any sizing issues.
   



-------

.. _no-26373:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.removeNode(self, node)



-------

.. _no-26377:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.setNodeImg(self, node, imgKey, which='normal')

   
   Sets the specified node's image to the image corresponding to the
   specified key. May also optionally pass the index of the image in the
   image list rather than the key, which is the state of the node.
   
   Valid states are:
   
       'normal'
       'expanded'
       'selected'
       'selectedexpanded'
   
   



-------

.. _no-26381:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.setRootNode(self, txt)



-------

.. _no-26387:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.showNode(self, node)



-------

.. _no-26389:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.treeFromStructure(self, stru, topNode=None)

   
   Given a sequence of items with a standard format,
   this will construct a tree structure and append it to
   the specified 'topNode'. If 'topNode' is None, the tree
   will be cleared, and a new structure containing only the
   passed info will be created. The info should be passed
   as a sequence of either lists or tuples, with the first
   element being the text to be displayed, and, if there are
   to be child nodes, the second being the child node
   information. If there are no children for that node, either
   do not include the second element, or set it to None.
   If there are child nodes, the child information will be
   recursively parsed.
   



-------


Methods - inherited
=====================

.. _no-26280:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.absoluteCoordinates(self, pos=None)
   :noindex:


   Translates a position value for a control to absolute screen position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26283:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.addObject(self, classRef, Name=None, \*args, \**kwargs)
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

.. _no-26284:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26285:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.afterInitAll(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26286:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.afterSetProperties(self)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26289:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.autoBindEvents(self, force=True)
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

.. _no-26290:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26291:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.beforeSetProperties(self, properties)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26292:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-26293:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-26294:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.bindKey(self, keyCombo, callback, \**kwargs)
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

.. _no-26295:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.bringToFront(self)
   :noindex:


   Makes this object topmost


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26297:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.clone(self, obj, name=None)
   :noindex:


   
   Create another object just like the passed object. It assumes that the
   calling object will be the container of the newly created object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26301:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.containerCoordinates(self, cnt, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the specified container. If no position is passed, returns the position
   of this control relative to the container.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26302:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.copy(self)
   :noindex:


   
   Called by uiApp when the user requests a copy operation.
   
   Return None (the default) and uiApp will try a default copy operation.
   Return anything other than None and uiApp will assume that the copy
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26303:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.cut(self)
   :noindex:


   
   Called by uiApp when the user requests a cut operation.
   
   Return None (the default) and uiApp will try a default cut operation.
   Return anything other than None and uiApp will assume that the cut
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26304:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.drawArc(self, xPos, yPos, rad, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a circle centered around the specified point,
   starting from 'startAngle' degrees, and sweeping counter-clockwise
   until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26305:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.drawBitmap(self, bmp, x=0, y=0, mode=None, persist=True, transparent=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   Draws a bitmap on the object at the specified position.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26306:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.drawCircle(self, xPos, yPos, rad, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
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

.. _no-26307:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.drawEllipse(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an ellipse contained within the rectangular space defined by
   the position and size coordinates
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26308:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.drawEllipticArc(self, xPos, yPos, width, height, startAngle, endAngle, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws an arc (pie slice) of a ellipse contained by the specified
   dimensions, starting from 'startAngle' degrees, and sweeping
   counter-clockwise until 'endAngle' is reached.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26309:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.drawGradient(self, orientation, x=0, y=0, width=None, height=None, color1=None, color2=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a horizontal or vertical gradient on the control. Default
   is to cover the entire control, although you can specify positions.
   The gradient is drawn with 'color1' as the top/left color, and 'color2'
   as the bottom/right color.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26310:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.drawLine(self, x1, y1, x2, y2, penColor='black', penWidth=1, fillColor=None, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a line between (x1,y1) and (x2, y2).
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26311:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.drawPolyLines(self, points, penColor='black', penWidth=1, lineStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a series of connected line segments defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the shape. Lines
   are drawn connecting the points sequentially, but a segment from the last
   point to the first is not drawn, leaving an 'open' polygon. As a result, there is no
   FillColor or HatchStyle defined for this.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26312:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.drawPolygon(self, points, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a polygon defined by the specified points.
   
   The 'points' parameter should be a tuple of (x,y) pairs defining the
   polygon.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26313:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.drawRectangle(self, xPos, yPos, width, height, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rectangle of the specified size beginning at the specified
   point.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26314:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.drawRoundedRectangle(self, xPos, yPos, width, height, radius, penColor='black', penWidth=1, fillColor=None, lineStyle=None, hatchStyle=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws a rounded rectangle of the specified size beginning at the specified
   point, with the specified corner radius.
   
   See the 'drawCircle()' method above for more details.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26315:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.drawText(self, text, x=0, y=0, angle=0, fontFace=None, fontSize=None, fontBold=None, fontItalic=None, fontUnderline=None, foreColor=None, backColor=None, mode=None, persist=True, visible=True, dc=None, useDefaults=False)
   :noindex:


   
   Draws text on the object at the specified position
   using the specified characteristics. Any characteristics
   not specified will be set to the system default.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26316:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.endHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26322:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.fitToSizer(self, extraWidth=0, extraHeight=0)
   :noindex:


   Resize the control to fit the size required by its sizer.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26323:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.fontZoomIn(self, amt=1)
   :noindex:


   Zoom in on the font, by setting a higher point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-26324:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.fontZoomNormal(self)
   :noindex:


   Reset the font zoom back to zero.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-26325:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.fontZoomOut(self, amt=1)
   :noindex:


   Zoom out on the font, by setting a lower point size.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-26326:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.formCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to this control, return a position relative
   to the containing form. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26327:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26328:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.getCaptureBitmap(self)
   :noindex:


   Return a bitmap snapshot of self as it appears in the UI at this moment.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26330:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.getContainingPage(self)
   :noindex:


   
   Return the dPage or WizardPage that contains self.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26332:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.getDisplayLocker(self)
   :noindex:


   
   Returns an object that locks the current display when created, and
   unlocks it when destroyed. This is generally safer than calling lockDisplay()
   and unlockDisplay(), especially when used with callAfterInterval(), when
   the unlockDisplay() calls may not all happen.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26333:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.getMousePosition(self)
   :noindex:


   
   Returns the current mouse position on the entire screen
   relative to this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26338:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.getPositionInSizer(self)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26339:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-26342:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.getSizerProp(self, prop)
   :noindex:


   
   Gets the current setting for the given property from the object's
   ControllingSizer. Returns None if object is not in a sizer.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26343:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.getSizerProps(self)
   :noindex:


   
   Returns a dict containing the object's sizer property info. The
   keys are the property names, and the values are the current
   values for those props.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26344:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.hide(self)
   :noindex:


   Make the object invisible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26345:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26346:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26347:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.isContainedBy(self, obj)
   :noindex:


   
   Returns True if the containership hierarchy for this control
   includes the passed object reference.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26348:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.iterateCall(self, funcName, \*args, \**kwargs)
   :noindex:


   
   Call the given function on this object and all of its Children. If
   any object does not have the given function, no error is raised; it
   is simply ignored.
   


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-26349:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.lockDisplay(self)
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

.. _no-26351:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.moveTabOrderAfter(self, obj)
   :noindex:


   Moves this object's tab order after the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26352:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.moveTabOrderBefore(self, obj)
   :noindex:


   Moves this object's tab order before the passed obj.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26356:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.objectCoordinates(self, pos=None)
   :noindex:


   
   Given a position relative to the form, return a position relative
   to this object. If no position is passed, returns the position
   of this control relative to the form.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26357:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.onHover(self, evt=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26358:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.paste(self)
   :noindex:


   
   Called by uiApp when the user requests a paste operation.
   
   Return None (the default) and uiApp will try a default paste operation.
   Return anything other than None and uiApp will assume that the paste
   operation has been handled.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26359:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.posIsWithin(self, xpos, ypos=None)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26362:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.processDroppedFiles(self, filelist, x, y)
   :noindex:


   
   Handler for files dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26363:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.processDroppedText(self, txt, x, y)
   :noindex:


   
   Handler for text dropped on the control. Override in your
   subclass/instance for your needs .
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26364:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.raiseEvent(self, eventClass, nativeEvent=None, \*args, \**kwargs)
   :noindex:


   Raise the passed Dabo event.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26365:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.reCreate(self, child=None)
   :noindex:


   Abstract method: subclasses MUST override for UI-specifics.


Inherited from: :ref:`dabo.ui.dPemMixinBase.dPemMixinBase`

-------

.. _no-26366:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.recreate(self, child=None)
   :noindex:


   
   Recreate the object.
   
   Warning: this is experimental and is known to cause hair loss.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26367:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.redraw(self, dc)
   :noindex:


   
   Called when the object is (re)drawn.
   
   This is a user subclass hook, where you should put any drawing routines
   to affect the object appearance.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26368:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.refresh(self, fromRefresh=False)
   :noindex:


   Repaints this control and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26370:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.relativeCoordinates(self, pos=None)
   :noindex:


   Translates an absolute screen position to position value for a control.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26371:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.release(self)
   :noindex:


   Destroys the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26372:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.removeDrawnObject(self, obj)
   :noindex:



Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26374:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.sendToBack(self)
   :noindex:


   Places this object behind all others.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26375:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.setAll(self, prop, val, recurse=True, filt=None, instancesOf=None)
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

.. _no-26376:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.setFocus(self)
   :noindex:


   Sets focus to the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26378:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.setPositionInSizer(self, pos)
   :noindex:


   Convenience method to let you call this directly on the object.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26379:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-26380:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-26382:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.setSizerProp(self, prop, val)
   :noindex:


   Tells the object's ControllingSizer to adjust the requested property.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26383:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.setSizerProps(self, propDict)
   :noindex:


   
   Convenience method for setting multiple sizer item properties at once. The
   dict should have the property name as the key and the desired new value
   as the associated value.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26384:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.show(self)
   :noindex:


   Make the object visible.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26385:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.showContainingPage(self)
   :noindex:


   
   If this object is inside of any paged control, it will force all containing
   paged controls to switch to the page that contains this object.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26386:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.showContextMenu(self, menu, pos=None, release=True)
   :noindex:


   
   Display a context menu (popup) at the specified position.
   
   If no position is specified, the menu will be displayed at the current
   mouse position.
   
   If release is True (the default), the menu will be released after the user
   has dismissed it.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26388:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-26390:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-26391:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.unbindKey(self, keyCombo)
   :noindex:


   
   Unbind a previously bound key combination.
   
   Fail silently if the key combination didn't exist already.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26392:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.unlockDisplay(self)
   :noindex:


   
   Unlocks the visual updates to the control.
   
   Use in conjunction with lockDisplay(), when you are doing lots of things
   that would result in lengthy screen updates.
   
   Since lockDisplay() may be called several times on an object, calling
   unlockDisplay() will "undo" one locking call. When all locks have been
   removed, repainting of the display will resume.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26393:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.unlockDisplayAll(self)
   :noindex:


   
   Immediately unlocks the display, no matter how many previous
   lockDisplay calls have been made. Useful in a callAfterInterval()
   construction to avoid flicker.
   


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------

.. _no-26394:

.. function:: dabo.ui.uiwx.dTreeView.dTreeView.update(self)
   :noindex:


   Update the properties of this object and all contained objects.


Inherited from: :ref:`dabo.ui.uiwx.dPemMixin.dPemMixin`

-------


|
