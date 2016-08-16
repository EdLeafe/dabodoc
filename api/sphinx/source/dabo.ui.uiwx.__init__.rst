
.. include:: _static/headings.txt

.. module:: dabo.ui.uiwx.__init__

.. _dabo.ui.uiwx.__init__._Functions:

===================================
**__init__** functions
===================================

This is the description of standalone Python functions in the **dabo.ui.uiwx.__init__** module.

|method_summary| Functions Summary
==================================


.. autosummary::
   :nosignatures:

   beep
   bitmapFromData
   browse
   busyInfo
   callAfter
   callAfterInterval
   callEvery
   continueEvent
   copyToClipboard
   createClass
   createForm
   createMenuBar
   discontinueEvent
   fontMetric
   fontMetricFromDC
   fontMetricFromDrawObject
   fontMetricFromFont
   getAvailableFonts
   getChoice
   getChoices
   getColor
   getCommonBitmap
   getDate
   getDirectory
   getDisplaySize
   getEventData
   getFile
   getFileAndType
   getFolder
   getFont
   getFormMousePosition
   getFromClipboard
   getImagePath
   getInt
   getMouseObject
   getMousePosition
   getObjectAtPosition
   getPositionInSizer
   getSaveAs
   getSaveAsAndType
   getScrollWinEventClass
   getString
   getSystemInfo
   getUiApp
   imageFromData
   isAltDown
   isCommandDown
   isControlDown
   isMouseAux1Down
   isMouseAux2Down
   isMouseLeftDown
   isMouseMiddleDown
   isMouseRightDown
   isShiftDown
   makeGridEditor
   pathToBmp
   resizeBmp
   saveScreenShot
   sendIdle
   setAfter
   setAfterInterval
   setPositionInSizer
   setdFormClass
   sortList
   spawnProcess
   strToBmp
   yieldUI



