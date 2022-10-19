states = ["Kansas", "Nebraska", "North Dakota", "South Dakota"]

# urls: Imperative version
def imperative_urls(states):
    urls = []
    for state in states:
      urls.append("-".join(state.lower().split()))
    return urls

print(imperative_urls(states))
