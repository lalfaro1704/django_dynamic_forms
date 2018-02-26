=====
Usage
=====

To use Django Dynamic Forms in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_dynamic_forms.apps.Config',
        ...
    )

Add Django Dynamic Forms's URL patterns:

.. code-block:: python

    from django_dynamic_forms import urls as django_dynamic_forms_urls


    urlpatterns = [
        ...
        url(r'^', include(django_dynamic_forms_urls)),
        ...
    ]
