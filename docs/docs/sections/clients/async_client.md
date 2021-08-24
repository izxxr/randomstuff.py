# `randomstuff.AsyncClient`

An async version of [`Client`](client.md). All the methods have same name as Client but all methods are coroutine.

## Example
```py
import randomstuff
import asyncio

async def coro(self):
    async with randomstuff.AsyncClient(api_key="api-key") as client:
        response = await client.get_ai_response('Hi there.')
        print(response.message)

loop = asyncio.get_event_loop()
loop.run_until_complete(coro())
```