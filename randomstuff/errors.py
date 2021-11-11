class HTTPError(Exception):
    """Super class for 500s status codes.

    This usually indicates that library couldn't establish a connection with base URL (or API). This is raised
    when API is has something wrong.
    """

    def __init__(self, message, status):
        super().__init__(message)
        self.message = message
        self.status = status


class ArgumentError(Exception):
    """Super class for argument related errors"""

    pass


class InvalidType(Exception):
    """Raised upon invalid (unsupported) type of parameter provided"""

    pass


class InvalidVersionError(ArgumentError):
    """
    Inherits from `ArgumentError`
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Raised upon invalid version passed
    """

    pass


class UnsupportedOperation(Exception):
    """
    Raised upon using AsyncClient class in a synchronous context manager
    """

    pass


class InvalidPlanError(InvalidType):
    """
    Inherits from `ArgumentError`
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Raised upon invalid plan passed
    """

    pass


class InvalidServerError(InvalidType):
    """
    Inherits from `ArgumentError`
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Raised upon invalid server passed
    """

    pass


class InvalidCityError(Exception):
    """
    Inherits from `ArgumentError`
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Raised upon invalid city passed in get_weather method.
    """

    pass


class Forbidden(Exception):
    """Super class for 403, 401 and other related status codes."""

    pass


class PlanNotAllowed(Exception):
    """
    Inherits from `Forbidden`
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Raised when the plan provided is not allowed on the API key. This is usually because you don't have that plan
    bought.
    """

    pass


class BadAPIKey(Exception):
    """
    Inherits from `Forbidden`
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Raised when the API key provided is not valid.
    """

    pass


class RateLimited(Exception):
    """
    Inherits from `Forbidden`
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Raised when the API key is being Rate Limited.
    """

    pass
