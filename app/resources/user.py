from flask_restful import reqparse
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity

from flask import current_app as app
from flask_restx import Namespace

from app.models.user import User

_user_parser = reqparse.RequestParser()
_user_parser.add_argument(
    "username",
    type=str,
    required=True,
    help="This field cannot be blank"
)
_user_parser.add_argument(
    "password",
    type=str,
    required=True,
    help="This field cannot be blank"
)
_user_parser.add_argument(
    "name",
    type=str,
    required=False,
    help="This field cannot be blank"
)
_user_parser.add_argument(
    "email",      
    type=str,
    required=False,
    help="This field cannot be blank"
)

api = Namespace('users', path='/api', description='Users')
