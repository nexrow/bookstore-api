from flask_restful import reqparse
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity

from flask import current_app as app
from flask_restx import Namespace, Resource

from app.helpers.common import authorize, status_code_responses, is_admin
from app.models.user import User

import hashlib

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

@api.route('/register')
@api.doc(responses=status_code_responses,
         security=['apitoken']
        )
class UserRegister(Resource):
    def post(self):
        data = _user_parser.parse_args()

        username = data["username"]

        if User.find_user_by_username(data["username"]):
            return {
                    f"message": "User {data[username]} exists!"
            }, 400

        user = User(username, hashlib.sha256(data["password"].encode("utf-8")).hexdigest(), data["name"], data["email"])

        try:            
            user.save_to_db()
            return {
                    f"message": "User {username} created!"
            }, 200
        except:
            return {
                    f"message": "The user {username} was not saved in the database."
            }, 500
