from django.apps import AppConfig


class RformConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Rform'

    def ready(self):
        import Rform.signals