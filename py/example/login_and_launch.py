import asyncio

from src.main import CodinAPI
async def main():
    user = CodinAPI()
    json = await user.login('canrrwxnectmuqptat@upived.online','12345678')
    print(json)

asyncio.run(main())