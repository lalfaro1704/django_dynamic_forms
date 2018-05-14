# -*- coding: utf-8 -*-
import unicodedata
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Group

from model_utils.models import TimeStampedModel, SoftDeletableModel
from django.utils.translation import ugettext_lazy as _


FIELD_TYPE = (
    ('a', _('a')),
    ('input', _('input')),
    ('textarea', _('textarea')),
    ('checkbox', _('checkbox')),
    ('radio', _('radio')),
    ('select', _('select')),
    ('div', _('div')),
    ('label', _('label')),
    ('button', _('button')),
    ('span', _('span')),
    ('switch', _('switch')),
    ('ngb-accordion', _('ngb-accordion')),
    ('ngb-panel', _('ngb-panel')),
    ('ng-template', _('ng-template')),
    ('hr', _('hr')),
    ('i', _('i')),
    ('p', _('p')),
    ('h1', _('h1')),
    ('h2', _('h2')),
    ('h3', _('h3')),
    ('h4', _('h4')),
    ('h5', _('h5')),
    ('h6', _('h6')),
)


class DynamicParameter(TimeStampedModel):
    key  = models.CharField(
        max_length=100,
        verbose_name=_('key'))
    value = models.CharField(
        verbose_name=_('value'),
        max_length=256,
        null=True,
        blank=True)

    class Meta:
        verbose_name = _('dynamic parameter')
        verbose_name_plural = _('dynamic parameters')

    def __str__(self):
        output = '{}'.format(self.key)
        if self.value:
            output = '{}="{}"'.format(self.key, self.value)
        return output


class ListName(models.Model):
    name  = models.CharField(
        max_length=256,
        verbose_name=_('name'))
    select_list = models.ForeignKey(
        'DynamicAttribute',
        on_delete=models.CASCADE,
        verbose_name=_('select list'),
        null=True,
        blank=True)

    class Meta:
        verbose_name = _('list name')
        verbose_name_plural = _('list names')

    def __str__(self):
        return '{}'.format(self.name)


class ListOptionSelect(models.Model):
    name = models.CharField(
        verbose_name=_('name'),
        max_length=256)
    list_name = models.ManyToManyField(
        'ListName',
        verbose_name=_('lists name'))
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
    )

    class Meta:
        verbose_name = _('list option select')
        verbose_name_plural = _('lists option select')

    def __str__(self):
        return "{}".format(self.name)


class DynamicAttribute(TimeStampedModel):
    element_type  = models.CharField(
        max_length=100,
        verbose_name=_('element type'),
        choices=FIELD_TYPE)
    id_element = models.CharField(
        verbose_name=_('id'),
        max_length=256,
        unique=True,
        help_text=_('Value for HTML attribute (id="example").'))
    default_value = models.CharField(
        verbose_name=_('default value'),
        max_length=256,
        null=True,
        blank=True)
    parent = models.ForeignKey(
        'DynamicAttribute',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name=_('parent'))
    parameters = models.ManyToManyField(
        DynamicParameter,
        null=True,
        blank=True,
        verbose_name=_('parameters')
    )
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
    )
    order = models.DecimalField(
        max_digits=20,
        decimal_places=10,
        verbose_name=_('order'))

    class Meta:
        verbose_name = _('dynamic attribute')
        verbose_name_plural = _('dynamic attributes')

    def __str__(self):
        return "{} {}".format(self.id_element, self.element_type)


class SimpleOptionSelects(TimeStampedModel):
    code  = models.CharField(
        max_length=100,
        verbose_name=_('code'))
    name = models.CharField(
        verbose_name=_('name'),
        max_length=256)
    parent = models.ForeignKey(
        'DynamicAttribute',
        on_delete=models.CASCADE,
        verbose_name=_('parent'))

    class Meta:
        verbose_name = _('simple option select')
        verbose_name_plural = _('simple option select')

    def __str__(self):
        return "{}".format(self.name)


class DynamicForm(TimeStampedModel):
    name = models.CharField(
        verbose_name=_('name'),
        max_length=256)
    css_class = models.CharField(
        verbose_name=_('css class'),
        max_length=256,
        blank=True,
        null=True)
    code = models.CharField(
        verbose_name=_('code'),
        blank=True,
        null=True,
        max_length=256)
    target = models.CharField(
        verbose_name=_('target'),
        blank=True,
        null=True,
        max_length=256,
        help_text=_('Specifies the target of the address in the action '
                    'attribute (default: _self).'))
    action = models.CharField(
        verbose_name=_('action'),
        blank=True,
        null=True,
        max_length=256,
        help_text=_('Specifies an address (url) where to submit '
                    'the form (default: the submitting page).'))
    method = models.CharField(
        verbose_name=_('method'),
        blank=True,
        null=True,
        max_length=256,
        help_text=_('Specifies the HTTP method used when '
                    'submitting the form (default: GET).'))
    enctype = models.CharField(
        verbose_name=_('enctype'),
        blank=True,
        null=True,
        max_length=256,
        help_text=_('Specifies the encoding of the submitted data '
                    '(default: is url-encoded).'))
    is_wizard = models.BooleanField(
        default=False,
        verbose_name=_('is wizard?'))
    attribute = models.ManyToManyField(
        DynamicAttribute,
        through='FormAttribute',
        through_fields=('dynamic_form', 'dynamic_element'),
        verbose_name=_('attribute')
    )
    parameters = models.ManyToManyField(
        DynamicParameter,
        null=True,
        blank=True,
        verbose_name=_('parameters')
    )
    parent = models.ForeignKey(
        'DynamicForm',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name=_('parent'))
    order = models.DecimalField(
        max_digits=20,
        decimal_places=10,
        verbose_name=_('order'))

    class Meta:
        verbose_name = _('dynamic form')
        verbose_name_plural = _('dynamic forms')

    def __str__(self):
        return "{}".format(self.name)


class FormAttribute(TimeStampedModel):
    is_required = models.BooleanField(
        default=False,
        verbose_name=_('is required?'))
    dynamic_form = models.ForeignKey(
        DynamicForm,
        on_delete=models.CASCADE,
        verbose_name=_('form'))
    dynamic_element = models.ForeignKey(
        DynamicAttribute,
        on_delete=models.CASCADE,
        verbose_name=_('element'))
    order = models.DecimalField(
        max_digits=20,
        decimal_places=10,
        verbose_name=_('order'))

    class Meta:
        verbose_name = _('form attribute')
        verbose_name_plural = _('form attribute')

    def __str__(self):
        return "{}".format(self.dynamic_element)
