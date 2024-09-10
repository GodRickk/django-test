import asyncio
from django.apps import AppConfig
from django.core.signals import request_finished
from django.dispatch import receiver
from django.db.models.signals import post_migrate
from .websocket_app.tasks import generate_random_number
from asgiref.sync import async_to_sync


class RandomNumberAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'random_number_app'

    def ready(self):
        from .models import RandomNumber
        # post_migrate.connect(runner, sender=self)

    '''def ready(self):
    # Используем сигнал, чтобы убедиться, что все приложения загружены
        request_finished.connect()'''


'''@receiver(post_migrate)
def runner(sender, **kwargs):
    generate_random_number.delay()'''