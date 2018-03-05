# Core Django imports
from django.contrib import admin

# Imports from project
from .models import (DynamicForm, DynamicAttribute, FormAttribute,
                     DynamicOptionSelects, DynamicSelectList)


class DynamicAttributeAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">input</i>'
    list_display = ('name', 'field_type', )
    list_filter = ['name', 'field_type']


class DynamicFormAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">reorder</i>'
    list_display = ('name', 'parent', 'code', 'is_wizard' )
    list_filter = ['name']
    readonly_fields = ('code', )


class FormAttributeAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">reorder</i>'
    list_display = ('dynamic_form', 'dynamic_attribute', 'css_class', )
    list_filter = ['dynamic_form']


class DynamicOptionSelectsInlineAdmin(admin.ModelAdmin):
    model = DynamicOptionSelects


class DynamicSelectListAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">reorder</i>'
    list_display = ('dynamic_form', 'dynamic_attribute', 'css_class', )
    list_filter = ['dynamic_form']
    inlines = ['DynamicOptionSelectsInlineAdmin']


admin.site.register(DynamicAttribute, DynamicAttributeAdmin)
admin.site.register(DynamicForm, DynamicFormAdmin)
admin.site.register(FormAttribute, FormAttributeAdmin)
admin.site.register(DynamicSelectList, DynamicSelectListAdmin)
admin.site.register(DynamicOptionSelects)