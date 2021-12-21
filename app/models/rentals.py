from datetime import datetime
from time import tzname

from app.database.db import db
import uuid

class Rental(db.Model):
    __tablename__ = 'rentals'
    id = db.Column(db.String(40), primary_key=True, default=lambda: str(uuid.uuid4()))
    book_id = db.Column(db.String(40), db.ForeignKey('books.id'))
    user_id = db.Column(db.String(40), db.ForeignKey('users.id'))
    rented_at = db.Column(db.DateTime(timezone=True), default=datetime.now(tzname))

    def json(self):
        return {
            "id": self.id,
            "book_id": self.book_id,
            "user_id": self.user_id,
            "rented_at": self.rented_at,
        }
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def remove_from_db(self):
        db.session.remove(self)
        db.session.commit(self)
    
    @classmethod
    def get(cls, id):
        return cls.query.get(id)
    
    @classmethod
    def get_rental(cls, book_id, user_id):
        return cls.query.filter(Rental.book_id == book_id, Rental.user_id == user_id).first()
