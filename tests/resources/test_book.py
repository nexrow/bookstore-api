import json

def books_json(title,author,genre,seller):
    return json.dumps(
        {
            "title": title,
            "author": author,
            "genre": genre,
            "seller": seller,
        }
    )

def test_book_should_add(client):
    res = client.post(
        '/api/books',
        data = books_json("Harry Potter", "J.K. Rowling", "Adventorious","Bezos"),
        content_type='application/json'
    )

    assert res.status_code == 200

def should_not_add_book_missing_title(client):
    book_json =  {
        "author": "author",
        "genre": "genre",
        "seller": "seller",
    }

    res = client.post(
        '/api/books',
        data = book_json,
        content_type = 'application/json'
    )

    assert res.status_code == 400

def should_not_add_book_missing_author(client):
    book_json =  {
        "title": "title",
        "genre": "genre",
        "seller": "seller",
    }

    res = client.post(
        '/api/books',
        data = book_json,
        content_type = 'application/json'
    )

    assert res.status_code == 400

def should_not_add_book_missing_genre(client):
    book_json =  {
        "title" : "title",
        "author": "author",
        "seller": "seller",
    }

    res = client.post(
        '/api/books',
        data = book_json,
        content_type = 'application/json'
    )

    assert res.status_code == 400

def should_not_add_book_missing_seller(client):
    book_json =  {
        "title": "title",
        "author": "author",
        "genre": "genre",
    }

    res = client.post(
        '/api/books',
        data = book_json,
        content_type = 'application/json'
    )

    assert res.status_code == 400

def should_not_add_book_when_existing_book(client):
    res = client.post(
    '/api/books',
    data = books_json("Harry Potter123", "J.K. Rowling123", "Adventorious123","Bezos123"),
    content_type='application/json'
    )

    assert res.status_code == 200

    res = client.post(
    '/api/books',
    data = books_json("Harry Potter123", "J.K. Rowling123", "Adventorious123","Bezos123"),
    content_type='application/json'
    )

    assert res.status_code == 400
