from typing import List, Union, Optional
class BaseObject:
    """Super class for most of the objects used in the library

    Attributes
    ----------
    data (Union[List[dict], dict]) : The raw data as returned by API.
    is_ai_response (bool) : True if the data is for an AI response
    is_joke (bool) : True if the data is for a joke

    """
    def __init__(self, data : Union[List[dict], dict], **kwargs):
        self.data = data
        self.is_ai_response : bool = kwargs.get('is_ai_response', False)
        self.is_joke : bool = kwargs.get('is_joke', False)

        if self.is_ai_response:
            self.message : str = data[0].get('message')
            self.success : bool = data[0].get('success', None) # NoneType when using version 4
            self.api_key : str = data[0].get('api_key', None) # NoneType when using version 4
            
            if not self.success:
                self.response_time : Optional[str] = data[1].get('response_time') # NoneType in version 3
            else:
                self.response_time : Optional[str] = None
            return

        if self.is_joke:
            if self.data['type'] == 'twopart':
                self.joke = {'setup': self.data['setup'], 'delivery': self.data['delivery']}
            else:
                self.joke = self.data['joke']

        for _ in self.data.keys():
            if _ == 'flags':
                setattr(self, _, Flags(self.data[_]))
            elif _ in ['setup', 'twopart']:
                pass
            else:
                setattr(self, _, self.data[_])


class Joke(BaseObject):
    """Represents a Joke

    Attributes
    ----------

    category (str): The category of joke.
    type (str): The type of joke.
    joke (str or dict): The main joke. This can be a `dict` or `str` depending on joke's type.
                        If joke's type is single then this will be `str` otherwise it will be a `dict`

    flags (randomstuff.Flags): The flags of joke. This is a `randomstuff.Flags` object. 
    id (int): The joke's ID.
    safe (bool): Determines if the joke is marked safe or not.
    lang (str): The language of the joke

    """
    def __init__(self, data):
        super().__init__(data, is_joke=True)

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

class AIResponse(BaseObject):
    """Represents an AI response returned from `get_ai_response` method.
    
    Attribues
    ---------

    message : The main message.
    response_time : The response time returned by API. (NoneType in V3)
    """
    def __init__(self, data):
        super().__init__(data, is_ai_response=True)

    def __str__(self):
        return self.message

    def __repr__(self):
        return "<AIResponse message={} response_time={}>".format(message=self.message, response_time=self.response_time)

class Flags(BaseObject):
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
        super().__init__(data)

    def __repr__(self):
        return '<Flags nsfw={nsfw} religious={religious} political={political} racist={racist} sexist={sexist} explicit={explicit}>'.format(
            nsfw=self.nsfw,
            religious=self.religious,
            political=self.political,
            racist=self.racist,
            sexist=self.sexist,
            explicit=self.explicit,
            )

class Waifu(BaseObject):
    """Represents a waifu returned by API

    Attributes
    ----------
    
    url (str) : The URL to waifu image.
    """
    def __init__(self, data):
        super().__init__(data)

    def __str__(self):
        return self.url

    def __repr__(self):
        return "<Waifu url={url}>".format(url=self.url)
