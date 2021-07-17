from typing import List, Union, Optional
from dataclasses import dataclass


@dataclass(frozen=True)
class JokeFlags:
    """
    Represents a joke's flags

    Attributes
    ----------

      nsfw : bool
        Determines if the joke is marked NSFW or not.

      religious : bool
        Determines if the joke is marked religious or not.

      political : bool
        Determines if the joke is marked political or not.

      racist : bool
        Determines if the joke is marked racist or not.

      sexist : bool
        Determines if the joke is marked sexist or not.

      explicit : bool
        Determines if the joke is marked explicit or not.

    """
    nsfw: bool = None
    religious: bool = None
    political: bool = None
    racist: bool = None
    sexist: bool = None
    explicit: bool = None

@dataclass(frozen=True)
class Joke:
    """
    Represents a Joke

    Attributes
    ----------

      category : str
        The category of joke.
      
      type : str
        The type of joke.

      joke : Union[str, dict]
        The main joke. This can be a `dict` or `str` depending on joke's type.
        If joke's type is single then this will be `str` otherwise it will be a `dict`

      flags : JokeFlags
        The flags of joke. This is a `JokeFlags` object.

      id : int
        The joke's ID.

      safe : bool
        Determines if the joke is marked safe or not.
      
      lang : str
        The language of the joke

      language : str
        An alias for `lang` attribute

    """
    category: str = None
    type: str = None
    joke: Union[str, dict] = None
    flags: JokeFlags = None
    id: int = None
    safe: bool = None
    lang: str = None

    # Aliasing
    language: str = lang
