# randomstuff.py
An easy to use python API wrapper for the Random Stuff API.

- Easy-to-use & Organized
- Supports both async and sync
- Supports both v2 and v3 versions of API
- Supports all type of API plans

## Quickstart
Firstly make sure to [get the API key from here](https://api.pgamerx.com/register)

Here are few examples to get you started.

### Getting AI response
```py
import randomstuff

client = randomstuff.Client(key='api-key-here')

response = client.get_ai_response("Hi there")
client.close()
print(response)
```

### Getting random joke
```py
import randomstuff

client = randomstuff.Client(key='api-key-here')

response = client.get_joke(type="any")
client.close()
print(response.joke)
```

### Getting random image
```py
import randomstuff

client = randomstuff.Client(key='api-key-here')

response = client.get_image(type="any")
client.close()
print(response)
```

## Async Support
This library also supports async usage.
```py
import randomstuff
import asyncio

client = randomstuff.AsyncClient(key="api-key-here")

def coro():
  response = await client.get_ai_response("Hello world")
  await client.close()  
  print(response)

loop = asyncio.get_event_loop()
loop.run_until_complete(coro())
```
