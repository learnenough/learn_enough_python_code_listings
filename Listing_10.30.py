def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    base_title = "Learn Enough Python Sample App"
    title = f"<title>{base_title} | Home</title>"
    assert title in response.text
    assert "<h1>" in response.text

def test_about(client):
    response = client.get("/about")
    assert response.status_code == 200
    base_title = "Learn Enough Python Sample App"
    title = f"<title>{base_title} | About</title>"
    assert title in response.text
    assert "<h1>" in response.text

def test_palindrome(client):
    response = client.get("/palindrome")
    assert response.status_code == 200
    base_title = "Learn Enough Python Sample App"
    title = f"<title>{base_title} | Palindrome Detector</title>"
    assert title in response.text
    assert "<h1>" in response.text
