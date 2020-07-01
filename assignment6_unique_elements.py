def unique_list(l):
    x=[]
    for a in l:
        if a not in x:
            x.append(a)
    return x
print(unique_list([1,5,6,3,3,6,6,8]))
