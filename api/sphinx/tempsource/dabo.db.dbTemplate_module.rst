
.. include:: _static/headings.txt

.. module:: dabo.db.dbTemplate

.. _dabo.db.dbTemplate:

==================================
|doc_title|  **dbTemplate module**
==================================

|

.. highlight:: python


This is a template for creating new backend-specific scripts. To create
a script to support a database not yet suppported by Dabo, make a copy
of this file in the dabo/db directory, and name the copy 'dbProduct.py',
where 'Product' is the actual name of the database (e.g., dbMySQL.py,
dbFirebird.py, etc.)

This template uses 'NEWDATABASE' as the name of the database; you
should replace this with the actual name of the database
(e.g., Oracle, PostgreSQL, etc.)

Then go down through each section marked with TODO comments, and
modify the code so that it works correctly for this particular database. As
soon as you know that it works, remove the TODO comment, and replace it
with anything that might be relevant.

These database-specific scripts are designed to abstract out those parts
of the code that can vary among the various products out there. By
customizing the code in these methods, the standard cursor works great
in the framework with any database backend. However, if you find
something about your database that simply can't be fixed by
customizing these methods, report it to the dabo-dev list; it may require
some refactoring of the code to handle a situation that is unique to this
particular database.


.. moduleauthor:: Dabo community <dabo-users@leafe.com>






|class_summary| Class Summary
=============================



Module Summary
==============

.. toctree::
   :glob:
   :maxdepth: 1

   dabo.db.dbTemplate*


|
