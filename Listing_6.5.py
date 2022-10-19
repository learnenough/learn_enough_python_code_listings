states = ["Kansas", "Nebraska", "North Dakota", "South Dakota"]
.
.
.
# singles: Imperative version
def imperative_singles(states):
    singles = []
    for state in states:
        if len(state.split()) == 1:
            singles.append(state)
    return singles

print(imperative_singles(states))

# singles: Functional version
def functional_singles(states):
    return [state for state in states if len(state.split()) == 1]

print(functional_singles(states))
