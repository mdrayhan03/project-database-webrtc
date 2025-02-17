import json
from channels.generic.websocket import AsyncWebsocketConsumer

class VideoChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)

            # Check if 'message' exists in the received data
            message = data.get("message")
            if message is None:
                await self.send(text_data=json.dumps({
                    "error": "Missing 'message' key in received data"
                }))
                return

            # Broadcast the message to the group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message
                }
            )

        except json.JSONDecodeError:
            await self.send(text_data=json.dumps({
                "error": "Invalid JSON format"
            }))

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({'message': event['message']}))