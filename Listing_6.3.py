states = ["Kansas", "Nebraska", "North Dakota", "South Dakota"]

def urlify(string):
    """Returns a URL-friendly version of a string.

    Example: "North Dakota" -> "north-dakota"
    """
    return "-".join(string.lower().split())

# urls: Imperative version
def imperative_urls(states):
    urls = []
    for state in states:
      urls.append(urlify(state))
    return urls

print(imperative_urls(states))

# urls: Functional version
def functional_urls(states):
    return [urlify(state) for state in states]

print(functional_urls(states))
