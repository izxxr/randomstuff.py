## Development Notice
As of April 2023, due to lack of activity and maintanence of Random Stuff API and busy schedule of the maintainer of this package, this package is not being maintained and is not likely to work for the newer (or even older) versions of API.

<div>
  <h1 align='center'>
    randomstuff.py
  </h1>
</div>
<div>
  <p align='center'>
    <img src=https://img.shields.io/pypi/dm/randomstuff.py?color=success&label=PyPi%20Downloads&style=flat-square>
    <img src=https://img.shields.io/badge/Stable_Version-2.0.0-informational>
    <img src=https://img.shields.io/badge/Development_Version-2.5.0-informational>
  </p>
  <p align='center'>
    A simple and easy to use, async-ready API wrapper around Random Stuff API.
  </p>
</div>
<br>

## Features
- Easy to use, pythonic and Object Oriented interface
- Implements the entire API
- Support for both synchronous and asynchronous usage

## Installation
Installation can be done easily using the python package manager `pip`
```sh
python -m pip install -U randomstuff.py
```
To install development (potentially unstable) version:
```sh
python -m pip install git+https://github.com/nerdguyahmad/randomstuff.py
```

## Quickstart
Make sure to [get the API key from here](https://api.pgamerx.com/register)

### Basic Usage
```py
import randomstuff

with randomstuff.Client(api_key='api-key-here') as client:
  response = client.get_ai_response("Hi there")
  print(response.message)
```

### Async Usage
```py
import randomstuf

async with randomstuff.AsyncClient(api_key='api-key-here') as client:
  response = await client.get_ai_response('Hey there')
  print(response.message)
```
More examples can be found in [documentation](https://nerdguyahmad.github.io/randomstuff/examples)
  
## Contribution
Feel free to contribute by either opening an issue or a pull request.

See the [Contribution Guide](.github/CONTRIBUTING.MD) for more info.
