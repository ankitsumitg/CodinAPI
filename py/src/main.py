import asyncio
import aiohttp
import requests
from json import dumps
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
        headers = {'Content-Type': 'application/json', 'Accept': '*/*'}
        data = [email, password, True]
        r = self._session.post(Endpoints.login, json=data, headers=headers)
        self.codin_user = r.json()
        self.user_id = self.codin_user['userId']

    async def create_clash(self):
        headers = {'Content-Type': 'application/json', 'Accept': '*/*'}
        data = [self.user_id, {'SHORT': True}, [], ["FASTEST", "SHORTEST", "REVERSE"]]
        r = self._session.post(Endpoints.createClash, json=data, headers=headers)
        self.private_clash_url = 'https://www.codingame.com/clashofcode/clash/' + r.json()['publicHandle']

    async def close(self):
        await self._session.close()
