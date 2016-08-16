
.. include:: _static/headings.txt

.. module:: dabo.ui.__init__

.. _dabo.ui.__init__:

================================
|doc_title|  **__init__ module**
================================

|

.. highlight:: python


This is Dabo's user interface layer which is the topmost layer.

There are submodules for all supported UI libraries. As of this writing,
the only supported UI library is wxPython (uiwx).

To use a given submodule at runtime, you need to call loadUI() with the
ui module you want as a parameter. For instance, to load wxPython, you
would issue::

    import dabo.ui
    dabo.ui.loadUI("wx")



.. moduleauthor:: Dabo community <dabo-users@leafe.com>






|method_summary| Function Summary
=================================


* :meth:`~dabo.ui.__init__.deadCheck`
* :meth:`~dabo.ui.__init__.getEventData`
* :meth:`~dabo.ui.__init__.getUIType`
* :meth:`~dabo.ui.__init__.loadUI`
* :meth:`~dabo.ui.__init__.makeDynamicProperty`
* :meth:`~dabo.ui.__init__.makeProxyProperty`

Module Summary
==============

.. toctree::
   :glob:
   :maxdepth: 1

   dabo.ui.__init__*


|
