def test_palindrome_page(client):
    response = client.get("/palindrome")
    assert form_tag() in response.text

def form_tag():
    return '<form id="palindrome_tester" action="/check" method="post">'
