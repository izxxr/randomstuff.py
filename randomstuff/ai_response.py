from typing import List, Union, Optional
from dataclasses import dataclass

@dataclass(frozen=True)
class AIResponse:
    """Represents an AI response returned from `get_ai_response` method.
    
    Attribues
    ---------

      message : str
        The main message.

      response : str
        An alias for message.

      response_time : str
        The response time returned by API. This is `None` in version 3 and 5.

      success : bool
        The success status. This is `None` in version 4 and 5.

      api_key : str
        The API key used to fetch the response. This is `None` in version 4 and 5.

      uid : int
        The unique ID used to get resopnse

      server : str
        The server from which response was got.
    """

    # All versions
    message: str = None
    response: str = message
    
    # Version 3
    success: bool = None
    api_key: str = None

    # Version 4
    response_time: bool = None

    # Version 5
    uid: int = None
    server: str = None