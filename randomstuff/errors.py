class HTTPError(Exception):
    """Super class for 500s status codes.

    This usually indicates that library couldn't establish a connection with base URL (or API). This is raised
    when API is has something wrong.
    """
    def __init__(self, message, status_code):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

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

class InvalidPlanError(ArgumentError):
    """
    Inherits from `ArgumentError`
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Raised upon invalid plan passed
    """
    pass

class InvalidServerError(ArgumentError):
    """
    Inherits from `ArgumentError`
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Raised upon invalid server passed
    """
    pass


class Forbidden(Exception):
    """Super class for 403, 401 and other related status codes."""
    pass

class PlanNotAllowed(Exception):
    """
    Inherits from `Forbiddem`
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Raised when the plan provided is not allowed on the API key. This is usually because you don't have that plan
    bought. 
    """
    pass

class BadAPIKey(Exception):
    """
    Inherits from `Forbiddem`
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Raised when the API key provided is not valid.
    """
    pass

