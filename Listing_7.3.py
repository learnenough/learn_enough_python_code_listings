class Phrase:
    """A class to represent phrases."""

    def __init__(self, content):
        self.content = content

if __name__ == "__main__":
    phrase = Phrase("Madam, I'm Adam.")
    print(phrase.content)

    phrase.content = "Able was I, ere I saw Elba."
    print(phrase.content)
