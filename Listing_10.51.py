def test_palindrome_page(client):
    response = client.get("/palindrome")
    assert form_tag() in response.text

def test_non_palindrome_submission(client):
    phrase = "Not a palindrome."
    response = client.post("/check", data={"phrase": phrase})
    assert f'<p>"{phrase}" isn\'t a palindrome.</p>' in response.text

def test_palindrome_submission(client):
    phrase = "Sator Arepo tenet opera rotas"
    response = client.post("/check", data={"phrase": phrase})
    assert f'<p>"{phrase}" is a palindrome!</p>' in response.text

def form_tag():
    return '<form id="palindrome_tester" action="/check" method="post">'
