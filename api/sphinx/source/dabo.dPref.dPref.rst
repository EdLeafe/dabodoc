
.. include:: _static/headings.txt

.. module:: dabo.dPref

.. _dabo.dPref.dPref:

====================================
|doc_title|  **dPref.dPref** - class
====================================

dPref is a class that is used to automatically manage preferences. It requires
SQLite in order to function; without that installed, you cannot use this class. It
automatically supports nesting of preferences; if you have a dPref object named
'basePref', and then issue the statement 'basePref.subPref.something=True', a
new dPref object named 'subPref' will be created, and can be referred to using
'basePref.subPref'.

Normally you should specify the initial key for your prefs. This will ensure that
your preference names do not conflict with other dabo preferences. This is much like
the approach to modules in the Python namespace. Failure to specify a base
key would put all of your prefs into the 'root' namespace, where collisions can more
easily happen, and thus is not allowed.

All preference assignments are automatically persisted to the database unless
the 'AutoPersist' property on this object or one of its 'ancestors' is set to False.
When that is False, you must call the persist() method manually, or your settings
will not be saved. Calling 'persist()' will write any values of that object and all of its
child objects to the database.




|API| Class API
===============


.. autoclass:: dabo.dPref.dPref

   .. automethod:: dabo.dPref.dPref.__init__

|
