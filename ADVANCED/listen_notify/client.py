"""
A base snippet of an app that uses Postgres LISTEN/NOTIFY feature with asyncpg.

"""

import asyncio
import asyncpg


MY_QUEUE = asyncio.Queue()


async def callback(connection, pid, channel_name, payload):
    # Function's signature of this form is required by asyncpg add_listener()
    if channel_name == 'my_channel':
        await MY_QUEUE.put(payload)


async def listen_to_the_channel():

    pool = await asyncpg.create_pool(
        database="example_db",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432",
        max_size=20,
    )

    async with pool.acquire() as conn:
        await conn.add_listener('my_channel', callback)
        while True:
            if MY_QUEUE.qsize() == 0:
                await asyncio.sleep(3)
                print('Queue empty')
            else:
                new_item = await MY_QUEUE.get()
                print(f"New item: {new_item}")



if __name__ == "__main__":
    asyncio.run(listen_to_the_channel())