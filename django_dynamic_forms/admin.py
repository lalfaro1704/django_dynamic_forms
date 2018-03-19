# Core Django imports
from django.contrib import admin

# Imports from project
from .models import (DynamicForm, DynamicAttribute, FormAttribute,
                     SimpleOptionSelects, DynamicParameter)


class DynamicAttributeAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">input</i>'
    search_fields = ('id_element', 'element_type', )
    list_display = ('id_element', 'element_type','created', )
    ordering = ('-created',)
    filter_horizontal = ('parameters', )


class DynamicFormAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">reorder</i>'
    list_display = ('name', 'parent', 'code', 'is_wizard', 'created')
    search_fields = ('name', 'parent__name', 'code')
    list_filter = ['created', 'is_wizard', ]
    ordering = ('-created',)
    fields = ('name', 'css_class', 'action', 'method',
              'enctype', 'parent', 'order', 'is_wizard')


class FormAttributeAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">reorder</i>'
    list_display = ('dynamic_form', 'dynamic_attribute', )
    list_filter = ['dynamic_form']


class SimpleOptionSelectsAdmin(admin.ModelAdmin):
    
    def get_form(self, request, obj=None, **kwargs):
        form = super(SimpleOptionSelectsAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['parent'].queryset = DynamicAttribute.objects.filter(element_type='select')
        return form


admin.site.register(DynamicAttribute, DynamicAttributeAdmin)
admin.site.register(DynamicForm, DynamicFormAdmin)
admin.site.register(FormAttribute, FormAttributeAdmin)
admin.site.register(SimpleOptionSelects, SimpleOptionSelectsAdmin)
admin.site.register(DynamicParameter)