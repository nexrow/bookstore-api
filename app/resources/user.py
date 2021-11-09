import hashlib

from flask_restful import reqparse
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity

from flask import current_app as app
from flask_restx import Namespace, Resource

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


@api.route('/login')
class UserLogin(Resource):

    def post(self):
        data = _user_parser.parse_args()
        username = (data.get('username') or '').strip()
        password = (data.get('password') or '').strip()

        if not (username and password):
            return {
                'message': 'Missing username or password'
            }, 400

        user = User.find_user_by_username(username)

        if user and user.password == hashlib.sha256(password.encode('utf-8')).hexdigest():
            return {
                'access_token': create_access_token(identity=user.id, fresh=True),
                'refresh_token': create_refresh_token(identity=user.id),
                'message': 'Successfully signed in {}.'.format(user.id),
            }, 200

        return {
            'message': 'Invalid credentials',
        }, 401