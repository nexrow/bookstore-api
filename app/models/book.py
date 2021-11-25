from app.database.db import db
import uuid

class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.String(40), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(80))
    author = db.Column(db.String(80))
    genre = db.Column(db.String(50))
    seller = db.Column(db.String(50))

    def __init__(self, title, author, genre, seller):
        self.title = title
        self.author = author
        self.genre = genre
        self.seller = seller

    def json(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "seller": self.seller
        }, 200

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def remove_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_book_by_title(cls, title):
        return cls.query.filter_by(title=title).first()

    @classmethod
    def find_book_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
