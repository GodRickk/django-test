import asyncio
from django.apps import AppConfig
from .websocket_app.tasks import generate_random_number
from asgiref.sync import async_to_sync


class RandomNumberAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'random_number_app'


async def ready(self):
    asyncio.create_task(generate_random_number())