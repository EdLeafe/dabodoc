
.. include:: _static/headings.txt

.. module:: dabo.db

.. _dabo.db:

===========================
|doc_title|  **db package**
===========================

|

.. highlight:: python


dabo.db is the lowest tier, db access.

This is where the communication to and from the backend database happens, and
cursors get generated to be manipulated by the bizobj's in dabo.biz.

dabo.biz.dBiz is the entity that will interact with this dabo.db stuff, but you
can also work with dabo.db directly if you want. Perhaps you just want to read
some rows from a backend database in a script. Here's an example of that::

    from connectInfo import ConnectInfo
    from dConnection import dConnection

    ci = ConnectInfo('MySQL')
    ci.host = 'paulmcnett.com'
    ci.dbName = "house"
    ci.user = 'dabo'
    ci.password = 'dabo'

    conn = dConnection(ci).getConnection()
    cursor = conn.cursor()
    print cursor.execute("select * from addressbook order by iid limit 10")
    for row in cursor.fetchall():
        print row[0], row[1]



.. moduleauthor:: Dabo community <dabo-users@leafe.com>




Module Summary
==============

.. toctree::
   :glob:
   :maxdepth: 1

   dabo.db*


|
