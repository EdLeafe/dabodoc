
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dPemMixin

.. _dabo.ui.uiwx.dPemMixin.DrawObject:

=============================================
|doc_title|  **dPemMixin.DrawObject** - class
=============================================


Class to handle drawing on an object.

It is not meant to be used directly; instead, it is returned after a drawing
instruction is called on the object.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **DrawObject**

.. inheritance-diagram:: DrawObject


|supclasses| Known Superclasses
===============================

* :ref:`dabo.dObject.dObject`



|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.dPemMixin.DrawObject

   .. automethod:: dabo.ui.uiwx.dPemMixin.DrawObject.__init__

|method_summary| Properties Summary
===================================


======================================= ========================
:ref:`Angle <no-11533>`                 Angle (in degrees) to draw text  (int)
:ref:`Application <no-11534>`           Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BackColor <no-11535>`             Background color of text when using text objects  (str or tuple)
:ref:`BaseClass <no-11536>`             The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-11537>`           Base key used when saving/restoring preferences  (str)
:ref:`Bitmap <no-11538>`                Bitmap to be drawn on the object  (dBitmap)
:ref:`Class <no-11539>`                 The class the object is based on. Read-only.  (class)
:ref:`DrawMode <no-11540>`              Logical operation for how the drawing is done. Can be one of:  (str)
:ref:`DynamicAngle <no-11541>`          Dynamically determine the value of the Angle property.
:ref:`DynamicBackColor <no-11542>`      Dynamically determine the value of the BackColor property.
:ref:`DynamicBitmap <no-11543>`         Dynamically determine the value of the Bitmap property.
:ref:`DynamicDrawMode <no-11544>`       Dynamically determine the value of the DrawMode property.
:ref:`DynamicFillColor <no-11545>`      Dynamically determine the value of the FillColor property.
:ref:`DynamicFontBold <no-11546>`       Dynamically determine the value of the FontBold property.
:ref:`DynamicFontFace <no-11547>`       Dynamically determine the value of the FontFace property.
:ref:`DynamicFontItalic <no-11548>`     Dynamically determine the value of the FontItalic property.
:ref:`DynamicFontSize <no-11549>`       Dynamically determine the value of the FontSize property.
:ref:`DynamicFontUnderline <no-11550>`  Dynamically determine the value of the FontUnderline property.
:ref:`DynamicForeColor <no-11551>`      Dynamically determine the value of the ForeColor property.
:ref:`DynamicGradientColor1 <no-11552>` Dynamically determine the value of the GradientColor1 property.
:ref:`DynamicGradientColor2 <no-11553>` Dynamically determine the value of the GradientColor2 property.
:ref:`DynamicHeight <no-11554>`         Dynamically determine the value of the Height property.
:ref:`DynamicLineStyle <no-11555>`      Dynamically determine the value of the LineStyle property.
:ref:`DynamicOrientation <no-11556>`    Dynamically determine the value of the Orientation property.
:ref:`DynamicParent <no-11557>`         Dynamically determine the value of the Parent property.
:ref:`DynamicPenColor <no-11558>`       Dynamically determine the value of the PenColor property.
:ref:`DynamicPenWidth <no-11559>`       Dynamically determine the value of the PenWidth property.
:ref:`DynamicPoints <no-11560>`         Dynamically determine the value of the Points property.
:ref:`DynamicRadius <no-11561>`         Dynamically determine the value of the Radius property.
:ref:`DynamicShape <no-11562>`          Dynamically determine the value of the Shape property.
:ref:`DynamicText <no-11563>`           Dynamically determine the value of the Text property.
:ref:`DynamicTransparent <no-11564>`    Dynamically determine the value of the Transparent property.
:ref:`DynamicVisible <no-11565>`        Dynamically determine the value of the Visible property.
:ref:`DynamicWidth <no-11566>`          Dynamically determine the value of the Width property.
:ref:`DynamicXpos <no-11567>`           Dynamically determine the value of the Xpos property.
:ref:`DynamicYpos <no-11568>`           Dynamically determine the value of the Ypos property.
:ref:`EndAngle <no-11569>`              Angle (in degrees) used to end drawing a circular or elliptic arc  (int)
:ref:`FillColor <no-11570>`             Background color for the shape  (color)
:ref:`FontBold <no-11571>`              Bold setting for text objects  (bool)
:ref:`FontFace <no-11572>`              Face of the font used for text objects  (str)
:ref:`FontItalic <no-11573>`            Italic setting for text objects  (bool)
:ref:`FontSize <no-11574>`              Size of the font used for text objects  (int)
:ref:`FontUnderline <no-11575>`         Underline setting for text objects  (bool)
:ref:`ForeColor <no-11576>`             Color of text when using text objects  (str or tuple)
:ref:`GradientColor1 <no-11577>`        Top/Left color for the gradient  (color: str or tuple)
:ref:`GradientColor2 <no-11578>`        Bottom/Right color for the gradient  (color: str or tuple)
:ref:`HatchStyle <no-11579>`            Hatching style for the fill.  (str)
:ref:`Height <no-11580>`                For rectangles, the height of the shape  (int)
:ref:`LineStyle <no-11581>`             Line style (solid, dash, dot) drawn  (str)
:ref:`LogEvents <no-11582>`             Specifies which events to log.  (list of strings)
:ref:`Name <no-11583>`                  The name of the object.  (str)
:ref:`Orientation <no-11584>`           Direction of the drawn gradient ('v' or 'h')  (str)
:ref:`Parent <no-11585>`                Reference to the object being drawn upon.  (object)
:ref:`PenColor <no-11586>`              ForeColor of the shape's lines  (color)
:ref:`PenWidth <no-11587>`              Width of the shape's lines  (int)
:ref:`Points <no-11588>`                Tuple of (x,y) pairs defining a polygon.  (tuple)
:ref:`Position <no-11589>`              Shorthand for (Xpos, Ypos).  (2-tuple)
:ref:`PreferenceManager <no-11590>`     Reference to the Preference Management object  (dPref)
:ref:`Radius <no-11591>`                For circles, the radius of the shape. For Rounded Rectangles,
:ref:`Rect <no-11592>`                  Reference to a wx.Rect that encompasses the drawn object (read-only) (wx.Rect)
:ref:`Shape <no-11593>`                 Type of shape to draw  (str)
:ref:`Size <no-11594>`                  Convenience property, equivalent to (Width, Height)  (2-tuple)
:ref:`StartAngle <no-11595>`            Angle (in degrees) used to start drawing a circular or elliptic arc  (int)
:ref:`Text <no-11596>`                  Text to be drawn  (str)
:ref:`Transparent <no-11597>`           Should the bitmap be drawn transparently?  (bool)
:ref:`Visible <no-11598>`               Controls whether the shape is drawn.  (bool)
:ref:`Width <no-11599>`                 For rectangles, the width of the shape  (int)
:ref:`Xpos <no-11600>`                  For circles, the x position of the center. For rectangles,
:ref:`Ypos <no-11601>`                  For circles, the y position of the center. For rectangles,

