
.. include:: _static/headings.txt

.. module:: dabo.lib.reportWriter

.. _dabo.lib.reportWriter.ReportWriter:

==================================================
|doc_title|  **reportWriter.ReportWriter** - class
==================================================

Reads a report form specification, iterates over a data cursor, and
outputs a pdf file. Allows for lots of fine-tuned control over layout, and
dynamic evaluation of object properties. Works with the concept of bands,
letting the designer lay out the page header, footer, groups, and detail
separately.

At runtime, you feed ReportWriter a data cursor (a list of dictionaries
where each list index is a 'row' and each dictionary key is a 'field'.)
The detail band will print once for every row.

Define your properties in the report form specification file, which is
either xml or pure Python, depending on your preferences. There are (will
be) examples of both types of specification files here. In the future
there will be a Dabo Report Designer that will create the xml report form
specification files for you.

In the context of a running report, the property values of the specification
can refer to 'self', which is the ReportWriter instance. Thus, you can use
the self instance to get to whatever value you want for the property.

For example, to get the value of a field to print in your detail band, just
put a string object into the detail band, positioned and sized how you want,
and set the 'expr' property to refer to the field. If the field name is
'cArtist', the expr for the string object would be 'self.Record["cArtist"]'.

You'll need to craft denormalized data, as ReportWriter only wants to operate
on a single table and there is no provision for relating one table to another.
This is, IMO, the right way to go anyway, offering the most control and
flexibility yet still keeping it really simple. Just have the calling program
get the data denormalized into one cursor, and then call ReportWriter
feeding it the Cursor, Report Form, and OutputFile.

More documentation will come.




|subclasses| Known Subclasses
=============================

* :ref:`dabo.dReportWriter.dReportWriter`



|API| Class API
===============


.. autoclass:: dabo.lib.reportWriter.ReportWriter


|
