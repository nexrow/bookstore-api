import json

def books_json(id,title,author,genre,seller):
    return json.dumps(
        {
            "id": id,
            "title": title,
            "author": author,
            "genre": genre,
            "seller": seller,
        }
    )

def test_book_should_add(client):
    res = client.post(
        '/api/books',
        data = books_json("1", "Harry Ptter", "J.K. Rowling", "Adventorious","Bezos"),
        content_type='application/json'
    )

    assert res.status_code == 200

def test_book_should_not_add(client):    
    
    res = client.post(
        '/api/books',
        data = books_json("321", "Book123", "J.K. Rowling4132", "Comedy/Horror","You"),
        content_type = 'application/json'
    )

    assert res.status_code == 400

    res = client.post(
        '/api/books',
        data = books_json("22", "WorstBook", "You421", "Comedy","Me413"),
        content_type = 'application/json'
    )

    assert res.status_code == 400

    res = client.post(
        '/api/books',
        data = books_json("411", "", "", "",""),
        content_type = 'application/json'
    )

    assert res.status_code == 400
