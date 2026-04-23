from functools import wraps
from flask import redirect, url_for, request

def authorized(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.cookies.get("access_token")

        if not token:
            return redirect(url_for("auth.login"))

        return func(*args, **kwargs)
    return wrapper