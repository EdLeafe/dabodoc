
.. include:: _static/headings.txt

.. module:: dabo.dEvents

.. _dabo.dEvents.DocumentationHint:

==================================================
|doc_title|  **dEvents.DocumentationHint** - class
==================================================

Occurs when the editor wants documentation information to change.

The IDE can bind to this to direct detailed documentation into a separate
window, likely replacing previous documentation. The user can choose how
to display that window, if at all.

Raise this event with three additional keyword arguments:
+ shortDoc: a one-liner call tip
+ longDoc: a multi-line call tip plus expanded documentation
+ object: a reference to the object to be documented, in case
the listener wants to format additional information about
the object.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **DocumentationHint**

.. inheritance-diagram:: DocumentationHint


|supclasses| Known Superclasses
===============================

* :ref:`dabo.dEvents.EditorEvent`



|API| Class API
===============


.. autoclass:: dabo.dEvents.DocumentationHint


|
