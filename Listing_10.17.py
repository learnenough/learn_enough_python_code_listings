def test_index(client):
    response = client.get("/")
    assert response.status_code == 200

def test_about(client):
    response = client.get("/about")
    assert response.status_code == 200

def test_palindrome(client):
    response = client.get("/palindrome")
    assert response.status_code == 200
