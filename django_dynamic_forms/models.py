# -*- coding: utf-8 -*-
import unicodedata
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from model_utils.models import TimeStampedModel, SoftDeletableModel
from django.utils.translation import ugettext_lazy as _


FIELD_TYPE = (
    ('TXT', _('Text')),
    ('TXB', _('Textarea')),
    ('CHK', _('Checkbox')),
    ('RDO', _('Radio')),
    ('SLT', _('Select'))
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

    def __str__(self):
        return "{} {}".format(self.name, self.field_type)


class DynamicOptionSelects(TimeStampedModel):
    code  = models.CharField(
        max_length=100,
        verbose_name=_('code'))
    name = models.CharField(
        verbose_name=_('name'),
        max_length=256)
    parent = models.ForeignKey(
        'DynamicSelectList',
        on_delete=models.CASCADE,
        verbose_name=_('parent'))

    class Meta:
        verbose_name_plural = _('dynamic option select')

    def __str__(self):
        return "{}".format(self.name)


class DynamicSelectList(TimeStampedModel):
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.DO_NOTHING
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey(
        'content_type',
        'object_id'
    )
    name = models.CharField(
        verbose_name=_('name'),
        max_length=100
    )

    class Meta:
        verbose_name = _('select list')
        verbose_name_plural = _('select lists')

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
        max_length=256)
    is_wizard = models.BooleanField(
        default=False,
        verbose_name=_('is wizard?'))
    attribute = models.ManyToManyField(
        DynamicAttribute,
        through='FormAttribute',
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

    def __str__(self):
        return "{}".format(self.name)

    def elimina_tildes(self, name):
        normalize = unicodedata.normalize('NFD',str(name))
        s = ''.join((c for c in normalize if unicodedata.category(c) != 'Mn'))
        return s

    def form_code(self, name):
        code = name.lower().replace(" ", "_")
        code = self.elimina_tildes(code)
        return code

    def save(self, *args, **kwargs):
        self.code = self.form_code(self.name)
        super(DynamicForm, self).save(*args, **kwargs)


class FormAttribute(TimeStampedModel):
    css_class = models.CharField(
        verbose_name=_('css class'),
        max_length=256,
        blank=True,
        null=True)
    is_required = models.BooleanField(
        default=False,
        verbose_name=_('is required?'))
    dynamic_form = models.ForeignKey(
        DynamicForm,
        on_delete=models.CASCADE,
        verbose_name=_('form'))
    dynamic_attribute = models.ForeignKey(
        DynamicAttribute,
        on_delete=models.CASCADE,
        verbose_name=_('attribute'))

    def __str__(self):
        return "{}".format(self.value)
