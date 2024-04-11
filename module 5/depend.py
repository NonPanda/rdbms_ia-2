from itertools import combinations

class FunctionalDependency:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def __repr__(self):
        return f"{','.join(self.lhs)} -> {','.join(self.rhs)}"


def find_closure(attributes, fds):
    closure = set(attributes)
    changed = True
    while changed:
        changed = False
        for fd in fds:
            if all(attr in closure for attr in fd.lhs) and not all(attr in closure for attr in fd.rhs):
                closure.update(fd.rhs)
                changed = True
    return closure


def find_candidate_keys(attributes, fds):
    candidate_keys = []
    all_attributes = set(attributes)
    for i in range(1, len(attributes) + 1):
        for combo in combinations(attributes, i):
            closure = find_closure(combo, fds)
            if closure == all_attributes:
                candidate_keys.append(combo)
    minimal_candidate_keys = []
    for key in candidate_keys:
        is_minimal = True
        for other_key in candidate_keys:
            if key != other_key and set(key).issubset(set(other_key)):
                is_minimal = False
                break
        if is_minimal:
            minimal_candidate_keys.append(key)
    return minimal_candidate_keys


attributes = ['A', 'B', 'C', 'D', 'E', 'F']

functional_dependencies = [
    FunctionalDependency(['A'], ['B']),
    FunctionalDependency(['B'], ['C', 'D']),
    FunctionalDependency(['D'], ['A']),
    FunctionalDependency(['C', 'E'], ['F']),
    FunctionalDependency(['F'], ['B'])
]

print("\nList of Candidate Keys is :")
candidate_keys = find_candidate_keys(attributes, functional_dependencies)
for key in candidate_keys:
    print(','.join(key))

print("\nList of Closure of Attributes is :")
for attr in attributes:
    closure = find_closure([attr], functional_dependencies)
    print(f"{attr}+ = {','.join(closure)}")