|API| Functions API
===================


   .. autofunction:: dabo.ui.uiwx.__init__.beep()
   .. autofunction:: dabo.ui.uiwx.__init__.bitmapFromData(data)
   .. autofunction:: dabo.ui.uiwx.__init__.browse(dataSource, parent=None, keyCaption=None, includeFields=None, colOrder=None, colWidths=None, colTypes=None, autoSizeCols=True)
   .. autofunction:: dabo.ui.uiwx.__init__.busyInfo(msg='Please wait...')
   .. autofunction:: dabo.ui.uiwx.__init__.callAfter(fnc)
   .. autofunction:: dabo.ui.uiwx.__init__.callAfterInterval(interval, func)
   .. autofunction:: dabo.ui.uiwx.__init__.callEvery(interval, func)
   .. autofunction:: dabo.ui.uiwx.__init__.continueEvent(evt)
   .. autofunction:: dabo.ui.uiwx.__init__.copyToClipboard(val)
   .. autofunction:: dabo.ui.uiwx.__init__.createClass(srcFile)
   .. autofunction:: dabo.ui.uiwx.__init__.createForm(srcFile, show=False)
   .. autofunction:: dabo.ui.uiwx.__init__.createMenuBar(src, form=None, previewFunc=None)
   .. autofunction:: dabo.ui.uiwx.__init__.discontinueEvent(evt)
   .. autofunction:: dabo.ui.uiwx.__init__.fontMetric(txt=None, wind=None, face=None, size=None, bold=None, italic=None)
   .. autofunction:: dabo.ui.uiwx.__init__.fontMetricFromDC(dc, text)
   .. autofunction:: dabo.ui.uiwx.__init__.fontMetricFromDrawObject(obj)
   .. autofunction:: dabo.ui.uiwx.__init__.fontMetricFromFont(txt, font)
   .. autofunction:: dabo.ui.uiwx.__init__.getAvailableFonts()
   .. autofunction:: dabo.ui.uiwx.__init__.getChoice(choices, message=None, caption=None, defaultPos=None)
   .. autofunction:: dabo.ui.uiwx.__init__.getChoices(choices, message=None, caption=None, defaultPos=None)
   .. autofunction:: dabo.ui.uiwx.__init__.getColor(color=None)
   .. autofunction:: dabo.ui.uiwx.__init__.getCommonBitmap(name)
   .. autofunction:: dabo.ui.uiwx.__init__.getDate(dt=None)
   .. autofunction:: dabo.ui.uiwx.__init__.getFolder(message=u'Choose a folder', defaultPath='', wildcard='*')
   .. autofunction:: dabo.ui.uiwx.__init__.getDisplaySize()
   .. autofunction:: dabo.ui.uiwx.__init__.getEventData(wxEvt)
   .. autofunction:: dabo.ui.uiwx.__init__.getFile()
   .. autofunction:: dabo.ui.uiwx.__init__.getFileAndType()
   .. autofunction:: dabo.ui.uiwx.__init__.getFolder(message=u'Choose a folder', defaultPath='', wildcard='*')
   .. autofunction:: dabo.ui.uiwx.__init__.getFont(font=None)
   .. autofunction:: dabo.ui.uiwx.__init__.getFormMousePosition()
   .. autofunction:: dabo.ui.uiwx.__init__.getFromClipboard()
   .. autofunction:: dabo.ui.uiwx.__init__.getImagePath(nm, url=False)
   .. autofunction:: dabo.ui.uiwx.__init__.getInt(message=u'Enter an integer value:', caption='Dabo', defaultValue=0)
   .. autofunction:: dabo.ui.uiwx.__init__.getMouseObject()
   .. autofunction:: dabo.ui.uiwx.__init__.getMousePosition()
   .. autofunction:: dabo.ui.uiwx.__init__.getObjectAtPosition(x, y=None)
   .. autofunction:: dabo.ui.uiwx.__init__.getPositionInSizer(obj)
   .. autofunction:: dabo.ui.uiwx.__init__.getSaveAs()
   .. autofunction:: dabo.ui.uiwx.__init__.getSaveAsAndType()
   .. autofunction:: dabo.ui.uiwx.__init__.getScrollWinEventClass(evt)
   .. autofunction:: dabo.ui.uiwx.__init__.getString(message=u'Please enter a string:', caption='Dabo', defaultValue='')
   .. autofunction:: dabo.ui.uiwx.__init__.getSystemInfo(returnType=None)
   .. autofunction:: dabo.ui.uiwx.__init__.getUiApp(app, uiAppClass=None, callback=None, forceNew=False)
   .. autofunction:: dabo.ui.uiwx.__init__.imageFromData(data)
   .. autofunction:: dabo.ui.uiwx.__init__.isAltDown()
   .. autofunction:: dabo.ui.uiwx.__init__.isCommandDown()
   .. autofunction:: dabo.ui.uiwx.__init__.isControlDown()
   .. autofunction:: dabo.ui.uiwx.__init__.isMouseAux1Down()
   .. autofunction:: dabo.ui.uiwx.__init__.isMouseAux2Down()
   .. autofunction:: dabo.ui.uiwx.__init__.isMouseLeftDown()
   .. autofunction:: dabo.ui.uiwx.__init__.isMouseMiddleDown()
   .. autofunction:: dabo.ui.uiwx.__init__.isMouseRightDown()
   .. autofunction:: dabo.ui.uiwx.__init__.isShiftDown()
   .. autofunction:: dabo.ui.uiwx.__init__.makeGridEditor(controlClass, minWidth=None, minHeight=None)
   .. autofunction:: dabo.ui.uiwx.__init__.pathToBmp(pth)
   .. autofunction:: dabo.ui.uiwx.__init__.resizeBmp(bmp, wd, ht)
   .. autofunction:: dabo.ui.uiwx.__init__.saveScreenShot(obj=None, imgType=None, pth=None, delaySeconds=None)
   .. autofunction:: dabo.ui.uiwx.__init__.sendIdle()
   .. autofunction:: dabo.ui.uiwx.__init__.setAfter(obj, prop, val)
   .. autofunction:: dabo.ui.uiwx.__init__.setAfterInterval(interval, obj, prop, val)
   .. autofunction:: dabo.ui.uiwx.__init__.setPositionInSizer(obj, pos)
   .. autofunction:: dabo.ui.uiwx.__init__.setdFormClass(typ)
   .. autofunction:: dabo.ui.uiwx.__init__.sortList(chc, Caption='', ListCaption='')
   .. autofunction:: dabo.ui.uiwx.__init__.spawnProcess(cmd, wait=False, handler=None)
   .. autofunction:: dabo.ui.uiwx.__init__.strToBmp(val, scale=None, width=None, height=None)
   .. autofunction:: dabo.ui.uiwx.__init__.yieldUI(_safe=False)

|
