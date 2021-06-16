import string
import random
import asyncio
from .objects import Joke
from .client import *
from typing import Union

def generate_uid(level=30):
    """
    Generates a complex and safe to use unique ID. This is very useful when you need a
    key for AI response endpoint.
    
    Parameters:
        level (int) (optional):
            This determines how many chars will there be in the generated key. It is 30 by default.

    Returns:
        str: The generated string

    """
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(level))

def format_joke(joke: Joke, format_as='{setup}... {delivery}'):
    """A simple method to turn a twopart joke into a string.
    
    How this works is, It simply makes twopart joke in provided template, By default is:
    '{setup}... {delivery}'
    
    If the joke is single, it silently returns the joke.

    Parameters:
        joke (Joke) : The joke object to parse.
        separator (str) : The separator, This allows you to customise how joke will be parsed.
                        Defaults to `... `

    Returns:
        str: The formatted joke.

    Raises:
        TypeError: The passed argument isn't a Joke object.
    """
    if joke.type == 'single':
        return joke
    else:
        joke.joke = format_as.format(setup=joke.joke['setup'], delivery=joke.joke['delivery'])
        return joke

def get_safe_joke(client: Union[Client, AsyncClient], type:str='any'):
    """A highly useful method to get a joke marked safe.
    
    Jokes usually returned are safe 90% of the time but this function can filter any 'unsafe' joke.
    """
    if isinstance(client, AsyncClient):
        loop = asyncio.get_event_loop()
        joke = loop.run_until_complete(client.get_joke(type))

        while not joke.safe:
            joke = loop.run_until_complete(client.get_joke(type))

        return joke

    if isinstance(client, Client):
        joke = client.get_joke(type)
        while not joke.safe:
            joke = client.get_joke(type)

        return joke


    
