
.. include:: _static/headings.txt

.. module:: dabo.lib.SimpleCrypt

.. _dabo.lib.SimpleCrypt.SimpleCrypt:

================================================
|doc_title|  **SimpleCrypt.SimpleCrypt** - class
================================================

Provides basic encryption for Dabo. Perhaps a better term would
be 'obscure' rather than 'encrypt', since the latter implies strong
security. Since this class is provided to all Dabo users, anyone with
a copy of Dabo can decrypt your encrypted values.

You can make your application more secure by making sure that the
PyCrypto package is installed, and then setting the application's
'CryptoKey' property to a string that is not publicly discoverable. This
will provide security as strong as the secrecy of this key.

For real-world applications, you should provide your own security
class, and then set the Application's 'Crypto' property to an instance
of that class. That class must provide the following interface:

encrypt(val)
decrypt(val)

Thanks to Raymond Hettinger for the default (non-DES) code, originally found on
http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/266586




|API| Class API
===============


.. autoclass:: dabo.lib.SimpleCrypt.SimpleCrypt

   .. automethod:: dabo.lib.SimpleCrypt.SimpleCrypt.__init__

|