======================================= ========================


Properties
==========

.. _no-11533:

**Angle** 

Angle (in degrees) to draw text  (int)



-------

.. _no-11535:

**BackColor** 

Background color of text when using text objects  (str or tuple)



-------

.. _no-11538:

**Bitmap** 

Bitmap to be drawn on the object  (dBitmap)



-------

.. _no-11540:

**DrawMode** 

Logical operation for how the drawing is done. Can be one of:  (str)

        copy (or None) - default
        invert
        and
        and_invert
        and_reverse
        clear
        equiv
        nand
        nor
        no_op
        or
        or_invert
        or_reverse
        set
        src_invert
        xor

    



-------

.. _no-11541:

**DynamicAngle** 

Dynamically determine the value of the Angle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Angle property. If DynamicAngle is set to None (the default), Angle
will not be dynamically evaluated.



-------

.. _no-11542:

**DynamicBackColor** 

Dynamically determine the value of the BackColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
BackColor property. If DynamicBackColor is set to None (the default), BackColor
will not be dynamically evaluated.



-------

.. _no-11543:

**DynamicBitmap** 

Dynamically determine the value of the Bitmap property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Bitmap property. If DynamicBitmap is set to None (the default), Bitmap
will not be dynamically evaluated.



-------

.. _no-11544:

**DynamicDrawMode** 

Dynamically determine the value of the DrawMode property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
DrawMode property. If DynamicDrawMode is set to None (the default), DrawMode
will not be dynamically evaluated.



-------

