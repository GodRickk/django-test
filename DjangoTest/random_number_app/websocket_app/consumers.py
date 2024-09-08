import json
from random import randint
from time import sleep
from channels.generic.websocket import WebsocketConsumer


class RandomNumberConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        
        while True:
            num = randint(1, 10000)
            self.send(json.dumps({"number": num}))
            sleep(5)

        '''await self.channel_layer.group_add(
            'random_number_group',
            self.channel_name
        )


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            'random_number_group',
            self.channel_name
        )


    async def send_random_number(self, event):
        number = event['number']
        await self.send(text_data=json.dumps({
            'number': number
        }))'''