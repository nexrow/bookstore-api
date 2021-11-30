import hashlib

from flask_restful import reqparse
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity

from flask import current_app as app
from flask_restx import Namespace, Resource

from app.helpers.common import status_code_responses
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

api = Namespace('users', path='/api/users', description='Users')


@api.route('/<username>')
@api.doc(responses=status_code_responses,
         security=['apitoken']
         )
class Users(Resource):
    @api.doc(description='Get User by username', params={'username': 'Users username. Example: john.'})
    def get(self, username):
        user = User.find_user_by_username(username)
        if user:
            return user.json()

        return {
            "message": "User not found!"
        }, 404


@jwt_required(refresh=True)
@api.route('/<user_id>')
@api.doc(description='Delete a user by id.', params={
    'user_id': 'The user ID. Usually an UUID like: 63755806-e359-455f-9915-8fda80d501db.',
})
class UserDelete(Resource):

    def delete(self, user_id):
        user = User.find_user_by_id(user_id)
        if user:
            user.remove_from_db()
            return {
                "message": "User deleted!"
            }, 200

        return {
            "message": "User not found!"
        }, 404


@api.route('/register')
@api.doc(responses=status_code_responses,
         security=['apitoken'],
         params={
             'username': 'The username. Example: john.',
             'password': 'The password.',
             'name': 'User\'s full  name. Example: John Doe.',
             'email': 'User\'s email like: john.doe@example.com.',
         }
         )
class UserRegister(Resource):
    def post(self):
        data = _user_parser.parse_args()

        username = data["username"]

        if User.find_user_by_username(data["username"]):
            return {
                "message": "User {} exists!".format(data["username"])
            }, 400

        user = User(username, hashlib.sha256(data["password"].encode(
            "utf-8")).hexdigest(), data["name"], data["email"])

        try:
            user.save_to_db()
            return {
                "message": "User {} created!".format(username)
            }, 200
        except:
            return {
                "message": "The user {} was not saved in the database.".format(username)
            }, 500


@api.route('/login')
@api.doc(
    description='Login to generate JWT',
    params={
        'username': 'The username.',
        'password': 'The password.',
    })
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
