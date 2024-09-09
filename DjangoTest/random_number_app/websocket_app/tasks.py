import asyncio
from json import JSONEncoder
import random
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.http import JsonResponse
from celery import shared_task

'''async def generate_random_number():
    channel_layer = get_channel_layer()
    while True:
        number = random.randint(1, 10000)

        await channel_layer.group_send(
            'random_number_group',
            {
                'type': 'send_random_number',
                'number': number
            }
        )
        await asyncio.sleep(1)'''

@shared_task
def generate_random_number():
    number = random.randint(1, 10000)
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'random_number_group',
        {
            'type': 'send_random_number',
            'number': number,
        }
    )
    return {'number': number}