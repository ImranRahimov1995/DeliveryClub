from django.apps import AppConfig


class DeliveryClubConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.delivery_club'

    def ready(self):
        import apps.delivery_club.signals
