#!/usr/bin/env python
import sys
import requests
from bs4 import BeautifulSoup

# Return the paragraphs from a Wikipedia link, stripped of reference numbers.
# Especially useful for text-to-speech (both native and foreign).

# Get URL from the command line.
url = sys.argv[1]
# Create Beautiful Soup document from live URL.
doc = BeautifulSoup(requests.get(url).text)
# Remove references.
for reference in doc("sup", class_="reference"):
    reference.decompose()
# Print paragraphs.
for paragraph_tag in doc("p"):
    print(paragraph_tag.text)
