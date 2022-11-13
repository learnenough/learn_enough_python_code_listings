class Phrase:
    """A class to represent phrases."""

    def __init__(self, content):
        self.content = content

    def ispalindrome(self):
        """Return True for a palindrome, False otherwise."""
        return self.processed_content() == reverse(self.processed_content())

    def processed_content(self):
        """Return content for palindrome testing."""
        return self.content.lower()

    def letters(self):
        """Return the letters in the content."""
        pass

def reverse(string):
    """Reverse a string."""
    return "".join(reversed(string))
