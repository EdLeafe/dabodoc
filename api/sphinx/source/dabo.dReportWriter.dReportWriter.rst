
.. include:: _static/headings.txt

.. module:: dabo.dReportWriter

.. _dabo.dReportWriter.dReportWriter:

====================================================
|doc_title|  **dReportWriter.dReportWriter** - class
====================================================

The Dabo Report Writer Engine, which mixes a data cursor and a report
format file (.rfxml) to output a PDF.

For each row in the Cursor, a detail band is printed. For each page in the
report, the pageBackground, pageHeader, pageFooter, and pageForeground
bands are printed. For each defined grouping, the groupHeader and groupFooter
bands are printed.

Report variables can be defined as accumulators, or for any purpose you
need. All properties of the report form are evaluated at runtime, so that
you can achieve full flexibility and ultimate control.

There is also a pure-python interface available.




|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dReportWriter**

.. inheritance-diagram:: dReportWriter


|supclasses| Known Superclasses
===============================

* :ref:`dabo.dObject.dObject`
* :ref:`dabo.lib.reportWriter.ReportWriter`



|API| Class API
===============


.. autoclass:: dabo.dReportWriter.dReportWriter


|method_summary| Properties Summary
===================================


================================ ========================
:ref:`Application <no-35>`       Read-only object reference to the Dabo Application object.  (dApp).
:ref:`BaseClass <no-36>`         The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-37>`       Base key used when saving/restoring preferences  (str)
:ref:`Class <no-38>`             The class the object is based on. Read-only.  (class)
:ref:`Encoding <no-39>`          Specifies the encoding for unicode strings.  (str)
:ref:`HomeDirectory <no-40>`     Specifies the home directory for the report.
:ref:`LogEvents <no-41>`         Specifies which events to log.  (list of strings)
:ref:`Name <no-42>`              The name of the object.  (str)
:ref:`Parent <no-43>`            The containing object.  (obj)
:ref:`PreferenceManager <no-44>` Reference to the Preference Management object  (dPref)
:ref:`ProgressControl <no-45>`   Specifies the control to receive progress updates.

================================ ========================


Properties
==========

.. _no-45:

**ProgressControl** 

Specifies the control to receive progress updates.

The specified control will be updated with every record processed. It must have
a updateProgress(current_row, num_rows) method.

For the default control, use dabo.ui.dReportProgress.




-------


Properties - inherited
========================

.. _no-35:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-36:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-37:

**BasePrefKey** 

Base key used when saving/restoring preferences  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-38:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-39:

**Encoding** 

Specifies the encoding for unicode strings.  (str)


Inherited from: :ref:`dabo.lib.reportWriter.ReportWriter`

-------

.. _no-40:

**HomeDirectory** 

Specifies the home directory for the report.

Resources on disk (image files, etc.) will be looked for relative to the
HomeDirectory if specified with relative pathing. The HomeDirectory should
be the directory that contains the report form file. If you set
self.ReportFormFile, HomeDirectory will be set for you automatically.
Otherwise, it will get set to self.Application.HomeDirectory.


Inherited from: :ref:`dabo.lib.reportWriter.ReportWriter`

-------

.. _no-41:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-42:

**Name** 

The name of the object.  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-43:

**Parent** 

The containing object.  (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-44:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------


|method_summary| Events Summary
===============================


============================== ========================
:ref:`ReportBegin <no-46>`     Occurs at the beginning of the report.
:ref:`ReportCancel <no-47>`    Occurs when the user cancels the report.
:ref:`ReportEnd <no-48>`       Occurs at the end of the report.
:ref:`ReportEvent <no-49>`     
:ref:`ReportIteration <no-50>` Occurs when the RecordNumber changes at report runtime.

============================== ========================


Events
=======

.. _no-46:

**ReportBegin** 

Occurs at the beginning of the report.



-------

.. _no-47:

**ReportCancel** 

Occurs when the user cancels the report.



-------

.. _no-48:

**ReportEnd** 

Occurs at the end of the report.



-------

.. _no-49:

**ReportEvent** 



-------

.. _no-50:

**ReportIteration** 

Occurs when the RecordNumber changes at report runtime.



-------


|method_summary| Methods Summary
================================


========================================= ========================
:ref:`afterInit <no-51>`                  Subclass hook. Called after the object's __init__ has run fully.
:ref:`autoBindEvents <no-52>`             Automatically bind any on*() methods to the associated event.
:ref:`beforeInit <no-53>`                 Subclass hook. Called before the object is fully instantiated.
:ref:`bindEvent <no-54>`                  Bind a dEvent to a callback function.
:ref:`bindEvents <no-55>`                 Bind a sequence of [dEvent, callback] lists.
:ref:`cancel <no-56>`                     Cancel the report printout on the next iteration of self.Cursor.
:ref:`clearSpanningObjects <no-57>`       
:ref:`convertParagraphsToMemos <no-58>`   Converts all Paragraph objects to Memo objects.
:ref:`draw <no-59>`                       Draw the given object on the Canvas.
:ref:`drawPageCounts <no-60>`             
:ref:`drawSpanningObjects <no-61>`        Draw all spanning objects. Called when page is changing or group is ending.
:ref:`getAbsoluteName <no-62>`            Return the fully qualified name of the object.
:ref:`getBandHeight <no-63>`              Return the height of the band.
:ref:`getColorTupleFromReportLab <no-64>` Given a color tuple in reportlab format (values between 0 and 1), return
:ref:`getFramesetCount <no-65>`           Returns the number of framesets in the report.
:ref:`getFramesets <no-66>`               Returns a list of (idx, frameset, band) for every frameset in the report.
:ref:`getPageSize <no-67>`                
:ref:`getProperties <no-68>`              Returns a dictionary of property name/value pairs.
:ref:`getPt <no-69>`                      Given a string or a number, convert the value into a numeric pt value.
:ref:`getReportLabColorTuple <no-70>`     Given a color tuple in rgb format (values between 0 and 255), return
:ref:`getStory <no-71>`                   
:ref:`initEvents <no-72>`                 Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-73>`             Hook for subclasses. User subclasses should set properties
:ref:`printBandOutline <no-74>`           
:ref:`ptToUnit <no-75>`                   Given a numeric pt like 36, return a string like '0.5 in'.
:ref:`raiseEvent <no-76>`                 Send the event to all registered listeners.
:ref:`save <no-77>`                       
:ref:`setProperties <no-78>`              Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-79>`      Sets a group of properties on the object all at once. This
:ref:`storeSpanningObject <no-80>`        Store the passed spanning object for printing when the group or
:ref:`storeUndo <no-81>`                  
:ref:`super <no-82>`                      This method used to call superclass code, but it's been removed.
:ref:`unbindEvent <no-83>`                Remove a previously registered event binding.
:ref:`undo <no-84>`                       
:ref:`write <no-85>`                      Write the PDF file based on the ReportForm spec.

========================================= ========================


Methods - inherited
=====================

.. _no-51:

.. function:: dabo.dReportWriter.dReportWriter.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-52:

.. function:: dabo.dReportWriter.dReportWriter.autoBindEvents(self, force=True)
   :noindex:


   
   Automatically bind any on*() methods to the associated event.
   
   User code only needs to define the callback, and Dabo will automatically
   set up the event binding. This will satisfy lots of common cases where
   you want an object or its parent to respond to the object's events.
   
   To use this feature, just define a method on<EventName>(), or    if you
   want a parent container to respond to the event, make a method in the
   parent on<EventName>_<object Name or RegID>().
   
   For example::
   
       class MyButton(dabo.ui.dButton):
           def onHit(self, evt):
               print "Hit!"
   
       class MyPanel(dabo.ui.dPanel):
           def afterInit(self):
               self.addObject(MyButton, RegID="btn1")
   
           def onHit_btn1(self, evt):
               print "panel: button hit!"
   
   When the button is pressed, you'll see both 'hit' messages because of
   auto event binding.
   
   If you want to bind your events explicitly, you can turn off auto event
   binding by issuing::
   
        dabo.autoBindEvents = False
   
   This feature is inspired by PythonCard.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-53:

.. function:: dabo.dReportWriter.dReportWriter.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-54:

.. function:: dabo.dReportWriter.dReportWriter.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-55:

.. function:: dabo.dReportWriter.dReportWriter.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-56:

.. function:: dabo.dReportWriter.dReportWriter.cancel(self)
   :noindex:


   Cancel the report printout on the next iteration of self.Cursor.


Inherited from: :ref:`dabo.lib.reportWriter.ReportWriter`

-------

.. _no-57:

.. function:: dabo.dReportWriter.dReportWriter.clearSpanningObjects(self, group=None)
   :noindex:



Inherited from: :ref:`dabo.lib.reportWriter.ReportWriter`

-------

.. _no-58:

.. function:: dabo.dReportWriter.dReportWriter.convertParagraphsToMemos(self)
   :noindex:


   Converts all Paragraph objects to Memo objects.


Inherited from: :ref:`dabo.lib.reportWriter.ReportWriter`

-------

.. _no-59:

.. function:: dabo.dReportWriter.dReportWriter.draw(self, obj, origin=(0, 0), availableHeight=None, deferred=None)
   :noindex:


   Draw the given object on the Canvas.
   
   The object is a dictionary containing properties, and    origin is the (x,y)
   tuple where the object will be drawn.
   
   availableHeight is the height available on the current page; deferred is
   the contents of the object partially printed on the last page that needs
   to continue printing now (paragraph story).
   


Inherited from: :ref:`dabo.lib.reportWriter.ReportWriter`

-------

.. _no-60:

.. function:: dabo.dReportWriter.dReportWriter.drawPageCounts(self, pageNum, pageCount)
   :noindex:



Inherited from: :ref:`dabo.lib.reportWriter.ReportWriter`

-------

.. _no-61:

.. function:: dabo.dReportWriter.dReportWriter.drawSpanningObjects(self, origin=(0, 0), group=None)
   :noindex:


   Draw all spanning objects. Called when page is changing or group is ending.


Inherited from: :ref:`dabo.lib.reportWriter.ReportWriter`

-------

.. _no-62:

.. function:: dabo.dReportWriter.dReportWriter.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-63:

.. function:: dabo.dReportWriter.dReportWriter.getBandHeight(self, bandDict)
   :noindex:


   Return the height of the band.
   
   If the band's Height property is None, the height will be
   calculated based on the objects in the band.
   


Inherited from: :ref:`dabo.lib.reportWriter.ReportWriter`

-------

.. _no-64:

.. function:: dabo.dReportWriter.dReportWriter.getColorTupleFromReportLab(self, val)
   :noindex:


   Given a color tuple in reportlab format (values between 0 and 1), return
   a color tuple in 0-255 format.


Inherited from: :ref:`dabo.lib.reportWriter.ReportWriter`

-------

.. _no-65:

.. function:: dabo.dReportWriter.dReportWriter.getFramesetCount(self)
   :noindex:


   Returns the number of framesets in the report.


Inherited from: :ref:`dabo.lib.reportWriter.ReportWriter`

-------

.. _no-66:

.. function:: dabo.dReportWriter.dReportWriter.getFramesets(self)
   :noindex:


   Returns a list of (idx, frameset, band) for every frameset in the report.
   
   idx is the position in the Objects list for whatever band the
   frameset is part of.
   


Inherited from: :ref:`dabo.lib.reportWriter.ReportWriter`

-------

.. _no-67:

.. function:: dabo.dReportWriter.dReportWriter.getPageSize(self)
   :noindex:



Inherited from: :ref:`dabo.lib.reportWriter.ReportWriter`

-------

.. _no-68:

.. function:: dabo.dReportWriter.dReportWriter.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
   :noindex:


   
   Returns a dictionary of property name/value pairs.
   
   If a sequence of properties is passed, just those property values
   will be returned. Otherwise, all property values will be returned.
   The sequence of properties can be a list, tuple, or plain string
   positional arguments. For instance, all of the following are
   equivilent::
   
       print self.getProperties("Caption", "FontInfo", "Form")
       print self.getProperties(["Caption", "FontInfo", "Form"])
       t = ("Caption", "FontInfo", "Form")
       print self.getProperties(t)
       print self.getProperties(\*t)
   
   An exception will be raised if any passed property names don't
   exist, aren't actual properties, or are not readable (do not have
   getter functions).
   
   However, if an exception is raised from the property getter function,
   the exception will get caught and used as the property value in the
   returned property dictionary. This allows the property list to be
   returned even if some properties can't be evaluated correctly by the
   object yet.
   


Inherited from: :ref:`dabo.lib.propertyHelperMixin.PropertyHelperMixin`

-------

.. _no-69:

.. function:: dabo.dReportWriter.dReportWriter.getPt(self, val)
   :noindex:


   Given a string or a number, convert the value into a numeric pt value.
   
   Strings can have the unit appended, like "3.5 in", "2 cm", "3 pica", "10 mm".
   
   > print self.getPt("1 in")
   72
   > print self.getPt("1")
   1
   > print self.getPt(1)
   1
   


Inherited from: :ref:`dabo.lib.reportWriter.ReportWriter`

-------

.. _no-70:

.. function:: dabo.dReportWriter.dReportWriter.getReportLabColorTuple(self, val)
   :noindex:


   Given a color tuple in rgb format (values between 0 and 255), return
   a color tuple in reportlab 0-1 format.


Inherited from: :ref:`dabo.lib.reportWriter.ReportWriter`

-------

.. _no-71:

.. function:: dabo.dReportWriter.dReportWriter.getStory(self, obj, overrideExpr=None, overrideFontSize=None, availableHeight=None)
   :noindex:



Inherited from: :ref:`dabo.lib.reportWriter.ReportWriter`

-------

.. _no-72:

.. function:: dabo.dReportWriter.dReportWriter.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-73:

.. function:: dabo.dReportWriter.dReportWriter.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-74:

.. function:: dabo.dReportWriter.dReportWriter.printBandOutline(self, band, x, y, width, height)
   :noindex:



Inherited from: :ref:`dabo.lib.reportWriter.ReportWriter`

-------

.. _no-75:

.. function:: dabo.dReportWriter.dReportWriter.ptToUnit(self, pt, unit)
   :noindex:


   Given a numeric pt like 36, return a string like '0.5 in'.
   
   Warning, this isn't exact, and isn't intended to be.
   


Inherited from: :ref:`dabo.lib.reportWriter.ReportWriter`

-------

.. _no-76:

.. function:: dabo.dReportWriter.dReportWriter.raiseEvent(self, eventClass, uiEvent=None, \*args, \**kwargs)
   :noindex:


   
   Send the event to all registered listeners.
   
   If uiEvent is sent, dEvents.Event will be able to parse it for useful
   information to send along to the callback.
   
   Additional arguments, if any, are sent along to the constructor    of the
   event. While this feature exists so that UI-lib event handlers can pass
   along information (such as the keystroke information in a key event), user
   code may pass along additional arguments as well, which    will exist in the
   event.EventData dictionary property.
   
   In most cases, user code should call raiseEvent() with
   the event class (dEvents.Hit, for example) as the only parameter.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-77:

.. function:: dabo.dReportWriter.dReportWriter.save(self)
   :noindex:



Inherited from: :ref:`dabo.lib.reportWriter.ReportWriter`

-------

.. _no-78:

.. function:: dabo.dReportWriter.dReportWriter.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
   :noindex:


   
   Sets a group of properties on the object all at once.
   
   You have the following options for sending the properties:
   
       1) Property/Value pair dictionary
       2) Keyword arguments
       3) Both
   
   The following examples all do the same thing::
   
       self.setProperties(FontBold=True, ForeColor="Red")
       self.setProperties({"FontBold": True, "ForeColor": "Red"})
       self.setProperties({"FontBold": True}, ForeColor="Red")
   
   


Inherited from: :ref:`dabo.lib.propertyHelperMixin.PropertyHelperMixin`

-------

.. _no-79:

.. function:: dabo.dReportWriter.dReportWriter.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
   :noindex:


   
   Sets a group of properties on the object all at once. This
   is different from the regular setProperties() method because
   it only accepts a dict containing prop:value pairs, and it
   assumes that the value is always a string. It will convert
   the value to the correct type for the property, and then set
   the property to that converted value. If the value needs to be evaluated
   in a specific namespace, pass that as the 'context' parameter.
   


Inherited from: :ref:`dabo.lib.propertyHelperMixin.PropertyHelperMixin`

-------

.. _no-80:

.. function:: dabo.dReportWriter.dReportWriter.storeSpanningObject(self, obj, origin=(0, 0), group=None)
   :noindex:


   Store the passed spanning object for printing when the group or
   page ends. Pass the group expr to identify group headers, or None to refer
   to the pageHeader.
   


Inherited from: :ref:`dabo.lib.reportWriter.ReportWriter`

-------

.. _no-81:

.. function:: dabo.dReportWriter.dReportWriter.storeUndo(self, \*args)
   :noindex:



Inherited from: :ref:`dabo.lib.reportWriter.ReportWriter`

-------

.. _no-82:

.. function:: dabo.dReportWriter.dReportWriter.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-83:

.. function:: dabo.dReportWriter.dReportWriter.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-84:

.. function:: dabo.dReportWriter.dReportWriter.undo(self)
   :noindex:



Inherited from: :ref:`dabo.lib.reportWriter.ReportWriter`

-------

.. _no-85:

.. function:: dabo.dReportWriter.dReportWriter.write(self, save=True)
   :noindex:


   Write the PDF file based on the ReportForm spec.
   
   If the save argument is True (the default), the PDF file will be
   saved and closed after the report form has been written. If False,
   the PDF file will be left open so that additional pages can be added
   with another call, perhaps after creating a different report form.
   


Inherited from: :ref:`dabo.lib.reportWriter.ReportWriter`

-------


|
