# -*- coding: utf-8 -*-

from django.db import models

from model_utils.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _


FIELD_TYPE = (
    ('TXT', _('Text')),
    ('TXB', _('Textbox')),
    ('CHK', _('Checkbox')),
    ('RDO', _('Radio'))
)


class DynamicAttribute(TimeStampedModel):
    field_type  = models.CharField(
        max_length=100,
        verbose_name=_('field types'),
        choices=FIELD_TYPE)
    name = models.CharField(
        verbose_name=_('name'),
        max_length=256)

    class Meta:
        verbose_name_plural = _('dynamic attributes')


class DynamicForm(TimeStampedModel):
    name = models.CharField(
        verbose_name=_('name'),
        max_length=256)
    attribute = models.ManyToManyField(
        DynamicAttribute,
        through='ValueAttribute',
        through_fields=('dynamic_form', 'dynamic_attribute'),
        verbose_name=_('attribute')
    )
    parent = models.ForeignKey(
        'DynamicForm',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name=_('parent'))

    class Meta:
        verbose_name_plural = _('dynamic forms')


class ValueAttribute(TimeStampedModel):
    dynamic_form = models.ForeignKey(
        DynamicForm,
        on_delete=models.CASCADE,
        verbose_name=_('form'))
    dynamic_attribute = models.ForeignKey(
        DynamicAttribute,
        on_delete=models.CASCADE,
        verbose_name=_('attribute'))
    value = models.CharField(
        blank=True,
        null=True,
        verbose_name=_('value'),
        max_length=256)