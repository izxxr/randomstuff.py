# Getting started
This page shows some quick examples to show off the basic design of this library and to quickly get you started.

---

## Installation
Installation of this package is done using the pip package manager:
```sh
pip install -U randomstuff.py
```

## Getting an API key
You need an API key which you can get from [this link](https://api-info.pgamerx.com/register)

## Basic Client example
`Client` class is the main class to make all API calls.

You can get random AI response to a message using [`Client.get_ai_response()`](sections/clients/client.md) method.

```py
import randomstuff

with randomstuff.Client(api_key="api-key") as client:
    response = client.get_ai_response('Hi there.')
    print(response.message)
```

!!! info "Information"
    The legacy non-context manager way is also supported but in that method, You will have to close the session after usage using [`Client.close()`](sections/clients/client.md)

Some other methods are:

- [`client.get_joke()`](sections/clients/client.md)
- [`client.get_image()`](sections/clients/client.md)
- [`client.get_weather()`](sections/clients/client.md)

## Async usage
This library also supports async usage to use in asynchrounous enivornments.

For async usage, We use [`AsyncClient`](sections/clients/async-client.md) class which is an async version of `Client` class.
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

!!! info "Information"
    This class is exactly same as Client class except all methods are coroutine and asynchrounous. By similar, We mean that all methods have the same name.
