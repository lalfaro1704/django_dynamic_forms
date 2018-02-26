# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from django_dynamic_forms.urls import urlpatterns as django_dynamic_forms_urls

urlpatterns = [
    url(r'^', include(django_dynamic_forms_urls)),
]
