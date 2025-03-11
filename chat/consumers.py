import json
import uuid
from channels.generic.websocket import AsyncWebsocketConsumer

class VideoChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        self.user_id = str(uuid.uuid4())  # Unique ID for each user

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

        # Notify others that a new user joined
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "user_joined",
                "user_id": self.user_id
            }
        )

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        data["sender"] = self.user_id  # Attach sender's ID

        await self.channel_layer.group_send(
            self.room_group_name,
            {**data, "type": data["type"]}
        )

    async def user_joined(self, event):
        if event["user_id"] != self.user_id:
            await self.send(text_data=json.dumps({"type": "user-joined", "user_id": event["user_id"]}))

    async def offer(self, event):
        if event["user_id"] != self.user_id:
            await self.send(text_data=json.dumps(event))

    async def answer(self, event):
        if event["user_id"] != self.user_id:
            await self.send(text_data=json.dumps(event))

    async def ice_candidate(self, event):
        if event["user_id"] != self.user_id:
            await self.send(text_data=json.dumps(event))
