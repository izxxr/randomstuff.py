import randomstuff
import asyncio

async def coro():
  async with randomstuff.AsyncClient(api_key="key") as client:
    response = await client.get_ai_response("Hello world")
    print(response.message)

loop = asyncio.get_event_loop()
loop.run_until_complete(coro())
