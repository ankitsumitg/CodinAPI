import asyncio
import aiohttp
from .endpoints import Endpoints


class CodinAPI:
    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self._session = aiohttp.ClientSession(loop=self.loop)
        self.logged_in = False
        self.codin_user = None


    async def login(self, email: str, password: str):
        r = self._session.post(Endpoints.login, json=[email, password, True])
        json = await r.json()
        self.codin_user = json
        self.logged_in = True
        return json

    async def close(self):
        await self._session.close()
