
.. include:: _static/headings.txt

.. module:: dabo.dApp

.. _dabo.dApp.dApp:

==================================
|doc_title|  **dApp.dApp** - class
==================================


The containing object for the entire application.

All Dabo objects have an Application property which refers to the dApp
instance. Instantiate your dApp object from your main script, like so::

    >>> from dabo.dApp import dApp
    >>> app = dApp()
    >>> app.start()

    Normally, dApp gets instantiated from the client app's main Python script,
    and lives through the life of the application.

        -- Set up an empty data connections dict that contains connection objects
        -- that use descriptive names as their keys. Obviously this requires that
        -- each connection has a unique name; if you create connections with
        -- identical names, the second one read in will overwrite the first, and
        -- the results are not guaranteed. Once read in, the only identifier for a
        -- connection is its name; the file from which it was read in, if any, is
        -- irrelevant. Any .cnxml files found in the app home directory, the
        -- current directory (if different) or any subdirectory named 'db' or
        -- 'data' of the home/current directory will be automatically read into the
        -- connections dict, but the connections aren't made until requested by the
        -- app. Additionally, connections defined in Python code in a file named
        -- 'dbConnectionDefs.py' will be imported. This is an old behavior that
        -- should no longer be used.

        -- Set up a DB Connection manager, that is basically a dictionary
        -- of dConnection objects. This allows connections to be shared
        -- application-wide.

        -- decide which ui to use (wx) and gets that ball rolling

        -- look for a MainForm in an expected place, otherwise use default dabo
        -- dFormMain, and instantiate that.

        -- maintain a forms collection and provide interfaces for
        -- opening dForms, closing them, and iterating through them.

        -- start the main app event loop.

        -- clean up and exit gracefully





|hierarchy| Inheritance Diagram
===============================

Inheritance diagram for: **dApp**

.. inheritance-diagram:: dApp


|supclasses| Known Superclasses
===============================

* :ref:`dabo.dObject.dObject`



|API| Class API
===============


.. autoclass:: dabo.dApp.dApp

   .. automethod:: dabo.dApp.dApp.__init__

|method_summary| Properties Summary
===================================


======================================== ========================
:ref:`HomeDirectory <no-100>`            Specifies the application's home directory. (string)
:ref:`Icon <no-101>`                     Specifies the icon to use on all forms and dialogs by default.
:ref:`LogEvents <no-102>`                Specifies which events to log.  (list of strings)
:ref:`LoginDialogClass <no-103>`         The class to use for logging in.
:ref:`MainForm <no-104>`                 The object reference to the main form of the application, or None.
:ref:`MainFormClass <no-105>`            Specifies the class to instantiate for the main form. Can be a
:ref:`Name <no-106>`                     The name of the object.  (str)
:ref:`NoneDisplay <no-107>`              Text to display for null (None) values.  (str)
:ref:`Parent <no-108>`                   The containing object.  (obj)
:ref:`Platform <no-109>`                 Returns the platform we are running on. This will be
:ref:`PreferenceDialogClass <no-110>`    Specifies the dialog to use for the application's user preferences.
:ref:`PreferenceManager <no-111>`        Reference to the Preference Management object  (dPref)
:ref:`ReleasePreferenceDialog <no-112>`  If False, the preference dialog will remain hidden in memory after closed,
:ref:`SearchDelay <no-113>`              Specifies the delay before incrementeal searching begins.  (int)
:ref:`SecurityManager <no-114>`          Specifies the Security Manager, if any.
:ref:`ShowCommandWindowMenu <no-115>`    Specifies whether the command window option is shown in the menu.
:ref:`ShowSizerLinesMenu <no-116>`       Specifies whether the "Show Sizer Lines" option is shown in the menu.
:ref:`SourceURL <no-117>`                If this app's source files are updated dynamically via the web,
:ref:`UI <no-118>`                       Specifies the user interface to load, or None. (str)
:ref:`UIAppClass <no-119>`               The name of the ui-specific app subclass to instantiate.
:ref:`UserSettingProvider <no-120>`      Specifies the reference to the object providing user preference persistence.
:ref:`UserSettingProviderClass <no-121>` Specifies the class to use for user preference persistence.
:ref:`AboutFormClass <no-86>`            Specifies the form class to use for the application's About screen.
:ref:`ActiveForm <no-87>`                Returns the form that currently has focus, or None.  (dForm)
:ref:`Application <no-88>`               Read-only object reference to the Dabo Application object.  (dApp).
:ref:`AutoImportConnections <no-89>`     Specifies whether .cnxml connection files are automatically imported. (Default True)
:ref:`BaseClass <no-90>`                 The base Dabo class of the object. Read-only.  (class)
:ref:`BasePrefKey <no-91>`               Base key used when saving/restoring preferences. This differs
:ref:`Class <no-92>`                     The class the object is based on. Read-only.  (class)
:ref:`Crypto <no-93>`                    Reference to the object that provides cryptographic services.  (varies)
:ref:`CryptoKey <no-94>`                 When set, creates a DES crypto object if PyCrypto is installed. Note that
:ref:`DefaultForm <no-95>`               The form class to open by default, automatically, after app instantiation.  (form class reference)
:ref:`DefaultMenuBarClass <no-96>`       The class used by all forms in the application when no specific MenuBarClass
:ref:`DrawSizerOutlines <no-97>`         Determines if sizer outlines are drawn on the ActiveForm.  (bool)
:ref:`Encoding <no-98>`                  Name of encoding to use for unicode  (str)
:ref:`FormsToOpen <no-99>`               List of forms to open after App instantiation.  (list of form class references)

