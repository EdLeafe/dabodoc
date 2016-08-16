.. include:: _static/headings.txt

====================
|doc_title| **Dabo**
====================

Desktop applications. That's what Dabo does. It's not YAWF (yet another web framework).
There are plenty of excellent web frameworks out there, so if that's what you are looking
for, Dabo isn't for you. But there are almost no desktop application frameworks out there,
and if you want to create applications that run on Windows, OS X or Linux, Dabo is for you!

|

.. tabularcolumns:: |C|C|C|

.. list-table::
   :header-rows: 1

   * - **Apple Mac**
     - **Windows**
     - **Linux**



   * - .. image:: _static/macWidgets/dGrid.png
          :scale: 75 %
          :target: gallery_mac.html
          :alt: dGrid on Mac



     - .. image:: _static/winWidgets/dGrid.png
          :scale: 75 %
          :target: gallery_win.html
          :alt: dGrid on Windows



     - .. image:: _static/nixWidgets/dGrid.png
          :scale: 75 %
          :target: gallery_nix.html
          :alt: dGrid on Linux

|



|table_contents| Table of Contents
==================================

|

+-----------------------------------+-----------------------------------+
| Main modules                      | Databases supported               |
+===================================+===================================+
| * :ref:`dabo.dabo`                | * :ref:`dabo.db.dbFirebird`       |
| * :ref:`dabo.biz`                 | * :ref:`dabo.db.dbMSSQL`          |
| * :ref:`dabo.db`                  | * :ref:`dabo.db.dbMySQL`          |
| * :ref:`dabo.ui`                  | * :ref:`dabo.db.dbPostgreSQL`     |
|                                   | * :ref:`dabo.db.dbSQLite`         |
+-----------------------------------+-----------------------------------+

|

=========================
|description| Description
=========================

Dabo is a 3-tier, cross-platform application development framework, written in Python atop the wxPython GUI toolkit. And while Dabo is designed to create database-centric apps, that is not a requirement. Lots of people are using Dabo for the GUI tools to create apps that have no need to connect to a database at all.


========================
|description| Background
========================

Dabo's authors, Ed Leafe and Paul McNett, have strong backgrounds in database application development using the awesome and underrated Microsoft Visual FoxPro development environment.

While Visual FoxPro shines at developing data-centric applications, it has one limitation that cannot be ignored: it only runs on Microsoft Windows, and Ed and Paul both have clients that want their applications to run on Linux and Macintosh. We are sure we are not alone in this regard: it is a multi-platform world with more diverse needs than one vendor can fulfill.

Ed and Paul got to talking one day: Paul had been researching various multiplatform GUI toolkits for about 18 months, and Ed has lots of experience developing the Visual FoxPro Codebook framework. We decided to work together to make a framework for developing robust data-centric applications for multi-platform deployment. We've come up with a design that is simple, flexible, and robust, and we've begun developing our own client applications using the Dabo framework.

===========================
|description| 3-Tier Design
===========================

We have taken what we've learned from 25 combined years of FoxPro database application development, and built an easy-to-use runtime framework that runs on all three major platforms. Dabo consists of 3 logical tiers plus an umbrella application object. The three tiers are:

======================
|description| Database
======================

Currently, Dabo supports MySQL, PostgreSQL, Firebird, Microsoft SQL Server and SQLite backends, but in the near future it will support all databases that have drivers that conform to the Python dbapi. These databases include:

    * MySQL (already supported)
    * PostgreSQL(already supported)
    * Firebird (already supported)
    * MS-SQL and MSDE (already supported)
    * SQLite (already supported)
    * Oracle
    * DB2
    * Sybase
    * Berkeley DB

============================
|description| Business Rules
============================

This tier is where all the business logic resides. You simply subclass dBizobj, set a few properties, and override a few methods. The dBizobj communicates with the database tier and the user interface tier, and enforces your business rules to your specifications.

============================
|description| User Interface
============================

You create your forms by laying out various controls or widgets, and setting properties to tell Dabo what bizobj and what field in the dataset the control represents. There is no business logic at this level, and only minimal code will be entered here: it is mostly laying out your UI design and setting properties to tell Dabo how to connect to the business rules.

Currently, the only supported UI is wxPython, but we've left it open for possible future additions of other UI libraries, such as:

    * wxPython (already supported)
    * PyQt
    * TkInter
    * Curses (text only - perhaps the computer isn't running a GUI)
    * HTTP (web server providing a browser interface)

However, wrapping a UI toolkit is a major effort, so don't hold your breath waiting for any of the other UIs - unless, of course, you want to volunteer to work with us to get it working!

============================
|description| Multi-Platform
============================

Dabo applications are known to run on all flavors of Windows, all recent flavors of Linux, and Macintosh OS X 10.2 or higher. Because Dabo is currently built on top of wxPython, which is built on top of wxWidgets, it probably runs elsewhere, too. It also suffers from the same display limitations on some platforms (most notably OS X), but these should improve as the underlying toolkits improve.

You can develop Dabo applications on all three supported platforms, and you can run your Dabo applications on all three supported platforms. Flexibility is a really good thing.

=======================
|description| Community
=======================

Visual FoxPro has a vibrant, vocal, energetic community that knows how to have a good time. From what we've seen of the Python community so far, the same goes there. We hope to provide the structure for forming a new community, a Dabo community that shares ideas and code, supports one-another, and hopefully even gets together once a year to socialize. There are mailing lists for users of Dabo and developers of Dabo, and a world-editable Dabo Wiki. We are friendly and look forward to meeting you.

Oh, and if you are a disenchanted Visual Basic developer, you've found the right place, too. 

==============================
|other_info| Other Information
==============================

Bugs and Limitations: many, patches and fixes welcome :-D

See the demo for an example of what **Dabo** can do, and on how to use it.

---------------

Copyright: Ed Leafe and Paul McNett

License: As of 11/4/2004, Dabo is licensed under the very liberal MIT License, which allows you to do whatever you want with our code, as long as the copyright notice and license terms remain intact. See http://www.dabodev.com/licensing.

---------------

SVN for latest code:
http://svn.dabodev.com/dabo/trunk/dabo

Mailing List:
dabo-users@leafe.com

---------------

Please let us know if you are using **Dabo**!

---------------

|indices| Indices and tables
============================

* :ref:`daboindex`
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Build information:
==================

:Version: |version|
:Date: |today|


.. toctree::
   :hidden:

   general_index

