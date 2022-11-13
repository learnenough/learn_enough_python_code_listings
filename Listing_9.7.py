#!/usr/bin/env python3
from palindrome_mhartl.phrase import Phrase


with open("phrases.txt") as file:
    palindromes = [line for line in file.readlines()
                   if Phrase(line).ispalindrome()]

palindrome_content = "".join(palindromes)
print(palindrome_content, end="")

with open("palindromes_file.txt", "w") as file:
    file.write(palindrome_content)
