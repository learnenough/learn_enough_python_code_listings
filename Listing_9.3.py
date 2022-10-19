#!/usr/bin/env python
from palindrome.phrase import Phrase

with open("phrases.txt") as file:
    text = file.read()
    for line in text.splitlines():    # Arguably not Pythonic
        if Phrase(line).ispalindrome():
            print(f"palindrome detected: {line}")
