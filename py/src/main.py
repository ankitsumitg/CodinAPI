import asyncio

import requests

from .endpoints import Endpoints


class CodinAPI:
    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self._session = requests.Session()
        self.logged_in = False
        self.codin_user = None
        self.user_id = None
        self.private_clash_url = None

    async def login(self, email, password):
        try:
            headers = {'Content-Type': 'application/json', 'Accept': '*/*'}
            data = [email, password, True]
            r = self._session.post(Endpoints.login, json=data, headers=headers)
            self.codin_user = r.json()
            if 'userId' not in self.codin_user:
                raise Exception(f'{"*" * 10} {self.codin_user["message"]} {"*" * 10}')
            self.user_id = self.codin_user['userId']
            self.logged_in = True
        except Exception as e:
            print(e)

    async def create_clash(self):
        if not self.logged_in:
            print(f'{"*" * 10} Not logged in {"*" * 10}')
            return
        headers = {'Content-Type': 'application/json', 'Accept': '*/*'}
        data = [self.user_id, {'SHORT': True}, [], ["FASTEST", "SHORTEST", "REVERSE"]]
        r = self._session.post(Endpoints.createClash, json=data, headers=headers)
        self.private_clash_url = 'https://www.codingame.com/clashofcode/clash/' + r.json()['publicHandle']

    def get_clash_url(self):
        if not self.private_clash_url:
            return f'{"*" * 10} Clash not created {"*" * 10}'
        return self.private_clash_url

    async def close(self):
        self._session.close()