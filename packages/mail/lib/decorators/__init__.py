from functools import wraps as _wraps
from flask import request
from packages.mail.env import SECRET_AUTHORIZATION_HEADER


def auth_required(function):
    """Decorator that acts like a middleware for handling authorization within the mailing service API

    Args:
        function (Callable): Request handler function

    Returns:
        Callable: A decorated handler function
    """

    @_wraps(function)
    def decorated_flask_callback(*args, **kwargs):
        authorization_header = request.headers.get("Authorization")

        if (
            authorization_header is None
            or authorization_header != SECRET_AUTHORIZATION_HEADER
        ):
            return {
                "message": "Unauthorized",
            }, 401

        return function(*args, **kwargs)

    return decorated_flask_callback
