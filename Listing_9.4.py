#!/usr/bin/env python
from palindrome.phrase import Phrase

with open("phrases.txt") as file:
    for line in file.readlines():    # Pythonic
        if Phrase(line).ispalindrome():
            print(f"palindrome detected: {line}")
