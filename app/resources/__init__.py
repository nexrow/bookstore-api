from flask.blueprints import Blueprint
from flask_restx import Api

from .user import api as user_api

authorizations = {
    'apitoken': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'API-TOKEN',
        'description': 'Token for authorization the Bookstore app'
    }
}

api_blueprint = Blueprint("Bookstore API", __name__)
api = Api(
        api_blueprint,
        title="Bookstore API",
        version="1.0",
        authorizations=authorizations,
        security='apitoken'
)

# Initializing the API
api.add_namespace(user_api)
