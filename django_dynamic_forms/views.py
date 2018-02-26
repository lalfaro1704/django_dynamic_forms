# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	DynamicForm,
	DynamicAttribute,
)


class DynamicFormCreateView(CreateView):

    model = DynamicForm


class DynamicFormDeleteView(DeleteView):

    model = DynamicForm


class DynamicFormDetailView(DetailView):

    model = DynamicForm


class DynamicFormUpdateView(UpdateView):

    model = DynamicForm


class DynamicFormListView(ListView):

    model = DynamicForm


class DynamicAttributeCreateView(CreateView):

    model = DynamicAttribute


class DynamicAttributeDeleteView(DeleteView):

    model = DynamicAttribute


class DynamicAttributeDetailView(DetailView):

    model = DynamicAttribute


class DynamicAttributeUpdateView(UpdateView):

    model = DynamicAttribute


class DynamicAttributeListView(ListView):

    model = DynamicAttribute

