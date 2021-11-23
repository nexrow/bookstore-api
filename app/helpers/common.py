import traceback

from functools import wraps
from flask import flash, redirect, url_for, session, abort
from flask import request, current_app as app
from flask_login import current_user

from app.models.user import User, Role

def is_admin(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        user = User.query.get(1)
        role = user.roles.all()
        roles = [ r.name for r in role ]
        if not 'Admin' in roles:
            abort(403)
        return func(*args, **kwargs)

    return wrapper

status_code_responses = {
    200: 'Success',
    204: 'Success without body',
    400: 'Bad request',
    401: 'Not Authorized',
    403: 'Forbidden',
    500: 'Internal server error',
    503: 'Service unavailable'
}