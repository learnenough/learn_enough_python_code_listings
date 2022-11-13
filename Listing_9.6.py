#!/usr/bin/env python3
from palindrome_mhartl.phrase import Phrase


with open("phrases.txt") as file:
    lines = file.readlines()
    for line in lines:
        if Phrase(line).ispalindrome():
            print(f"palindrome detected: {line.strip()}")

palindromes = [line for line in lines if Phrase(line).ispalindrome()]
with open("palindromes_file.txt", "w") as file:
    file.write("".join(palindromes))
