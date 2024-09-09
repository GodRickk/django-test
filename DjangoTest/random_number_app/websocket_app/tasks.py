import asyncio
import random
#from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

'''async def generate_random_numbers():
    channel_layer = get_channel_layer()
    while True:
        number = random.randint(1, 10000)

        await async_to_sync(channel_layer.group_send)(
            'random_number_group',
            {
                'type': 'send_random_number',
                'number': number
            }
        )
        await asyncio.sleep(5)'''