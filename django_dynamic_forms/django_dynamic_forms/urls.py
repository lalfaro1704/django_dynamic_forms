# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(
        regex="^DynamicForm/~create/$",
        view=views.DynamicFormCreateView.as_view(),
        name='DynamicForm_create',
    ),
    url(
        regex="^DynamicForm/(?P<pk>\d+)/~delete/$",
        view=views.DynamicFormDeleteView.as_view(),
        name='DynamicForm_delete',
    ),
    url(
        regex="^DynamicForm/(?P<pk>\d+)/$",
        view=views.DynamicFormDetailView.as_view(),
        name='DynamicForm_detail',
    ),
    url(
        regex="^DynamicForm/(?P<pk>\d+)/~update/$",
        view=views.DynamicFormUpdateView.as_view(),
        name='DynamicForm_update',
    ),
    url(
        regex="^DynamicForm/$",
        view=views.DynamicFormListView.as_view(),
        name='DynamicForm_list',
    ),
	url(
        regex="^DynamicAttribute/~create/$",
        view=views.DynamicAttributeCreateView.as_view(),
        name='DynamicAttribute_create',
    ),
    url(
        regex="^DynamicAttribute/(?P<pk>\d+)/~delete/$",
        view=views.DynamicAttributeDeleteView.as_view(),
        name='DynamicAttribute_delete',
    ),
    url(
        regex="^DynamicAttribute/(?P<pk>\d+)/$",
        view=views.DynamicAttributeDetailView.as_view(),
        name='DynamicAttribute_detail',
    ),
    url(
        regex="^DynamicAttribute/(?P<pk>\d+)/~update/$",
        view=views.DynamicAttributeUpdateView.as_view(),
        name='DynamicAttribute_update',
    ),
    url(
        regex="^DynamicAttribute/$",
        view=views.DynamicAttributeListView.as_view(),
        name='DynamicAttribute_list',
    ),
	]
