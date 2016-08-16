
.. include:: _static/headings.txt

.. module:: dabo.dEvents

.. _dabo.dEvents.RowNavigation:

==============================================
|doc_title|  **dEvents.RowNavigation** - class
==============================================

Occurs when the PrimaryBizobj of the dForm is being navigated.

As the user is rapidly calling dForm.next(), .prior(), etc., RowNavigation
events get raised. Your code should do some quick display updates to indicate
to the user that the record is changing, but the child bizobj's won't be
requeried until after the navigation has ended.

See also RowNumChanged, which only occurs after the user has settled on a
record and has stopped navigating.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **RowNavigation**

.. inheritance-diagram:: RowNavigation


|supclasses| Known Superclasses
===============================

* :ref:`dabo.dEvents.DataEvent`



|API| Class API
===============


.. autoclass:: dabo.dEvents.RowNavigation


|
