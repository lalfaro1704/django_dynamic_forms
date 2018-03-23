# Core Django imports
from django.contrib import admin

# Imports from project
from .models import (DynamicForm, DynamicAttribute, FormAttribute,
                     SimpleOptionSelects, DynamicParameter, ListName,
                     ListOptionSelect)


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
    list_display = ('name', 'parent', 'created', )
    list_filter = ['created', ]
    ordering = ('-created', )
    search_fields = ('name', 'parent__id_element')

    def get_form(self, request, obj=None, **kwargs):
        form = super(SimpleOptionSelectsAdmin, self).get_form(request, obj, **kwargs)
        listname = ListName.objects.all()
        queryset = DynamicAttribute.objects.filter(element_type='select')
        form.base_fields['parent'].queryset = queryset.exclude(listname__in=listname)
        return form


class ListNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'select_list', )

    def get_form(self, request, obj=None, **kwargs):
        form = super(ListNameAdmin, self).get_form(request, obj, **kwargs)
        simple = SimpleOptionSelects.objects.all()
        queryset = DynamicAttribute.objects.filter(element_type='select')
        form.base_fields['select_list'].queryset = queryset.exclude(simpleoptionselects__in=simple)
        return form


admin.site.register(DynamicAttribute, DynamicAttributeAdmin)
admin.site.register(DynamicForm, DynamicFormAdmin)
admin.site.register(FormAttribute, FormAttributeAdmin)
admin.site.register(SimpleOptionSelects, SimpleOptionSelectsAdmin)
admin.site.register(DynamicParameter)
admin.site.register(ListName, ListNameAdmin)
admin.site.register(ListOptionSelect)