======================================== ========================


Properties
==========

.. _no-86:

**AboutFormClass** 

Specifies the form class to use for the application's About screen.



-------

.. _no-87:

**ActiveForm** 

Returns the form that currently has focus, or None.  (dForm)



-------

.. _no-89:

**AutoImportConnections** 

Specifies whether .cnxml connection files are automatically imported. (Default True)



-------

.. _no-93:

**Crypto** 

Reference to the object that provides cryptographic services.  (varies)



-------

.. _no-94:

**CryptoKey** 

When set, creates a DES crypto object if PyCrypto is installed. Note that
    each time this property is set, a new PyCrypto instance is created, and
    any previous crypto objects are released. Write-only.  (varies)



-------

.. _no-95:

**DefaultForm** 

The form class to open by default, automatically, after app instantiation.  (form class reference)



-------

.. _no-96:

**DefaultMenuBarClass** 

The class used by all forms in the application when no specific MenuBarClass
    is specified  (dabo.ui.dMenuBar)



-------

.. _no-97:

**DrawSizerOutlines** 

Determines if sizer outlines are drawn on the ActiveForm.  (bool)



-------

.. _no-98:

**Encoding** 

Name of encoding to use for unicode  (str)



-------

.. _no-99:

**FormsToOpen** 

List of forms to open after App instantiation.  (list of form class references)



-------

.. _no-100:

**HomeDirectory** 

Specifies the application's home directory. (string)

    The HomeDirectory is the top-level directory for your application files,
    the directory where your main script lives. You never know what the
    current directory will be on a given system, but HomeDirectory will always
    get you to your files.



-------

.. _no-101:

**Icon** 

Specifies the icon to use on all forms and dialogs by default.

    The value passed can be a binary icon bitmap, a filename, or a
    sequence of filenames. Providing a sequence of filenames pointing to
    icons at expected dimensions like 16, 22, and 32 px means that the
    system will not have to scale the icon, resulting in a much better
    appearance.



-------

.. _no-103:

**LoginDialogClass** 

The class to use for logging in.



-------

.. _no-104:

**MainForm** 

The object reference to the main form of the application, or None.

    The MainForm gets instantiated automatically during application setup,
    based on the value of MainFormClass. If you want to swap in your own
    MainForm instance, do it after setup() but before start(), as in::

    >>> from dabo.dApp import dApp
    >>> app = dApp()
    >>> app.setup()
    >>> app.MainForm = myMainFormInstance
    >>> app.start()

    



-------

.. _no-105:

**MainFormClass** 

Specifies the class to instantiate for the main form. Can be a
    class reference, or the path to a .cdxml file.

    Defaults to the dFormMain base class. Set to None if you don't want a
    main form, or set to your own main form class. Do this before calling
    dApp.start(), as in::

    >>> from dabo.dApp import dApp
    >>> app = dApp()
    >>> app.MainFormClass = MyMainFormClass
    >>> app.start()

    



-------

.. _no-107:

**NoneDisplay** 

Text to display for null (None) values.  (str)



-------

.. _no-109:

**Platform** 

Returns the platform we are running on. This will be
    one of 'Mac', 'Win' or 'GTK'.  (str)



-------

.. _no-110:

**PreferenceDialogClass** 

Specifies the dialog to use for the application's user preferences.

    If None, the application will try to run the active form's onEditPreferences()
    method, if any. Otherwise, the preference dialog will be instantiated and
    shown when the user chooses to see the preferences.



-------

.. _no-112:

**ReleasePreferenceDialog** 

If False, the preference dialog will remain hidden in memory after closed,
    resulting in better performance when bringing up the dialog more than once.

    Note that you'll still have to handle intercepting your dialog's Close event and
    hiding it instead of releasing, or you'll be battling dead object errors.



