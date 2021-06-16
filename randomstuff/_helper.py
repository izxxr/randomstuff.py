import inspect
from .errors import *

def _warn(client, warning):
    if client.suppress_warnings:
        return
    else:
        print("\u001b[33m"+"[WARNING] "+warning)
        print("\u001b[36m"+"\n[INFO] Disable warnings by setting suppress_warnings to `True` in client." + "\u001b[0m")

def _check_coro(client):
    """Private method to initiate warning if the enivornment is asynchronus"""
    tup = inspect.stack()[2]
    try:
        if inspect.iscoroutinefunction(tup[0].f_globals[tup[3]]):
            _warn(client, "It seems you're using randomstuff.Client in an async enivornment. It is strongly recommended that you use randomstuff.AsyncClient to avoid blocking functions.")
    except KeyError:
        return

def _check_status(response):
    try:
        status = response.status_code
    except AttributeError:
        status = response.status

    if status == 401:
        raise BadAPIKey(response.text)
        return

    elif status == 403:
        raise PlanNotAllowed(response.text)
        return

    elif status >= 500:
        if type(response).__name__ == 'Response': # Client
            raise HTTPError(f"An error occured while connecting to the API. Returned with status code: {response.status_code}", response.status_code)
            return
        else:
            raise HTTPError(f"An error occured while connecting to the API. Returned with status code: {response.status}", response.status)
