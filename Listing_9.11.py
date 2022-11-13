#!/usr/bin/env python3
import requests

from palindrome_mhartl.phrase import Phrase

URL = "https://cdn.learnenough.com/phrases.txt"


for line in requests.get(URL).content.decode("utf-8").splitlines():
    if Phrase(line).ispalindrome():
        print(f"palindrome detected: {line}")
