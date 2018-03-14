from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DjangoDynamicFormsConfig(AppConfig):
    name = 'django_dynamic_forms'
    icon = '<i class="material-icons">memory</i>'
    verbose_name = _('Django Dynamic Forms')
