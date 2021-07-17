from typing import List, Union, Optional
from dataclasses import dataclass

@dataclass(frozen=True)
class AIResponse:
    """Represents an AI response returned from `get_ai_response` method.
    
    Attribues
    ---------

      message : str
        The main message.

      response_time : str
        The response time returned by API. This is `None` in version 3.

      success : bool
        The success status. This is `None` in version 4.

      api_key : str
        The API key used to fetch the response. This is `None` in version 4.
    """

    # Both version 3 & 4
    message: str = None
    
    # Version 3
    success: bool = None
    api_key: str = None

    # Version 4
    response_time: bool = None