.. _no-11545:

**DynamicFillColor** 

Dynamically determine the value of the FillColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FillColor property. If DynamicFillColor is set to None (the default), FillColor
will not be dynamically evaluated.



-------

.. _no-11546:

**DynamicFontBold** 

Dynamically determine the value of the FontBold property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontBold property. If DynamicFontBold is set to None (the default), FontBold
will not be dynamically evaluated.



-------

.. _no-11547:

**DynamicFontFace** 

Dynamically determine the value of the FontFace property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontFace property. If DynamicFontFace is set to None (the default), FontFace
will not be dynamically evaluated.



-------

.. _no-11548:

**DynamicFontItalic** 

Dynamically determine the value of the FontItalic property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontItalic property. If DynamicFontItalic is set to None (the default), FontItalic
will not be dynamically evaluated.



-------

.. _no-11549:

**DynamicFontSize** 

Dynamically determine the value of the FontSize property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontSize property. If DynamicFontSize is set to None (the default), FontSize
will not be dynamically evaluated.



-------

.. _no-11550:

**DynamicFontUnderline** 

Dynamically determine the value of the FontUnderline property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
FontUnderline property. If DynamicFontUnderline is set to None (the default), FontUnderline
will not be dynamically evaluated.



-------

.. _no-11551:

**DynamicForeColor** 

Dynamically determine the value of the ForeColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
ForeColor property. If DynamicForeColor is set to None (the default), ForeColor
will not be dynamically evaluated.



-------

.. _no-11552:

**DynamicGradientColor1** 

Dynamically determine the value of the GradientColor1 property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
GradientColor1 property. If DynamicGradientColor1 is set to None (the default), GradientColor1
will not be dynamically evaluated.



-------

.. _no-11553:

**DynamicGradientColor2** 

Dynamically determine the value of the GradientColor2 property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
GradientColor2 property. If DynamicGradientColor2 is set to None (the default), GradientColor2
will not be dynamically evaluated.



-------

.. _no-11554:

**DynamicHeight** 

Dynamically determine the value of the Height property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Height property. If DynamicHeight is set to None (the default), Height
will not be dynamically evaluated.



-------

.. _no-11555:

**DynamicLineStyle** 

Dynamically determine the value of the LineStyle property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
LineStyle property. If DynamicLineStyle is set to None (the default), LineStyle
will not be dynamically evaluated.



-------

.. _no-11556:

**DynamicOrientation** 

Dynamically determine the value of the Orientation property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Orientation property. If DynamicOrientation is set to None (the default), Orientation
will not be dynamically evaluated.



-------

.. _no-11557:

**DynamicParent** 

Dynamically determine the value of the Parent property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Parent property. If DynamicParent is set to None (the default), Parent
will not be dynamically evaluated.



-------

.. _no-11558:

**DynamicPenColor** 

Dynamically determine the value of the PenColor property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
PenColor property. If DynamicPenColor is set to None (the default), PenColor
will not be dynamically evaluated.



-------

.. _no-11559:

**DynamicPenWidth** 

Dynamically determine the value of the PenWidth property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
PenWidth property. If DynamicPenWidth is set to None (the default), PenWidth
will not be dynamically evaluated.



-------

.. _no-11560:

**DynamicPoints** 

Dynamically determine the value of the Points property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Points property. If DynamicPoints is set to None (the default), Points
will not be dynamically evaluated.



-------

.. _no-11561:

**DynamicRadius** 

Dynamically determine the value of the Radius property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Radius property. If DynamicRadius is set to None (the default), Radius
will not be dynamically evaluated.



-------

.. _no-11562:

**DynamicShape** 

Dynamically determine the value of the Shape property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Shape property. If DynamicShape is set to None (the default), Shape
will not be dynamically evaluated.



-------

.. _no-11563:

**DynamicText** 

Dynamically determine the value of the Text property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Text property. If DynamicText is set to None (the default), Text
will not be dynamically evaluated.



-------

.. _no-11564:

**DynamicTransparent** 

Dynamically determine the value of the Transparent property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Transparent property. If DynamicTransparent is set to None (the default), Transparent
will not be dynamically evaluated.



-------

.. _no-11565:

**DynamicVisible** 

Dynamically determine the value of the Visible property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Visible property. If DynamicVisible is set to None (the default), Visible
will not be dynamically evaluated.



