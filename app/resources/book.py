from flask_restful import reqparse
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity

from flask_restx import Namespace, Resource

from app.models.book import Book

_books_parser = reqparse.RequestParser()
_books_parser.add_argument(
    "title",
    type=str,
    required=True,
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

api = Namespace('books', path='/api/books', description='Books')


@api.route('')
@api.expect(_books_parser, validate=True)
@api.doc(description='Add new book', params={
    'title': 'Book\'s title.',
    'author': 'Book\'s author name.',
    'genre': 'Book\'s genre.',
    'seller': 'Book\'s seller.',
})
class BookAdd(Resource):
    def post(self):
        data = _books_parser.parse_args()
        book = Book(data['title'], data['author'],
                    data['genre'], data['seller'])

        try:
            book.save_to_db()
            return {
                "message": "Book saved to db: {}".format(book.id)
            }, 200
        except:
            return {
                "message": "The book was not saved in the database."
            }, 500


@api.route('/<id>')
@api.doc(description='Get a book by ID.')
class BookById(Resource):
    def get(self, id):
        book = Book.find_book_by_id(id)
        if book:
            return book.json()

        return {
            "message": "Book with id {} not found!".format(id)
        }, 404
