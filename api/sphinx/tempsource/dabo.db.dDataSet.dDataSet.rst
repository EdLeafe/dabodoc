
.. include:: _static/headings.txt

.. module:: dabo.db.dDataSet

.. _dabo.db.dDataSet.dDataSet:

==========================================
|doc_title|  **dDataSet.dDataSet** - class
==========================================

This class assumes that its contents are not ordinary tuples, but
rather tuples consisting of dicts, where the dict keys are field names.
This is the data structure returned by the dCursorMixin class.

It is used to give these data sets the ability to be queried, joined, etc.
This is accomplished by using SQLite in-memory databases. If SQLite
and pysqlite2 are not installed on the machine this is run on, a
warning message will be printed out and the SQL functions will return
None. The data will still be usable, though.




|API| Class API
===============


.. autoclass:: dabo.db.dDataSet.dDataSet

   .. automethod:: dabo.db.dDataSet.dDataSet.__init__

|
