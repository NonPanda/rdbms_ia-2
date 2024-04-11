import itertools

def compute_closure(attributes, fds):
    closure = set(attributes)
    changed = True
    while changed:
        changed = False
        for fd in fds:
            if fd[0].issubset(closure) and not fd[1].issubset(closure):
                closure |= fd[1]
                changed = True
    return closure

def is_superkey(attributes, fds, candidate_key):
    return compute_closure(candidate_key, fds) == set(attributes)

def find_candidate_keys(attributes, fds):
    candidate_keys = []
    for i in range(1, len(attributes) + 1):
        for subset in itertools.combinations(attributes, i):
            if is_superkey(attributes, fds, set(subset)):
                candidate_keys.append(set(subset))
    return candidate_keys

def decompose_to_bcnf(attributes, fds):
    bcnf_relations = []
    candidate_keys = find_candidate_keys(attributes, fds)
    for ck in candidate_keys:
        remaining_fds = fds.copy()
        for fd in fds:
            if fd[0].issubset(ck):
                remaining_fds.remove(fd)
        bcnf_relations.append((ck, compute_closure(ck, fds), remaining_fds))
    return bcnf_relations

attributes = ['A', 'B', 'C', 'D']
fds = [({'A'}, {'B', 'C'}), ({'B'}, {'D'})]

bcnf_relations = decompose_to_bcnf(attributes, fds)
for relation in bcnf_relations:
    
    print("Relation Number:", bcnf_relations.index(relation) + 1)
    print("Candidate Key:", relation[0])
    print("Attributes:", relation[1])
    print("Functional Dependencies:", relation[2])
    print()
