#!/usr/bin/env python3
from palindrome_mhartl.phrase import Phrase


with open("phrases.txt") as file:
    text = file.read()
    for line in text.splitlines():    # Arguably not Pythonic
        if Phrase(line).ispalindrome():
            print(f"palindrome detected: {line}")
