#!/usr/bin/env python3
from palindrome_mhartl.phrase import Phrase


with open("phrases.txt") as file:
    for line in file.readlines():    # Pythonic
        if Phrase(line).ispalindrome():
            print(f"palindrome detected: {line}")
