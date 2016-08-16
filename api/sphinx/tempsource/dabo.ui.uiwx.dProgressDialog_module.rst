
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.dProgressDialog

.. _dabo.ui.uiwx.dProgressDialog:

=======================================
|doc_title|  **dProgressDialog module**
=======================================

|

.. highlight:: python


(Barely started - don't use)

Ed writes:

The whole threading issue. Since killing threads is not
feasible, we should look at what we want to accomplish.
Ideally, we want to avoid locking the UI by a runaway query
process. Given that, we should rewrite all potentially
runaway calls in the UI to the bizobj so that we begin by
creating a separate thread for the bizobj call. The UI then
starts a timer, which will display a "Please Wait" message
with a Cancel button after a given time (say, 1 second). If
the user clicks Cancel, the UI continues on its way. Further
interaction with the bizobj will not be possible until the
bizobj process returns, since its state will be undefined. We
then need a UI-level flag to be set to indicate this state.
The bizobj returns from its process by emitting an event; the
UI will have to trap that event, and if it is received when
the flag is set, issue a call to the bizobj to reset itself
back to its last known state. When the bizobj completes that,
the UI clears the 'unstable' flag. This will require, of
course, that the bizobj save its state before each call, and
be able to restore that state when asked. None of this will
eliminate problems caused by runaway queries, but will at
least allow the UI to remain responsive, reducing the chance
that the user will three-finger it.


.. moduleauthor:: Dabo community <dabo-users@leafe.com>






|method_summary| Function Summary
=================================


* :meth:`~dabo.ui.uiwx.dProgressDialog.EVT_EXCEPTION`
* :meth:`~dabo.ui.uiwx.dProgressDialog.EVT_RESULT`
* :meth:`~dabo.ui.uiwx.dProgressDialog.displayAfterWait`



|class_summary| Class Summary
=============================



Module Summary
==============

.. toctree::
   :glob:
   :maxdepth: 1

   dabo.ui.uiwx.dProgressDialog*


|
