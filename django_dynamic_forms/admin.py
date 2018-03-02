# Core Django imports
from django.contrib import admin

# Imports from project
from .models import (DynamicForm, DynamicAttribute, ValueAttribute,
					 FormSector)


class DynamicAttributeAdmin(admin.ModelAdmin):
    model = DynamicAttribute
    icon = '<i class="material-icons">input</i>'
    list_display = ('name', 'field_type', )
    list_filter = ['name', 'field_type']


class DynamicFormAdmin(admin.ModelAdmin):
    model = DynamicForm
    icon = '<i class="material-icons">reorder</i>'
    list_display = ('name', 'parent', )
    list_filter = ['name']


class ValueAttributeAdmin(admin.ModelAdmin):
    model = ValueAttribute
    icon = '<i class="material-icons">reorder</i>'
    list_display = ('dynamic_form', 'dynamic_attribute', 'value', )
    list_filter = ['dynamic_form', 'dynamic_attribute']


class FormSectorAdmin(admin.ModelAdmin):
    model = FormSector
    icon = '<i class="material-icons">reorder</i>'
    list_display = ('name', 'code', )
    list_filter = ['name', 'code']


admin.site.register(DynamicAttribute, DynamicAttributeAdmin)
admin.site.register(DynamicForm, DynamicFormAdmin)
admin.site.register(ValueAttribute, ValueAttributeAdmin)
admin.site.register(FormSector, FormSectorAdmin)