def ispalindrome(string):
    """Return True for a palindrome, False otherwise."""
    return string.lower() == string.lower()[::-1]
