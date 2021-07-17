from typing import List, Union, Optional
from dataclasses import dataclass

@dataclass(frozen=True)
class Waifu:
    """
    Represents a waifu returned by API

    Attributes
    ----------
    
      url : str
        The URL to waifu image.
    """
    url : str = None
    

    