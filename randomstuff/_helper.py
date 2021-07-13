import inspect
from colorama import init
from .errors import *

def _warn(client, warning) -> None:
    if client.suppress_warnings:
        return
    else:
        init()
        print("\u001b[33m"+"[WARNING] "+warning)
        print("\u001b[36m"+"\n[INFO] Disable warnings by setting suppress_warnings to `True` in client." + "\u001b[0m")

def _check_coro(client) -> None:
    """Private method to initiate warning if the enivornment is asynchronus"""
    tup = inspect.stack()[2]
    try:
        if inspect.iscoroutinefunction(tup[0].f_globals[tup[3]]):
            _warn(client, "It seems you're using randomstuff.Client in an async enivornment. It is strongly recommended that you use randomstuff.AsyncClient to avoid blocking functions.")
    except KeyError:
        return

def _check_status(response) -> None:
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
    
    elif status == 429:
        raise RateLimited(response.text)
        return

    elif status >= 500:
        raise HTTPError(f"An error occured while connecting to the API. Returned with status code: {status}", status=status)
        return
