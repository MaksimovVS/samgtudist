from django.apps import AppConfig


class ApiSamgtudistConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_samgtudist'

    def ready(self):
        #коннектим сигналы
        from . import signals
