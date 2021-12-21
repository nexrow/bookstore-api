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
        data = books_json("Harry Ptter", "J.K. Rowling", "Adventorious","Bezos"),
        content_type='application/json'
    )

    assert res.status_code == 200

def test_book_should_not_add(client):
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