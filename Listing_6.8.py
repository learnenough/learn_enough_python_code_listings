.
.
.
# lengths: Imperative version
def imperative_lengths(states):
    lengths = {}
    for state in states:
        lengths[state] = len(state)
    return lengths

print(imperative_lengths(states))

def functional_lengths(states):
    return {state: len(state) for state in states}

print(functional_lengths(states))
