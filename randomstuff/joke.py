from typing import List, Union, Optional

class Joke:
    """Represents a Joke

    Attributes
    ----------

    category (str): The category of joke.
    type (str): The type of joke.
    joke (str): The main joke. This can be a `dict` or `str` depending on joke's type.
                        If joke's type is single then this will be `str` otherwise it will be a `dict`

    flags (randomstuff.Flags): The flags of joke. This is a `randomstuff.Flags` object. 
    id (int): The joke's ID.
    safe (bool): Determines if the joke is marked safe or not.
    lang (str): The language of the joke

    """
    def __init__(self, data):
        if data['type'] == 'twopart':
            self._joke = {'setup': data['setup'], 'delivery': data['delivery']}
        else:
            self._joke = self.data['joke']

        for _ in data.keys():
            if _ == 'flags':
                setattr(self, '_'+_, Flags(data[_]))
            elif _ in ['setup', 'twopart']:
                pass
            else:
                setattr(self, '_'+_, data[_])


    @property
    async def joke(self):
        return self._joke

    @property
    def flags(self):
        return self._flags

    @property
    def type(self):
        return self._type

    @property
    def id(self):
        return self._id

    @property
    def safe(self):
        return self._safe
    
    @property
    def lang(self):
        return self._lang
    
    @property
    def category(self):
        return self._category

    def __str__(self):
        if isinstance(self.joke, str):
            return self.joke
        return f"{self.joke['setup']}. {self.joke['delivery']}"

    def __repr__(self):
        return '<Joke category={category} type={type} flags={flags} id={id} safe={safe} lang={lang}>'.format(
            category=self.category,
            type=self.type,
            flags=self.flags,
            id=self.id,
            safe=self.safe,
            lang=self.lang,
            )

class Flags:
    """Represents a joke's flags

    Attributes
    ----------

    nsfw (bool): Determines if the joke is marked NSFW or not.
    religious (bool): Determines if the joke is marked religious or not.
    political (bool): Determines if the joke is marked political or not.
    racist (bool): Determines if the joke is marked racist or not.
    sexist (bool): Determines if the joke is marked sexist or not.
    explicit (bool): Determines if the joke is marked explicit or not.
    """
    def __init__(self, data):
        for flag in data.keys():
            setattr(self, '_'+flag, data[flag])

    @property
    def nsfw(self):
        return self._nsfw

    @property
    def religious(self):
        return self._religious

    @property
    def political(self):
        return self._political

    @property
    def racist(self):
        return self._racist

    @property
    def sexist(self):
        return self._sexist

    @property
    def explicit(self):
        return self._explicit

    def __repr__(self):
        return '<Flags nsfw={nsfw} religious={religious} political={political} racist={racist} sexist={sexist} explicit={explicit}>'.format(
            nsfw=self._nsfw,
            religious=self._religious,
            political=self._political,
            racist=self._racist,
            sexist=self._sexist,
            explicit=self._explicit,
            )