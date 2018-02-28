# Core Django imports
from django.contrib import admin

# Imports from project
from .models import (DynamicForm, DynamicAttribute, ValueAttribute)


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
    list_display = ('dynamic_form__name', 'dynamic_attribute__name', 'value', )


admin.site.register(DynamicAttribute, DynamicAttributeAdmin)
admin.site.register(DynamicForm, DynamicFormAdmin)
admin.site.register(ValueAttribute, ValueAttributeAdmin)