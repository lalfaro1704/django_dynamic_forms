=============================
Django Dynamic Forms
=============================

.. image:: https://badge.fury.io/py/django_dynamic_forms.svg
    :target: https://badge.fury.io/py/django_dynamic_forms

.. image:: https://travis-ci.org/lalfaro1704/django_dynamic_forms.svg?branch=master
    :target: https://travis-ci.org/lalfaro1704/django_dynamic_forms

.. image:: https://codecov.io/gh/lalfaro1704/django_dynamic_forms/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/lalfaro1704/django_dynamic_forms

Dynamic forms creator, you can add some fields and create your own forms.

Documentation
-------------

The full documentation is at https://django_dynamic_forms.readthedocs.io.

Quickstart
----------

Install Django Dynamic Forms::

    pip install django_dynamic_forms

Or install from Github repository::

    pip install -e git://github.com/lalfaro1704/django_dynamic_forms#egg=django_dynamic_forms

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_dynamic_forms',
        ...
    )

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
