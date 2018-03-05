# Core Django imports
from django.contrib import admin

# Imports from project
from .models import (DynamicForm, DynamicAttribute, FormAttribute,
					 FormSector)


class DynamicAttributeAdmin(admin.ModelAdmin):
    model = DynamicAttribute
    icon = '<i class="material-icons">input</i>'
    list_display = ('name', 'field_type', )
    list_filter = ['name', 'field_type']


class DynamicFormAdmin(admin.ModelAdmin):
    model = DynamicForm
    icon = '<i class="material-icons">reorder</i>'
    list_display = ('name', 'parent', 'code', 'is_wizard' )
    list_filter = ['name']
    fieldsets = ('name', 'parent', 'is_wizard', )

    def get_form(self, request, obj=None, **kwargs):
        if obj.id:
            self.fieldsets = ('name', 'parent', 'code', 'is_wizard', )
            self.readonly_fields = ('code', )

        form = super(BookAdmin, self).get_form(request, obj, **kwargs)
        return form


class ValueAttributeAdmin(admin.ModelAdmin):
    model = FormAttribute
    icon = '<i class="material-icons">reorder</i>'
    list_display = ('dynamic_form', 'sector', 'dynamic_attribute', )
    list_filter = ['dynamic_form', 'sector']


admin.site.register(DynamicAttribute, DynamicAttributeAdmin)
admin.site.register(DynamicForm, DynamicFormAdmin)
admin.site.register(FormAttribute, ValueAttributeAdmin)