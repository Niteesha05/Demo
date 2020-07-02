l=[('h',1),('e',2),('l',3),('l',4),('o',5)]
d={}
for a,b in l:
    d.setdefault(a,[]).append(b)
print(d)
