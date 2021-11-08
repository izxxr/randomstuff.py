import inspect
from colorama import init
from .errors import *
from .constants import *


def _warn(client, warning) -> None:
    if client.suppress_warnings:
        return
    init()
    print("\u001b[33m" + "[WARNING] " + warning)
    print(
        "\u001b[36m"
        + "\n[INFO] Disable warnings by setting suppress_warnings to `True` in client."
        + "\u001b[0m"
    )


def _check_coro(client) -> None:
    """Private method to initiate warning if the enivornment is asynchronus"""
    tup = inspect.stack()[2]
    try:
        if inspect.iscoroutinefunction(tup[0].f_globals[tup[3]]):
            _warn(
                client,
                "It seems you're using randomstuff.Client in an async enivornment. It is strongly recommended that you use randomstuff.AsyncClient to avoid blocking functions.",
            )
    except KeyError:
        return


def _check_status(response) -> None:
    try:
        status = response.status_code
    except AttributeError:
        status = response.status

    if status == 401:
        raise BadAPIKey(response.text)

    elif status == 403:
        raise PlanNotAllowed(response.text)

    elif status == 429:
        raise RateLimited(response.text)

    elif status >= 500:
        raise HTTPError(
            f"An error occured while connecting to the API. Returned with status code: {status}",
            status=status,
        )

def _get_method_images(method: str):
    final = {key: 1 for key in ONE_IMAGE_METHODS}
    for key in TWO_IMAGE_METHODS:
        final[key] = 2
    for key in THREE_IMAGE_METHODS:
        final[key] = 3
    for key in TEXT_METHODS:
        final[key] = 4
    return final[method]

def _validate_method_image(method, **kwargs):
    if method not in ALL_METHODS:
        raise ValueError(
            "Method not supported. "
            "Visit https://api-docs.pgamerx.com/Canvas/optional-customisation/ for valid methods"
        )

    img1, img2, img3, txt = (
        kwargs.get(i) for i in ["img1", "img2", "img3", "txt"]
    )

    images = _get_method_images(method)

    if (images == 1) and (img1 is None):
        raise ValueError(f"img1 is required for method {method}")
    if (images == 2) and (not all([img1, img2])):
        raise ValueError(f"img1 and img2 are required for method {method}")
    if (images == 3) and (not all([img1, img2. img3])):
        raise ValueError(f"img1, img2 and img3 are required for method {method}")
    if (images == 4) and (txt is None):
        raise ValueError(f"txt is required for method {method}")
