#!/usr/bin/env python
import requests
from palindrome.phrase import Phrase

url = "https://cdn.learnenough.com/phrases.txt"
for line in requests.get(url).text.splitlines():
    if Phrase(line).ispalindrome():
        print(f"palindrome detected: {line}")
