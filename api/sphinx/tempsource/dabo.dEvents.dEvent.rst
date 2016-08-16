
.. include:: _static/headings.txt

.. module:: dabo.dEvents

.. _dabo.dEvents.dEvent:

=======================================
|doc_title|  **dEvents.dEvent** - class
=======================================

Base class for Dabo events.

Event objects are instantiated in self.raiseEvent(), and passed to all
callbacks registered with self.bindEvent().

User code can define custom events by simply subclassing Event and then
using self.bindEvent() and self.raiseEvent() in your objects.




|subclasses| Known Subclasses
=============================

* :ref:`dabo.dEvents.Activate`
* :ref:`dabo.dEvents.BackgroundErased`
* :ref:`dabo.dEvents.CalendarEvent`
* :ref:`dabo.dEvents.ChildBorn`
* :ref:`dabo.dEvents.Close`
* :ref:`dabo.dEvents.ContextMenu`
* :ref:`dabo.dEvents.ControlNavigationEvent`
* :ref:`dabo.dEvents.Create`
* :ref:`dabo.dEvents.DataEvent`
* :ref:`dabo.dEvents.Deactivate`
* :ref:`dabo.dEvents.Destroy`
* :ref:`dabo.dEvents.EditorEvent`
* :ref:`dabo.dEvents.FontPropertiesChanged`
* :ref:`dabo.dEvents.GotFocus`
* :ref:`dabo.dEvents.GridEvent`
* :ref:`dabo.dEvents.Hit`
* :ref:`dabo.dEvents.HtmlLinkClicked`
* :ref:`dabo.dEvents.Idle`
* :ref:`dabo.dEvents.InteractiveChange`
* :ref:`dabo.dEvents.KeyEvent`
* :ref:`dabo.dEvents.ListControlEvent`
* :ref:`dabo.dEvents.LostFocus`
* :ref:`dabo.dEvents.MediaEvent`
* :ref:`dabo.dEvents.MenuEvent`
* :ref:`dabo.dEvents.MouseEvent`
* :ref:`dabo.dEvents.Move`
* :ref:`dabo.dEvents.PageChanged`
* :ref:`dabo.dEvents.PageChanging`
* :ref:`dabo.dEvents.PageClosed`
* :ref:`dabo.dEvents.PageClosing`
* :ref:`dabo.dEvents.PageContextMenu`
* :ref:`dabo.dEvents.PageEnter`
* :ref:`dabo.dEvents.PageLeave`
* :ref:`dabo.dEvents.Paint`
* :ref:`dabo.dEvents.ReportEvent`
* :ref:`dabo.dEvents.Resize`
* :ref:`dabo.dEvents.SashEvent`
* :ref:`dabo.dEvents.ScrollEvent`
* :ref:`dabo.dEvents.SearchButtonClicked`
* :ref:`dabo.dEvents.SearchCancelButtonClicked`
* :ref:`dabo.dEvents.ShellCommandRun`
* :ref:`dabo.dEvents.SlidePanelCaptionClick`
* :ref:`dabo.dEvents.SlidePanelChange`
* :ref:`dabo.dEvents.SpinnerEvent`
* :ref:`dabo.dEvents.TreeEvent`
* :ref:`dabo.dEvents.Update`
* :ref:`dabo.dEvents.ValueChanged`



|API| Class API
===============


.. autoclass:: dabo.dEvents.dEvent

   .. automethod:: dabo.dEvents.dEvent.__init__

|
