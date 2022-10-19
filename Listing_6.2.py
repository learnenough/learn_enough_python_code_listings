states = ["Kansas", "Nebraska", "North Dakota", "South Dakota"]

# urls: Imperative version
def imperative_urls(states):
    urls = []
    for state in states:
      urls.append("-".join(state.lower().split()))
    return urls

print(imperative_urls(states))

# urls: Functional version
def functional_urls(states):
    return ["-".join(state.lower().split()) for state in states]

print(functional_urls(states))
