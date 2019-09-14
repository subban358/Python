def func(l):
    d = dict()
    for i in range(len(l)):
        d[l[i]] = l.count(l[i])
    l1 = list(d.values())
    l2 = list(d.keys())
    l3 = []
    l4 = []
    l4 = l1.copy()
    l1.sort()
    l1.reverse()
    for i in range(len(l1)):
        for j in range(l1[i]):
            l3.append(l2[l4.index(l1[i])])
    return l3        
l = [1,2,2,2,3,3]
print(func(l))
