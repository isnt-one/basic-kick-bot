from curl_cffi import requests
import json

class KickAPI:
    def __init__(self):
        self.tokens = {}
        self.logged_in = False
        self.auth_token = None

    def get_tokens(self):
        response = requests.get('https://kick.com/kick-token-provider', impersonate='chrome101')
        return response.json()

    def login(self, username, password):
        self.tokens = self.get_tokens()
        
        response = requests.post('https://kick.com/mobile/login', data={
            'isMobileRequest': True,
            'email': username,
            'password': password,
            self.tokens['nameFieldName']: '',
            self.tokens['validFromFieldName']: self.tokens['encryptedValidFrom']
        }, impersonate='chrome101')

        if response.status_code == 200:
            data = response.json()
            self.auth_token = data["token"]
        else:
            print('Failed to login')

    def send_message(self, chatroom_id, message):
        response = requests.post('https://kick.com/api/v1/chat-messages', data={
            'chatroom_id': chatroom_id,
            'message': message
        }, headers={
            'Authorization': f'Bearer {self.auth_token}',
            'X-Xsrf-Token': self.auth_token
        }, impersonate='chrome101')

        if not response.status_code == 200:
            print(f'Failed to send message in {chatroom_id}')

    def get_channel_info(self, channel_name):
        response = requests.get(f'https://kick.com/api/v2/channels/{channel_name}', impersonate='chrome101')
        channel_data = response.json()

        return {
            'chatroom_name': channel_name,
            'chatroom_id': channel_data['chatroom']['id']
        }
