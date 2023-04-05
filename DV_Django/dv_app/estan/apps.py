from django.apps import AppConfig

class EstanConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'estan'

    def ready(self):
        from dv_app.jobs import updater
        updater.start()