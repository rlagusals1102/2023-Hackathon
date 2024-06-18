from json import loads, dumps
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self) -> None:
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code: int) -> None:
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data: str) -> None:
        message = loads(text_data)['message']
        username = self.scope['user'].username

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
            }
        )

    async def chat_message(self, event: dict) -> None:
        message = event['message']
        username = event['username']

        await self.send(text_data=dumps({
            'message': message,
            'username': username,
        }))
