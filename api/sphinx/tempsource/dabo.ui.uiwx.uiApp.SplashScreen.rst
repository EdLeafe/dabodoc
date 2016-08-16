
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.uiApp

.. _dabo.ui.uiwx.uiApp.SplashScreen:

===========================================
|doc_title|  **uiApp.SplashScreen** - class
===========================================


This is a specialized form that is meant to be used as a startup
splash screen. It takes an image file, bitmap, icon, etc., which is used
to size and shape the form. If you specify a mask color, that color
will be masked in the bitmap to appear transparent, and will affect the
shape of the form.

You may also pass a 'timeout' value; this is in milliseconds, and determines
how long until the splash screen automatically closes. If you pass zero
(or don't pass anything), the screen will remain visible until the user
clicks on it.

Many thanks to Andrea Gavana, whose 'AdvancedSplash' class was a
huge inspiration (and source of code!) for this Dabo class. I also borrowed
some ideas/code from the wxPython demo by Robin Dunn.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **SplashScreen**

.. inheritance-diagram:: SplashScreen


|supclasses| Known Superclasses
===============================




|API| Class API
===============


.. autoclass:: dabo.ui.uiwx.uiApp.SplashScreen
   :members:

   .. automethod:: dabo.ui.uiwx.uiApp.SplashScreen.__init__

|
