
.. include:: _static/headings.txt

.. module:: dabo.lib.profilehooks

.. _dabo.lib.profilehooks:

====================================
|doc_title|  **profilehooks module**
====================================

|

.. highlight:: python


Profiling hooks

This module contains a couple of decorators (`profile` and `coverage`) that
can be used to wrap functions and/or methods to produce profiles and line
coverage reports.

Usage example (Python 2.4 or newer)::

    from profilehooks import profile, coverage

    @profile    # or @coverage
    def fn(n):
        if n < 2: return 1
        else: return n * fn(n-1)

    print fn(42)

Usage example (Python 2.3 or older)::

    from profilehooks import profile, coverage

    def fn(n):
        if n < 2: return 1
        else: return n * fn(n-1)

    # Now wrap that function in a decorator
    fn = profile(fn) # or coverage(fn)

    print fn(42)

Reports for all thusly decorated functions will be printed to sys.stdout
on program termination.  You can alternatively request for immediate
reports for each call by passing immediate=True to the profile decorator.

There's also a @timecall decorator for printing the time to sys.stderr
every time a function is called, when you just want to get a rough measure
instead of a detailed (but costly) profile.

Caveats

  A thread on python-dev convinced me that hotshot produces bogus numbers.
  See http://mail.python.org/pipermail/python-dev/2005-November/058264.html

  I don't know what will happen if a decorated function will try to call
  another decorated function.  All decorators probably need to explicitly
  support nested profiling (currently TraceFuncCoverage is the only one that
  supports this, while HotShotFuncProfile has support for recursive functions.)

  Profiling with hotshot creates temporary files (\*.prof and \*.prof.pickle for
  profiling, \*.cprof for coverage) in the current directory.  These files are
  not cleaned up.  (In fact, the \*.pickle versions are intentionally written
  out in case you want to look at the profiler results without having to parse
  the big \*.prof file with hotshot.stats.load, which takes ages.  Just unpickle
  the file and you'll get a pstats object.)

  Coverage analysis with hotshot seems to miss some executions resulting in
  lower line counts and some lines errorneously marked as never executed.  For
  this reason coverage analysis now uses trace.py which is slower, but more
  accurate.

  Decorating functions causes doctest.testmod() to ignore doctests in those
  functions.

Copyright (c) 2004--2006 Marius Gedminas <marius@pov.lt>

Released under the MIT licence since December 2006:

    Permission is hereby granted, free of charge, to any person obtaining a
    copy of this software and associated documentation files (the "Software"),
    to deal in the Software without restriction, including without limitation
    the rights to use, copy, modify, merge, publish, distribute, sublicense,
    and/or sell copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
    DEALINGS IN THE SOFTWARE.

(Previously it was distributed under the GNU General Public Licence.)


.. moduleauthor:: Dabo community <dabo-users@leafe.com>






|method_summary| Function Summary
=================================


* :meth:`~dabo.lib.profilehooks.coverage`
* :meth:`~dabo.lib.profilehooks.coverage_with_hotshot`
* :meth:`~dabo.lib.profilehooks.profile`
* :meth:`~dabo.lib.profilehooks.timecall`

Module Summary
==============

.. toctree::
   :glob:
   :maxdepth: 1

   dabo.lib.profilehooks*


|
