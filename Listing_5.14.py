def reverse(string):
    """Reverse a string."""
    return "".join(reversed(string))

def ispalindrome(string):
    """Return True for a palindrome, False otherwise."""
    return string.lower() == reverse(string.lower())
