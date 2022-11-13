#!/usr/bin/env python3
import sys

import requests
from bs4 import BeautifulSoup


# Return the paragraphs from a Wikipedia link, stripped of reference numbers.
# Especially useful for text-to-speech (both native and foreign).

# Get URL from the command line.
url = sys.argv[1]
# Create Beautiful Soup document from live URL.
content = requests.get(url).content.decode("utf-8")
doc = BeautifulSoup(content, features="html.parser")
# Remove references.
for reference in doc("sup", class_="reference"):
    reference.decompose()