-------

.. _no-11566:

**DynamicWidth** 

Dynamically determine the value of the Width property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Width property. If DynamicWidth is set to None (the default), Width
will not be dynamically evaluated.



-------

.. _no-11567:

**DynamicXpos** 

Dynamically determine the value of the Xpos property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Xpos property. If DynamicXpos is set to None (the default), Xpos
will not be dynamically evaluated.



-------

.. _no-11568:

**DynamicYpos** 

Dynamically determine the value of the Ypos property.

Specify a function and optional arguments that will get called from the
update() method. The return value of the function will get set to the
Ypos property. If DynamicYpos is set to None (the default), Ypos
will not be dynamically evaluated.



-------

.. _no-11569:

**EndAngle** 

Angle (in degrees) used to end drawing a circular or elliptic arc  (int)



-------

.. _no-11570:

**FillColor** 

Background color for the shape  (color)



-------

.. _no-11571:

**FontBold** 

Bold setting for text objects  (bool)



-------

.. _no-11572:

**FontFace** 

Face of the font used for text objects  (str)



-------

.. _no-11573:

**FontItalic** 

Italic setting for text objects  (bool)



-------

.. _no-11574:

**FontSize** 

Size of the font used for text objects  (int)



-------

.. _no-11575:

**FontUnderline** 

Underline setting for text objects  (bool)



-------

.. _no-11576:

**ForeColor** 

Color of text when using text objects  (str or tuple)



-------

.. _no-11577:

**GradientColor1** 

Top/Left color for the gradient  (color: str or tuple)



-------

.. _no-11578:

**GradientColor2** 

Bottom/Right color for the gradient  (color: str or tuple)



-------

.. _no-11579:

**HatchStyle** 

Hatching style for the fill.  (str)
            Options are:

                Solid (default)
                Transparent
                Cross
                Horizontal
                Vertical
                Diagonal
                ReverseDiagonal
                CrossDiagonal

    



-------

.. _no-11580:

**Height** 

For rectangles, the height of the shape  (int)



-------

.. _no-11581:

**LineStyle** 

Line style (solid, dash, dot) drawn  (str)



-------

.. _no-11584:

**Orientation** 

Direction of the drawn gradient ('v' or 'h')  (str)



-------

.. _no-11586:

**PenColor** 

ForeColor of the shape's lines  (color)



-------

.. _no-11587:

**PenWidth** 

Width of the shape's lines  (int)



-------

.. _no-11588:

**Points** 

Tuple of (x,y) pairs defining a polygon.  (tuple)



-------

.. _no-11589:

**Position** 

Shorthand for (Xpos, Ypos).  (2-tuple)



-------

.. _no-11591:

**Radius** 

For circles, the radius of the shape. For Rounded Rectangles,
    the radius of the rounded corner. (int)



-------

.. _no-11592:

**Rect** 

Reference to a wx.Rect that encompasses the drawn object (read-only) (wx.Rect)



-------

.. _no-11593:

**Shape** 

Type of shape to draw  (str)



-------

.. _no-11594:

**Size** 

Convenience property, equivalent to (Width, Height)  (2-tuple)



-------

.. _no-11595:

**StartAngle** 

Angle (in degrees) used to start drawing a circular or elliptic arc  (int)



-------

.. _no-11596:

**Text** 

Text to be drawn  (str)



-------

.. _no-11597:

**Transparent** 

Should the bitmap be drawn transparently?  (bool)



-------

.. _no-11598:

**Visible** 

Controls whether the shape is drawn.  (bool)



-------

.. _no-11599:

**Width** 

For rectangles, the width of the shape  (int)



-------

.. _no-11600:

**Xpos** 

For circles, the x position of the center. For rectangles,
    the x position of the top left corner. (int)



-------

.. _no-11601:

**Ypos** 

For circles, the y position of the center. For rectangles,
    the y position of the top left corner. (int)



-------


Properties - inherited
========================

.. _no-11534:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11536:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11537:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11539:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11582:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11583:

**Name** 

The name of the object.  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11585:

**Parent** 

Reference to the object being drawn upon.  (object)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11590:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------


|method_summary| Events Summary
===============================


========== ========================

