def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert full_title("Home") in response.text
    assert "<h1>" in response.text
    assert "<nav>" in response.text

def test_about(client):
    response = client.get("/about")
    assert response.status_code == 200
    assert full_title("About") in response.text
    assert "<h1>" in response.text

def test_palindrome(client):
    response = client.get("/palindrome")
    assert response.status_code == 200
    assert full_title("Palindrome Detector") in response.text
    assert "<h1>" in response.text

def full_title(variable_title):
    """Return the full title."""
    base_title = "Learn Enough Python Sample App"
    return f"<title>{base_title} | {variable_title}</title>"
