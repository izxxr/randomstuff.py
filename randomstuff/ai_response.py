from typing import List, Union, Optional

class AIResponse:
    """Represents an AI response returned from `get_ai_response` method.
    
    Attribues
    ---------

    message : The main message.
    response_time : The response time returned by API. (NoneType in V3)
    """
    def __init__(self, data):
        # Universal

        self._message : str = data[0].get('message')

        # Version 3 specific

        self._success : bool = data[0].get('success', None) # NoneType when using version 4
        self._api_key : str = data[0].get('api_key', None) # NoneType when using version 4
        
        # Version 4 specific.

        if not self._success:
            self._response_time : Optional[str] = data[1].get('response_time') # NoneType in version 3
        else:
            self._response_time : Optional[str] = None

        return

    @property
    def success(self):
        return self._success

    @property
    def api_key(self):
        return self._api_key

    @property
    def response_time(self):
        return self._response_time

    @property
    def message(self):
        return self._message
    

    def __repr__(self):
        return "<AIResponse message={message} response_time={response_time}>".format(message=self.message, response_time=self.response_time)

    def __str__(self):
        return self.message