-------

.. _no-113:

**SearchDelay** 

Specifies the delay before incrementeal searching begins.  (int)

    As the user types, the search string is modified. If the time between
    keystrokes exceeds SearchDelay (milliseconds), the search will run and
    the search string    will be cleared.

    The value set here in the Application object will become the default for
    all objects that provide incremental searching application-wide.



-------

.. _no-114:

**SecurityManager** 

Specifies the Security Manager, if any.

    You must subclass dSecurityManager, overriding the appropriate hooks
    and properties, and then set dApp.SecurityManager to an instance of your
    subclass. There is no security manager by default - you explicitly set
    this to use Dabo security.



-------

.. _no-115:

**ShowCommandWindowMenu** 

Specifies whether the command window option is shown in the menu.

    If True (the default), there will be a File|Command Window option
    available in the base menu. If False, your code can still start the
    command window by calling app.showCommandWindow() directly.



-------

.. _no-116:

**ShowSizerLinesMenu** 

Specifies whether the "Show Sizer Lines" option is shown in the menu.

    If True (the default), there will be a View|Show Sizer Lines option
    available in the base menu.



-------

.. _no-117:

**SourceURL** 

If this app's source files are updated dynamically via the web,
    this is the base URL to which the source file's name will be appended.
    Default="" (i.e., no source on the internet).  (str)



-------

.. _no-118:

**UI** 

Specifies the user interface to load, or None. (str)

    This is the user interface library, such as 'wx' or 'tk'. Note that
    'wx' is the only supported user interface library at this point.



-------

.. _no-119:

**UIAppClass** 

The name of the ui-specific app subclass to instantiate.

    This will allow ui toolkit-specific behaviors to be added to a Dabo
    application. It MUST be either defined in the application subclass, or
    passed in the call to create the app object, since the UI App cannot
    be changed once the app is running. Defaults to dabo.ui.uiApp
    if not specified.  (dabo.ui.uiApp)



-------

.. _no-120:

**UserSettingProvider** 

Specifies the reference to the object providing user preference persistence.

    The default UserSettingProvider will save user preferences inside the .dabo
    directory inside the user's home directory.



-------

.. _no-121:

**UserSettingProviderClass** 

Specifies the class to use for user preference persistence.

    The default UserSettingProviderClass will save user preferences inside the .dabo
    directory inside the user's home directory, and will be instantiated by Dabo
    automatically.



-------


Properties - inherited
========================

.. _no-88:

**Application** 

Read-only object reference to the Dabo Application object.  (dApp).


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-90:

**BaseClass** 

The base Dabo class of the object. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-91:

**BasePrefKey** 

