import json
from random import randint
from asyncio import sleep
from channels.generic.websocket import AsyncWebsocketConsumer


class RandomNumberConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            'random_number_group',
            self.channel_name
        )
        
        await self.accept()
        

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            'random_number_group',
            self.channel_name
        )


    async def send_random_number(self, event):
        number = event['number']
        await self.send(text_data=json.dumps({
            'number': number
        }))