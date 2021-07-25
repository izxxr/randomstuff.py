import string
import random
import asyncio
from .joke import Joke
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

    if not isinstance(joke, Joke):
        raise TypeError("parameter joke must be of type Joke")

    if joke.type == 'single':
        return joke
    else:
        new_joke = format_as.format(setup=joke.joke['setup'], delivery=joke.joke['delivery'])
        new_flags = {
            'nsfw': joke.flags.nsfw,
            'religious': joke.flags.religious,
            'political': joke.flags.political,
            'racist': joke.flags.racist,
            'sexist': joke.flags.sexist,
            'explicit': joke.flags.explicit
        }

        return Joke(
            category=joke.category,
            type=joke.type,
            joke=new_joke,
            flags=JokeFlags(**new_flags),
            id=joke.id,
            safe=joke.safe,
            lang=joke.lang
            )