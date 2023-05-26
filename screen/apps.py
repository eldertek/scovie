from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ScreenAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'screen'
    verbose_name = _('Screen')
