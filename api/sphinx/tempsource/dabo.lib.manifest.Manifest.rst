
.. include:: _static/headings.txt

.. module:: dabo.lib.manifest

.. _dabo.lib.manifest.Manifest:

==========================================
|doc_title|  **manifest.Manifest** - class
==========================================

This class encapsulates all of the methods needed to create and manage
a manifest system for syncing directories.

A manifest is simply a dictionary with the keys being the file paths, and the
values being a timestamp. Two manifests, referred to as 'source' and 'target',
can be compared to find the changes required to make 'target' match 'source'.




|API| Class API
===============


.. autoclass:: dabo.lib.manifest.Manifest


|
