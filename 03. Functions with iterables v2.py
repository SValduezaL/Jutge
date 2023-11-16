def count_unique(L):
    unique = []
    for item in L:
        if item not in unique:
            unique.append(item)
    return len(unique)

def remove_duplicates(L):
    sol = []
    for item in L:
        if item not in sol:
            sol.append(item)
    return sol

def flatten(L):
    L_flatten = []
    for item in L:
        L_flatten += item
    return L_flatten

def flatten_rec(L):
    L_flatten_rec = []
    for i in range(len(L)):
        if isinstance(L[i], list):
            L_flatten_rec += flatten_rec(L[i])
        else:
            L_flatten_rec.append(L[i])
    return L_flatten_rec