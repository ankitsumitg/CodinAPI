import asyncio
from src.main import CodinAPI


async def main():
    user = CodinAPI()
    await user.login(input('Enter Email: '), input('Enter Password: '))
    await user.create_clash()
    print(f'Url to clash is : {user.private_clash_url}')
    await user.close()


asyncio.run(main())