Base key used when saving/restoring preferences. This differs
    from the default definition of this property in that if it is empty, it
    will return the ActiveForm's BasePrefKey or the MainForm's BasePrefKey
    in that order. (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-92:

**Class** 

The class the object is based on. Read-only.  (class)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-102:

**LogEvents** 


    Specifies which events to log.  (list of strings)

    If the first element is 'All', all events except the following listed events
    will be logged.
    Event logging is resource-intensive, so in addition to setting this LogEvents
    property, you also need to make the following call:

        >>> dabo.eventLogging = True

    


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-106:

**Name** 

The name of the object.  (str)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-108:

**Parent** 

The containing object.  (obj)


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-111:

**PreferenceManager** 

Reference to the Preference Management object  (dPref)


Inherited from: :ref:`dabo.dObject.dObject`

-------


|method_summary| Events Summary
===============================


========================== ========================
:ref:`Activate <no-122>`   Occurs when the form or application becomes active.
:ref:`Deactivate <no-123>` Occurs when another form becomes active.
:ref:`KeyChar <no-124>`    Occurs when a key is depressed and released on the
:ref:`KeyDown <no-125>`    Occurs when any key is depressed on the focused control or form.
:ref:`KeyEvent <no-126>`   
:ref:`KeyUp <no-127>`      Occurs when any key is released on the focused control or form.

========================== ========================


Events
=======

.. _no-122:

**Activate** 

Occurs when the form or application becomes active.



-------

.. _no-123:

**Deactivate** 

Occurs when another form becomes active.



-------

.. _no-124:

**KeyChar** 

Occurs when a key is depressed and released on the
focused control or form.




-------

.. _no-125:

**KeyDown** 

Occurs when any key is depressed on the focused control or form.



-------

.. _no-126:

**KeyEvent** 



-------

.. _no-127:

**KeyUp** 

Occurs when any key is released on the focused control or form.



-------


|method_summary| Methods Summary
================================


======================================= ========================
:ref:`addConnectFile <no-128>`          Accepts a cnxml file path, and reads in the connections
:ref:`addConnectInfo <no-129>`          
:ref:`addToAbout <no-130>`              Adds additional app-specific information to the About form.
:ref:`addToMRU <no-131>`                
:ref:`afterEditPreferences <no-132>`    
:ref:`afterFinish <no-133>`             Stub method. When this is called, the app has already terminated, and you have
:ref:`afterInit <no-134>`               Subclass hook. Called after the object's __init__ has run fully.
:ref:`afterSetup <no-135>`              Hook method that is called after the app's setup code has run, and the
:ref:`autoBindEvents <no-136>`          Automatically bind any on*() methods to the associated event.
:ref:`beforeEditPreferences <no-137>`   
:ref:`beforeInit <no-138>`              Subclass hook. Called before the object is fully instantiated.
:ref:`bindEvent <no-139>`               Bind a dEvent to a callback function.
:ref:`bindEvents <no-140>`              Bind a sequence of [dEvent, callback] lists.
:ref:`checkForUpdates <no-141>`         Public interface to the web updates mechanism. Returns a boolean
:ref:`clearActiveForm <no-142>`         Called by the form when it is deactivated.
:ref:`closeConnections <no-143>`        Cleanup as the app is exiting.
:ref:`copyToClipboard <no-144>`         Place the passed text onto the clipboard.
:ref:`decrypt <no-145>`                 Return decrypted string value. The request is passed to
:ref:`deleteAllUserSettings <no-146>`   Deletes all settings that begin with the supplied spec.
:ref:`deleteUserSetting <no-147>`       Removes the given item from the user settings file.
:ref:`displayInfoMessage <no-148>`      Displays a messagebox dialog along with a checkbox for the user
:ref:`encrypt <no-149>`                 Return the encrypted string value. The request is passed
:ref:`finish <no-150>`                  Called when the application event loop has ended. You may also
:ref:`fontZoomIn <no-151>`              Increase the font size on the active form.
:ref:`fontZoomNormal <no-152>`          Reset the font size to normal on the active form.
:ref:`fontZoomOut <no-153>`             Decrease the font size on the active form.
:ref:`getAbsoluteName <no-154>`         Return the fully qualified name of the object.
:ref:`getAppInfo <no-155>`              Look up the item, and return the value.
:ref:`getCharset <no-156>`              Returns one of 'unicode' or 'ascii'.
:ref:`getConnectionByName <no-157>`     Given the name of a connection, returns the actual
:ref:`getConnectionNames <no-158>`      Returns a list of all defined connection names
:ref:`getConnectionsFromFile <no-159>`  Given an absolute path to a .cnxml file, return the connection defs.
:ref:`getLoginInfo <no-160>`            Return a tuple of (user, password) to dSecurityManager.login(). The default
:ref:`getProperties <no-161>`           Returns a dictionary of property name/value pairs.
:ref:`getStandardAppDirectory <no-162>` Return the path to one of the standard Dabo application directories.
:ref:`getStandardDirectories <no-163>`  Return a tuple of the fullpath to each standard directory
:ref:`getTransactionToken <no-164>`     Only one bizobj at a time can begin and end transactions per connection.
:ref:`getUserCaption <no-165>`          Return the full name of the currently logged-on user.
:ref:`getUserSetting <no-166>`          Return the value of the item in the user settings table.
:ref:`getUserSettingKeys <no-167>`      Return a list of all keys underneath <spec> in the user settings table.
:ref:`getWebUpdateInfo <no-168>`        Returns a 2-tuple that reflects the current settings for web updates.
:ref:`hasTransactionToken <no-169>`     Returns True/False, depending on whether the specified
:ref:`initEvents <no-170>`              Hook for subclasses. User code should do custom event binding
:ref:`initProperties <no-171>`          Hook for subclasses. User subclasses should set properties
:ref:`initUIApp <no-172>`               Callback from the initial app setup. Used to allow the
:ref:`loginDialogHook <no-173>`         Hook method; modify the dialog as needed.
:ref:`onCmdWin <no-174>`                
:ref:`onDebugWin <no-175>`              
:ref:`onEditCopy <no-176>`              
:ref:`onEditCut <no-177>`               
:ref:`onEditFind <no-178>`              
:ref:`onEditFindAgain <no-179>`         
:ref:`onEditFindAlone <no-180>`         
:ref:`onEditPaste <no-181>`             
:ref:`onEditPreferences <no-182>`       
:ref:`onEditRedo <no-183>`              
:ref:`onEditSelectAll <no-184>`         
:ref:`onEditUndo <no-185>`              
:ref:`onFileExit <no-186>`              
:ref:`onHelpAbout <no-187>`             
:ref:`onMenuOpenMRU <no-188>`           
:ref:`onObjectInspectorWin <no-189>`    
:ref:`onReloadForm <no-190>`            
:ref:`onShowSizerLines <no-191>`        
:ref:`onUiNewFile <no-192>`             
:ref:`onUiOpenFile <no-193>`            
:ref:`onUiPrintFile <no-194>`           
:ref:`onUiReopenApp <no-195>`           
:ref:`onWinClose <no-196>`              
:ref:`raiseEvent <no-197>`              Send the event to all registered listeners.
:ref:`releaseTransactionToken <no-198>` When a process that would normally close a transaction happens, the
:ref:`resyncFiles <no-199>`             In the middle of an app's lifetime, files on the remote server may
:ref:`setAppInfo <no-200>`              Set item to value in the appinfo table.
:ref:`setLanguage <no-201>`             Allows you to change the language used for localization. If the language
:ref:`setProperties <no-202>`           Sets a group of properties on the object all at once.
:ref:`setPropertiesFromAtts <no-203>`   Sets a group of properties on the object all at once. This
:ref:`setUserSetting <no-204>`          Persist a value to the user settings file.
:ref:`setUserSettings <no-205>`         Convenience method for setting several settings with one
:ref:`setup <no-206>`                   Set up the application object.
:ref:`showCommandWindow <no-207>`       Shows a command window with a full Python interpreter.
:ref:`start <no-208>`                   Start the application event loop.
:ref:`startupForms <no-209>`            Open one or more of the defined forms. The default one is specified
:ref:`super <no-210>`                   This method used to call superclass code, but it's been removed.
:ref:`toggleDebugWindow <no-211>`       Shows/hodes a debug output window. It will
:ref:`unbindEvent <no-212>`             Remove a previously registered event binding.
:ref:`updateFromSource <no-213>`        This method takes either a single file path or a list of paths, and if there
:ref:`urlFetch <no-214>`                Fetches the specified resource from the internet using the SourceURL value

======================================= ========================


Methods
=======

.. _no-128:

.. function:: dabo.dApp.dApp.addConnectFile(self, connFile)

   
   Accepts a cnxml file path, and reads in the connections
   defined in it, adding them to self.dbConnectionDefs. If the
   file cannot be found, an exception is raised.
   



-------

.. _no-129:

.. function:: dabo.dApp.dApp.addConnectInfo(self, ci, name=None)



-------

.. _no-130:

.. function:: dabo.dApp.dApp.addToAbout(self)

   
   Adds additional app-specific information to the About form.
   By default, add the contents of the app's docstring.
   



-------

.. _no-131:

.. function:: dabo.dApp.dApp.addToMRU(self, menu, prmpt, bindfunc=None, \*args, \**kwargs)



-------

.. _no-132:

.. function:: dabo.dApp.dApp.afterEditPreferences(self)



-------

.. _no-133:

.. function:: dabo.dApp.dApp.afterFinish(self)

   
   Stub method. When this is called, the app has already terminated, and you have
   one last chance to execute code by overriding this method.
   



-------

.. _no-135:

.. function:: dabo.dApp.dApp.afterSetup(self)

   
   Hook method that is called after the app's setup code has run, and the
   database, UI and module references have all been established.
   



-------

.. _no-137:

.. function:: dabo.dApp.dApp.beforeEditPreferences(self)



-------

.. _no-141:

.. function:: dabo.dApp.dApp.checkForUpdates(self, evt=None)

   
   Public interface to the web updates mechanism. Returns a boolean
   indicating whether the update was successful.
   



-------

.. _no-142:

.. function:: dabo.dApp.dApp.clearActiveForm(self, frm)

   Called by the form when it is deactivated.



-------

.. _no-143:

.. function:: dabo.dApp.dApp.closeConnections(self)

   Cleanup as the app is exiting.



-------

.. _no-144:

.. function:: dabo.dApp.dApp.copyToClipboard(self, txt)

   Place the passed text onto the clipboard.



-------

.. _no-145:

.. function:: dabo.dApp.dApp.decrypt(self, val)

   
   Return decrypted string value. The request is passed to
   the Crypto object for processing.
   



-------

.. _no-146:

.. function:: dabo.dApp.dApp.deleteAllUserSettings(self, spec)

   Deletes all settings that begin with the supplied spec.



-------

.. _no-147:

.. function:: dabo.dApp.dApp.deleteUserSetting(self, item)

   Removes the given item from the user settings file.



-------

.. _no-148:

.. function:: dabo.dApp.dApp.displayInfoMessage(self, msgId, msg, defaultShowInFuture=True)

   
   Displays a messagebox dialog along with a checkbox for the user
   to specify whether or not to show this particular message again
   in the future.
   
   If user unchecks "show in future", saves that to the user's
   preference file and future calls to this function with that
   msgId will result in no message being shown.
   



-------

.. _no-149:

.. function:: dabo.dApp.dApp.encrypt(self, val)

   
   Return the encrypted string value. The request is passed
   to the Crypto object for processing.
   



-------

.. _no-150:

.. function:: dabo.dApp.dApp.finish(self)

   
   Called when the application event loop has ended. You may also
   call this explicitly to exit the application event loop.
   



-------

.. _no-151:

.. function:: dabo.dApp.dApp.fontZoomIn(self, evt=None)

   Increase the font size on the active form.



-------

.. _no-152:

.. function:: dabo.dApp.dApp.fontZoomNormal(self, evt=None)

   Reset the font size to normal on the active form.



-------

.. _no-153:

.. function:: dabo.dApp.dApp.fontZoomOut(self, evt=None)

   Decrease the font size on the active form.



-------

.. _no-155:

.. function:: dabo.dApp.dApp.getAppInfo(self, item, default=None)

   Look up the item, and return the value.



-------

.. _no-156:

.. function:: dabo.dApp.dApp.getCharset(self)

   Returns one of 'unicode' or 'ascii'.



-------

.. _no-157:

.. function:: dabo.dApp.dApp.getConnectionByName(self, connName)

   
   Given the name of a connection, returns the actual
   connection. Stores the connection so that multiple requests
   for the same named connection will not open multiple
   connections. If the name doesn't exist in self.dbConnectionDefs,
   then an exception is raised.
   



-------

.. _no-158:

.. function:: dabo.dApp.dApp.getConnectionNames(self)

   Returns a list of all defined connection names



-------

.. _no-159:

.. function:: dabo.dApp.dApp.getConnectionsFromFile(self, filePath)

   Given an absolute path to a .cnxml file, return the connection defs.



-------

.. _no-160:

.. function:: dabo.dApp.dApp.getLoginInfo(self, message=None)

   
   Return a tuple of (user, password) to dSecurityManager.login(). The default
   is to display the standard login dialog, and return the user/password as
   entered by the user, but subclasses can override to get the information from
   where ever is appropriate. You can customize the default dialog by adding
   your own code to the loginDialogHook() method, which will receive a
   reference to the login dialog.
   
   Return a tuple of (user, pass).
   



-------

.. _no-162:

.. function:: dabo.dApp.dApp.getStandardAppDirectory(self, dirname, start=None)

   
   Return the path to one of the standard Dabo application directories.
   If a starting file path is provided, use that first. If not, use the
   HomeDirectory as the starting point.
   



-------

.. _no-163:

.. function:: dabo.dApp.dApp.getStandardDirectories(self)

   Return a tuple of the fullpath to each standard directory



-------

.. _no-164:

.. function:: dabo.dApp.dApp.getTransactionToken(self, biz)

   
   Only one bizobj at a time can begin and end transactions per connection.
   This allows the bizobj to query the app for the 'token', which is simply an
   acknowledgement that there is no other transaction pending for that connection.
   If the bizobj gets the token, further requests for the token from bizobjs using the
   same transaction will receive a reply of False, meaning that they should not be
   handling the transaction.
   



-------

.. _no-165:

.. function:: dabo.dApp.dApp.getUserCaption(self)

   Return the full name of the currently logged-on user.



-------

.. _no-166:

.. function:: dabo.dApp.dApp.getUserSetting(self, item, default=None)

   Return the value of the item in the user settings table.



-------

.. _no-167:

.. function:: dabo.dApp.dApp.getUserSettingKeys(self, spec)

   
   Return a list of all keys underneath <spec> in the user settings table.
   
   For example, if spec is "appWizard.dbDefaults", and there are
   userSettings entries for:
   
       appWizard.dbDefaults.pkm.Host
       appWizard.dbDefaults.pkm.User
       appWizard.dbDefaults.egl.Host
   
   The return value would be ["pkm", "egl"]
   



-------

.. _no-168:

.. function:: dabo.dApp.dApp.getWebUpdateInfo(self)

   
   Returns a 2-tuple that reflects the current settings for web updates.
   The first position is a boolean that reflects whether auto-checking is turned
   on; the second is the update frequency in minutes.
   



-------

.. _no-169:

.. function:: dabo.dApp.dApp.hasTransactionToken(self, biz)

   
   Returns True/False, depending on whether the specified
   bizobj currently "holds" the transaction token.
   



-------

.. _no-172:

.. function:: dabo.dApp.dApp.initUIApp(self)

   
   Callback from the initial app setup. Used to allow the
   splash screen, if any, to be shown quickly.
   



-------

.. _no-173:

.. function:: dabo.dApp.dApp.loginDialogHook(self, dlg)

   Hook method; modify the dialog as needed.



-------

.. _no-174:

.. function:: dabo.dApp.dApp.onCmdWin(self, evt)



-------

.. _no-175:

.. function:: dabo.dApp.dApp.onDebugWin(self, evt)



-------

.. _no-176:

.. function:: dabo.dApp.dApp.onEditCopy(self, evt)



-------

.. _no-177:

.. function:: dabo.dApp.dApp.onEditCut(self, evt)



-------

.. _no-178:

.. function:: dabo.dApp.dApp.onEditFind(self, evt)



-------

.. _no-179:

.. function:: dabo.dApp.dApp.onEditFindAgain(self, evt)



-------

.. _no-180:

.. function:: dabo.dApp.dApp.onEditFindAlone(self, evt)



-------

.. _no-181:

.. function:: dabo.dApp.dApp.onEditPaste(self, evt)



-------

.. _no-182:

.. function:: dabo.dApp.dApp.onEditPreferences(self, evt)



-------

.. _no-183:

.. function:: dabo.dApp.dApp.onEditRedo(self, evt)



-------

.. _no-184:

.. function:: dabo.dApp.dApp.onEditSelectAll(self, evt)



-------

.. _no-185:

.. function:: dabo.dApp.dApp.onEditUndo(self, evt)



-------

.. _no-186:

.. function:: dabo.dApp.dApp.onFileExit(self, evt)



-------

.. _no-187:

.. function:: dabo.dApp.dApp.onHelpAbout(self, evt)



-------

.. _no-188:

.. function:: dabo.dApp.dApp.onMenuOpenMRU(self, menu)



-------

.. _no-189:

.. function:: dabo.dApp.dApp.onObjectInspectorWin(self, evt)



-------

.. _no-190:

.. function:: dabo.dApp.dApp.onReloadForm(self, evt)



-------

.. _no-191:

.. function:: dabo.dApp.dApp.onShowSizerLines(self, evt)



-------

.. _no-192:

.. function:: dabo.dApp.dApp.onUiNewFile(self, filename, \*args, \**kwargs)



-------

.. _no-193:

.. function:: dabo.dApp.dApp.onUiOpenFile(self, filename, \*args, \**kwargs)



-------

.. _no-194:

.. function:: dabo.dApp.dApp.onUiPrintFile(self, filename, \*args, \**kwargs)



-------

.. _no-195:

.. function:: dabo.dApp.dApp.onUiReopenApp(self, filename, \*args, \**kwargs)



-------

.. _no-196:

.. function:: dabo.dApp.dApp.onWinClose(self, evt)



-------

.. _no-198:

.. function:: dabo.dApp.dApp.releaseTransactionToken(self, biz)

   
   When a process that would normally close a transaction happens, the
   bizobj that is holding the transaction token for its connection calls this
   method to return the token. A check is run to ensure that the releasing bizobj
   is the one currently holding the token for its connection; if it is, the item is
   removed from the _transactionTokens dict.
   



-------

.. _no-199:

.. function:: dabo.dApp.dApp.resyncFiles(self)

   
   In the middle of an app's lifetime, files on the remote server may
   have been updated. This will ensure that the local copy is in sync.
   



-------

.. _no-200:

.. function:: dabo.dApp.dApp.setAppInfo(self, item, value)

   Set item to value in the appinfo table.



-------

.. _no-201:

.. function:: dabo.dApp.dApp.setLanguage(self, lang, charset=None)

   
   Allows you to change the language used for localization. If the language
   passed is not one for which there is a translation file, an IOError exception
   will be raised. You may optionally pass a character set to use.
   



-------

.. _no-204:

.. function:: dabo.dApp.dApp.setUserSetting(self, item, value)

   Persist a value to the user settings file.



-------

.. _no-205:

.. function:: dabo.dApp.dApp.setUserSettings(self, setDict)

   
   Convenience method for setting several settings with one
   call. Pass a dict containing {settingName: settingValue} pairs.
   



-------

.. _no-206:

.. function:: dabo.dApp.dApp.setup(self, initUI=True)

   Set up the application object.



-------

.. _no-207:

.. function:: dabo.dApp.dApp.showCommandWindow(self, context=None)

   
   Shows a command window with a full Python interpreter.
   
   This is great for debugging during development, but you should turn off
   app.ShowCommandWindowMenu in production, perhaps leaving backdoor
   access to this function.
   
   The context argument tells dShellForm what object becomes 'self'. If not
   passed, context will be app.ActiveForm.
   



-------

.. _no-208:

.. function:: dabo.dApp.dApp.start(self)

   Start the application event loop.



-------

.. _no-209:

.. function:: dabo.dApp.dApp.startupForms(self)

   
   Open one or more of the defined forms. The default one is specified
   in self.DefaultForm. If form names were passed on the command line,
   they will be opened instead of the default one as long as they exist.
   



-------

.. _no-211:

.. function:: dabo.dApp.dApp.toggleDebugWindow(self, context=None)

   
   Shows/hodes a debug output window. It will
   display the output of the debugging commands
   from your program.
   



-------

.. _no-213:

.. function:: dabo.dApp.dApp.updateFromSource(self, fileOrFiles)

   
   This method takes either a single file path or a list of paths, and if there
   is a SourceURL set, checks the source to see if there are newer versions available,
   and if so, downloads them.
   



-------

.. _no-214:

.. function:: dabo.dApp.dApp.urlFetch(self, pth, errorOnNotFound=False)

   
   Fetches the specified resource from the internet using the SourceURL value
   as the base for the resource URL. If a newer version is found, the local copy
   is updated with the retrieved resource. If the resource isn't found, nothing
   happens by default. If you want the error to be raised, pass True for the
   parameter 'errorOnNotFound'.
   



-------


Methods - inherited
=====================

.. _no-134:

.. function:: dabo.dApp.dApp.afterInit(self)
   :noindex:


   
   Subclass hook. Called after the object's __init__ has run fully.
   Subclasses should place their __init__ code here in this hook, instead of
   overriding __init__ directly, to avoid conflicting with base Dabo behavior.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-136:

.. function:: dabo.dApp.dApp.autoBindEvents(self, force=True)
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

.. _no-138:

.. function:: dabo.dApp.dApp.beforeInit(self, \*args, \**kwargs)
   :noindex:


   
   Subclass hook. Called before the object is fully instantiated.
   Usually, user code should override afterInit() instead, but there may be
   cases where you need to set an attribute before the init stage is fully
   underway.
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-139:

.. function:: dabo.dApp.dApp.bindEvent(self, eventClass, function, _auto=False)
   :noindex:


   Bind a dEvent to a callback function.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-140:

.. function:: dabo.dApp.dApp.bindEvents(self, bindings)
   :noindex:


   Bind a sequence of [dEvent, callback] lists.


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------

.. _no-154:

.. function:: dabo.dApp.dApp.getAbsoluteName(self)
   :noindex:


   Return the fully qualified name of the object.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-161:

.. function:: dabo.dApp.dApp.getProperties(self, propertySequence=(), propsToSkip=(), ignoreErrors=False, \*propertyArguments)
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

.. _no-170:

.. function:: dabo.dApp.dApp.initEvents(self)
   :noindex:


   
   Hook for subclasses. User code should do custom event binding
   here, such as::
   
       self.bindEvent(dEvents.GotFocus, self.customGotFocusHandler)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-171:

.. function:: dabo.dApp.dApp.initProperties(self)
   :noindex:


   
   Hook for subclasses. User subclasses should set properties
   here, such as::
   
       self.Name = "MyTextBox"
       self.BackColor = (192,192,192)
   
   


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-197:

.. function:: dabo.dApp.dApp.raiseEvent(self, eventClass, uiEvent=None, \*args, \**kwargs)
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

.. _no-202:

.. function:: dabo.dApp.dApp.setProperties(self, propDict={}, ignoreErrors=False, \**propKw)
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

.. _no-203:

.. function:: dabo.dApp.dApp.setPropertiesFromAtts(self, propDict={}, ignoreExtra=True, context=None)
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

.. _no-210:

.. function:: dabo.dApp.dApp.super(self, \*args, \**kwargs)
   :noindex:


   This method used to call superclass code, but it's been removed.


Inherited from: :ref:`dabo.dObject.dObject`

-------

.. _no-212:

.. function:: dabo.dApp.dApp.unbindEvent(self, eventClass=None, function=None)
   :noindex:


   
   Remove a previously registered event binding.
   
   Removes all registrations that exist for the given binding for this
   object. If event is None, all bindings for the passed function are
   removed. If function is None, all bindings for the passed event are
   removed. If both event and function are None, all event bindings are
   removed.
   


Inherited from: :ref:`dabo.lib.eventMixin.EventMixin`

-------


|
