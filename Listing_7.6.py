class Phrase:
    """A class to represent phrases."""

    def __init__(self, content):
        self.content = content

    def ispalindrome(self):
        """Return True for a palindrome, False otherwise."""
        processed_content = self.content.lower()
        return processed_content == reverse(processed_content)

    def louder(self):
      """Make the phrase LOUDER."""
      # FILL IN

def reverse(string):
    """Reverse a string."""
    return "".join(reversed(string))
