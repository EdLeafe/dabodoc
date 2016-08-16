
.. include:: _static/headings.txt

.. module:: dabo.dEvents

.. _dabo.dEvents.Idle:

=====================================
|doc_title|  **dEvents.Idle** - class
=====================================

Occurs when the event loop has no active events to process.

This is a good place to put redraw or other such UI-intensive code, so that it
will only run when the application is otherwise not busy doing other (more
important) things.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **Idle**

.. inheritance-diagram:: Idle


|supclasses| Known Superclasses
===============================

* :ref:`dabo.dEvents.dEvent`



|API| Class API
===============


.. autoclass:: dabo.dEvents.Idle


|
