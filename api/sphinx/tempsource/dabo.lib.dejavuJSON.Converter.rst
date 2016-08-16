
.. include:: _static/headings.txt

.. module:: dabo.lib.dejavuJSON

.. _dabo.lib.dejavuJSON.Converter:

=============================================
|doc_title|  **dejavuJSON.Converter** - class
=============================================

Provides two-way conversion of Units/JSON via loads and dumps methods.

Also converts datetime.date, datetime.time, datetime.datetime and
decimal.Decimal to/from JSON.

This is accomplished by the Encoder and Decoder classes, which are
subclasses of their counterparts in simplejson.     If you wish to change
the output of the converter at all, you should probably subclass the
Encoder/Decoder and then make a cusom Converter subclass with your
encoder/decoder as class attributes.




|API| Class API
===============


.. autoclass:: dabo.lib.dejavuJSON.Converter

   .. automethod:: dabo.lib.dejavuJSON.Converter.__init__

|
