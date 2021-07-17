from typing import List, Union, Optional


class Waifu:
    """Represents a waifu returned by API

    Attributes
    ----------
    
    url (str) : The URL to waifu image.
    """
    def __init__(self, data):
        self._url = data.get('url')
        
    @property
    def url(self):
        return self._url

    def __repr__(self):
        return "<Waifu url={url}>".format(url=self.url)

    def __str__(self):
        return self.url

    