<div>
  <h1 align='center'>
    randomstuff.py
  </h1>
</div>
<div>
  <p align='center'>
    <img src=https://img.shields.io/pypi/dm/randomstuff.py?color=success&label=PyPi%20Downloads&style=flat-square>
    <img src=https://img.shields.io/github/issues/nerdguyahmad/randomstuff.py?color=success&label=Active%20Issues&style=flat-square>
    <img src=https://img.shields.io/badge/License-MIT-informational>
    <img src=https://img.shields.io/badge/Stable_Version-1.6.0-informational>
  </p>
  <p align='center'>
    An easy to use, feature rich, highly customisable and async pythonic API wrapper for the Random Stuff API.
  </p>
</div>
<br>

## Features
- Easy-to-use & Organized
- Customisable
- Designed to be as optimized as possible
- Wraps the entire API including both versions, 3 and 4.
- Supports both async and sync
- Supports all type of API plans
- All classes are well [documented](https://nerdguyahmad.gitbook.io/randomstuff)
- Actively maintained, Remains up-to-date with all updates.

## Installation
Installation can be done easily using the python package manager `pip`
```bash
pip install randomstuff.py
```

## Quickstart
Firstly make sure to [get the API key from here](https://api.pgamerx.com/register)

Here are few examples to get you started.

### Getting AI response
```py
import randomstuff

with randomstuff.Client(api_key='api-key-here') as client:
  response = client.get_ai_response("Hi there")
  print(response.message)
```

### Getting random joke
```py
import randomstuff

with randomstuff.Client(api_key='api-key-here') as client:
  joke = client.get_joke(type="any")
  print(response.joke)
```

### Getting random image
```py
import randomstuff

with randomstuff.Client(api_key='api-key-here') as client:
  image = client.get_image(type="any")
  print(response)
```

### Getting weather
```py
import randomstuff

with randomstuff.Client(api_key='api-key-here') as client:
  weather = client.get_weather("new york")
  # print(weather) # Uncomment to see full object.
  print("Current weather in {} is {} degree centigrade".format(weather.location.name, weather.current.temprature))
```

## Async Support
This library also supports async usage.
```py
import randomstuff
import asyncio

async def coro():
  async with randomstuff.AsyncClient(api_key="api-key-here") as client:
    response = await client.get_ai_response("Hello world")
    print(response.message)

loop = asyncio.get_event_loop()
loop.run_until_complete(coro())
```
  
## Contribution
This library is powered by community contributions. Feel free to open a pull requests and improve this library. Please consider following points:
- Briefly explain what you did.
- Use this template after your PR description and mark certain checkboxes with `x` as per your PR.
```md
- [ ] This is a code change (Improvement, bug fix, new feature)
  - [ ] Bug fix
  - [ ] Improvement
  - [ ] Feature added

- [ ] The change is not a code change (ReadMe change, examples add, examples update etc.)
  - [ ] README change
  - [ ] Example Change
    - [ ] Added Example
    - [ ] Removed Example
    - [ ] Updated Example
  
- [ ] The change are tested
- [ ] Change is breaking change
```
