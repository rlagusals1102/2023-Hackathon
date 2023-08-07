import json
from channels.generic.websocket import AsyncWebsocketConsumer
# import pyrebase
import datetime

config = {
    "apiKey": "AIzaSyCATVf9W0--lK3S3XrjF9JeubttsAA0MeU",
    "authDomain": "Hackathon.firebaseapp.com",
    "databaseURL": "https://Hackathon-default-rtdb.firebaseio.com",
    "projectId": "Hackathon",
    "storageBucket": "Hackathon.appspot.com",
    "messagingSenderId": "236361789108",
    "appId": "1:236361789108:web:5e583d23c87812275331e1",
    "measurementId": "G-VFRLX52PT7"
}

# # firebase = pyrebase.initialize_app(config)
# authe = firebase.auth()
# database = firebase.database()


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        print("connected")
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        now = datetime.now().strftime("%Y-%m-%d:%H:%M:%S")

        # database.child('message').child(self.room_name).update({message: now})

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))