========== ========================


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`afterInit <no-11602>`             Subclass hook. Called after the object's __init__ has run fully.
:ref:`autoBindEvents <no-11603>`        Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-11604>`            Subclass hook. Called before the object is fully instantiated.
:ref:`bindEvent <no-11605>`             Bind a dEvent to a callback function.
:ref:`bindEvents <no-11606>`            Bind a sequence of [dEvent, callback] lists.
:ref:`bringToFront <no-11607>`          
:ref:`draw <no-11608>`                  Does the actual drawing.
:ref:`getAbsoluteName <no-11609>`       Return the fully qualified name of the object.
:ref:`getProperties <no-11610>`         Returns a dictionary of property name/value pairs.
:ref:`initEvents <no-11611>`            Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-11612>`        Hook for subclasses. User subclasses should set properties
:ref:`moveDown <no-11613>`              
:ref:`moveUp <no-11614>`                
:ref:`raiseEvent <no-11615>`            Send the event to all registered listeners.
:ref:`release <no-11616>`               
:ref:`sendToBack <no-11617>`            
:ref:`setProperties <no-11618>`         Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-11619>` Sets a group of properties on the object all at once. This
:ref:`super <no-11620>`                 This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-11621>`           Remove a previously registered event binding.
:ref:`update <no-11622>`                

======================================= ========================


Methods
=======

.. _no-11607:

.. function:: dabo.ui.uiwx.dPemMixin.DrawObject.bringToFront(self)



-------

.. _no-11608:

.. function:: dabo.ui.uiwx.dPemMixin.DrawObject.draw(self, dc=None)

   
   Does the actual drawing.
   
   NOTE: it does not clear any old drawings of the shape, so this shouldn't be
   called except as part of a method of the parent that first clears the
   background.
   



-------

.. _no-11613:

.. function:: dabo.ui.uiwx.dPemMixin.DrawObject.moveDown(self, levels=1)



-------

.. _no-11614:

.. function:: dabo.ui.uiwx.dPemMixin.DrawObject.moveUp(self, levels=1)



-------

.. _no-11616:

.. function:: dabo.ui.uiwx.dPemMixin.DrawObject.release(self)



-------

.. _no-11617:

.. function:: dabo.ui.uiwx.dPemMixin.DrawObject.sendToBack(self)



-------

.. _no-11622:

.. function:: dabo.ui.uiwx.dPemMixin.DrawObject.update(self)



-------


Methods - inherited
=====================

.. _no-11602:

.. function:: dabo.ui.uiwx.dPemMixin.DrawObject.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11603:

.. function:: dabo.ui.uiwx.dPemMixin.DrawObject.autoBindEvents(self, force=True)
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

.. _no-11604:

.. function:: dabo.ui.uiwx.dPemMixin.DrawObject.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11605:

.. function:: dabo.ui.uiwx.dPemMixin.DrawObject.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-11606:

.. function:: dabo.ui.uiwx.dPemMixin.DrawObject.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-11609:

.. function:: dabo.ui.uiwx.dPemMixin.DrawObject.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11610:

.. function:: dabo.ui.uiwx.dPemMixin.DrawObject.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-11611:

.. function:: dabo.ui.uiwx.dPemMixin.DrawObject.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11612:

.. function:: dabo.ui.uiwx.dPemMixin.DrawObject.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11615:

.. function:: dabo.ui.uiwx.dPemMixin.DrawObject.raiseEvent(self, eventClass, uiEvent=None, \*args, \**kwargs)
   :noindex:


   
   Send the event to all registered listeners.
   
   If uiEvent is sent, dEvents.Event will be able to parse it for useful
   information to send along to the callback.
   
   Additional arguments, if any, are sent along to the constructor    of the
   event. While this feature exists so that UI-lib event handlers can pass
   along information (such as the keystroke information in a key event), user
   code may pass along additional arguments as well, which    will exist in the
   event.EventData dictionary property.
   
   In most cases, user code should call raiseEvent() with
   the event class (dEvents.Hit, for example) as the only parameter.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-11618:

.. function:: dabo.ui.uiwx.dPemMixin.DrawObject.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-11619:

.. function:: dabo.ui.uiwx.dPemMixin.DrawObject.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-11620:

.. function:: dabo.ui.uiwx.dPemMixin.DrawObject.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-11621:

.. function:: dabo.ui.uiwx.dPemMixin.DrawObject.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------


|
