import json

def user_register_json(username, password, name, email):
    return json.dumps(
        {
            "username": username,
            "password": password,
            "name": name,
            "email": email
        }
    )

def test_user_register_should_create_user(client):
    res = client.post(
        '/api/users/register',
        data=user_register_json("user", "1234", "A user", "user@email.com"),
        content_type='application/json'
    )

    assert res.status_code == 200

def test_user_register_should_not_create_user(client):
    res = client.post(
        '/api/users/register',
        data=user_register_json("user1", "12345", "A user1", "user1@email.com"),
        content_type='application/json'
    )

    assert res.status_code == 200

    res = client.post(
        '/api/users/register',
        data=user_register_json("user1", "12345", "A user1", "user1@email.com"),
        content_type='application/json'
    )

    assert res.status_code == 400
