
.. include:: _static/headings.txt

.. module:: dabo.settings

.. _dabo.settings:

================================
|doc_title|  **settings module**
================================

|

.. highlight:: python


Dabo Global Settings

Do not modify this file directly. Instead, create a file called
settings_override.py, and copy/paste the settings section below into the
settings_override.py file. This way, when you update Dabo, you won't blow
away your custom tweaks.

Note that creating a settings_override.py isn't the only way to tweak the
settings - your custom code can also just make the settings in the dabo
namespace at runtime, eg::

    import dabo
    dabo.eventLogging = True
    <do stuff>
    dabo.eventLogging = False

.. note::

    settings_override.py is not the appropriate place to put
    application-specific settings, although it may seem at first like an easy
    place to do so.



.. moduleauthor:: Dabo community <dabo-users@leafe.com>





|
