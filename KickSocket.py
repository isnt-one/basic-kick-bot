import pysher
import json

PUSHER_KEY='eb1d5f283081a78b932c'
PUSHER_CLUSTER='us2'

class KickSocket:
    def __init__(self):
        self.commands = {}

    def connect_handler(self, payload):
        data = json.loads(payload)
        self.socket_id = data['socket_id']

        print(f'Connected on id: {self.socket_id}')

        self.channel = self.pusher.subscribe(f'chatrooms.{self.chatroom_id}.v2')
        self.channel.bind('App\\Events\\ChatMessageEvent', self.message_received)

    def message_received(self, payload):
        data = json.loads(payload)

        username = data['sender']['username']
        message = data['content']

        if message[0] == '!':
            command = message[1:]
            command_parts = message.split()
            command_name = command_parts[0][1:]

            if len(command_parts) > 1:
                arguments = command_parts[1:]
            else:
                arguments = []

            if not self.commands[command_name]:
                return False

            print(command_name, username, arguments)
            self.commands[command_name](self.chatroom_id, username, arguments)

    def connected(self, payload):
        data = json.loads(payload)
        print(data, self.channel)

    def add_command(self, name, func):
        self.commands[name] = func
        print(f'Added {name}')

    def connect(self, chatroom_id):
        self.chatroom_id = chatroom_id

        self.pusher = pysher.Pusher(
            cluster=PUSHER_CLUSTER,
            key=PUSHER_KEY
        )

        self.pusher.connection.bind('pusher:connection_established', self.connect_handler)
        self.pusher.connect()
