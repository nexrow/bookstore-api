from flask_restful import reqparse
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity

from flask_restx import Namespace, Resource

from app.models.books import Books

_books_parser = reqparse.RequestParser()
_books_parser.add_argument(
    "title",
    type=str,
    required=False,
    help="This field cannot be blank"
)
_books_parser.add_argument(
    "author",
    type=str,
    required=False,
    help="This field cannot be blank"
)
_books_parser.add_argument(
    "genre",
    type=str,
    required=False,
)
_books_parser.add_argument(
    "seller",      
    type=str,
    required=False,
)

api = Namespace('books', path='/api', description='Books')

@api.route('/add')
class BookAdd(Resource):
    def post(self):
        data = _books_parser.parse_args()
        title = data["title"]

        try:            
            title.save_to_db()
            return {
                    "message": "Book {} saved to db!".format(title)
            }, 200
        except:
            return {
                    "message": "The book {} was not saved in the database.".format(title)
            }, 500

@api.route('/get/<id>')
class BookById(Resource):
    def get(self, id):
        id = Books.find_book_by_id(id)
        if id:
            return id.json()

        return {
                "message": "Book id not found!"
        }, 404
