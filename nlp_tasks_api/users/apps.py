from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class UsersConfig(AppConfig):
    name = 'nlp_tasks_api.users'
    verbose_name = _('App Users')
