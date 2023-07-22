import time
from KickAPI import KickAPI
from KickSocket import KickSocket

CHANNEL_USERNAME=''

BOT_USERNAME=''
BOT_PASSWORD=''

kick_api = KickAPI()
channel_info = kick_api.get_channel_info(CHANNEL_USERNAME)

def testing(chatroom_id, username, args):
    tail = ' '.join(args)
    kick_api.send_message(chatroom_id, f'{tail}')

kick_api.login(BOT_USERNAME, BOT_PASSWORD)

chat_socket = KickSocket()
chat_socket.add_command('test', testing)
chat_socket.connect(channel_info['chatroom_id'])

while True:
    time.sleep(100)
