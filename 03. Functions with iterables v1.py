def count_unique(L):
    L.sort()
    count = 1
    for i in range(len(L)-1):
        if L[i] != L[i+1]:
            count += 1
    return count

def remove_duplicates(L):
    L.sort()
    for item in L:
        while L.count(item) > 1:
            L.remove(item)
    return L

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