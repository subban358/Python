def fun(lis):
    d = dict()
    l2 = []
    for i in range(len(l)):
        d[l[i]] = l.count(l[i])
    v = list(d.values())
    k = list(d.keys())
    l2.append(k[v.index(1)])
    v.pop(v.index(1))
    k.pop(v.index(1))
    l2.append(k[v.index(1)])
    '''print(d)
    print(k)
    print(v)'''
    print(l2)
    
l=[3,2]    
fun(l)
