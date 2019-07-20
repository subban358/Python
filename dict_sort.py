'''
There is a Player class which has fields: name String and Score an integer . Given an array of Player
objects that sorts them in order of decreasing score; I f players have the same score, sort those players
alphabetically by name. players can have the same name. Playe r names consi st of lowercase English
letters. Playe r object has been given by user

Sample Input:

5
amy 100
david 100
heraldo 50
aakansha 75
aleksa 150

Sample Output:

aleksa 150
amy 100
david 100
aakansha 75
heraldo 50

'''
l=[]
l1=[]
size=int(input())
for i in range(size):
    ele=input().split()
    l.append(ele)
    
d={}
for i in l:
    for k in i:
        l1.append(k)
for k in range (0,len(l1)-1,2):
    d[l1[k]] = int(l1[k+1])
l=list(d.keys())
l1=list(d.values())
l2=[]
l2=l1.copy()
l2.sort()
l2.reverse()
'''print(l)
print(l1)
print(l2)'''
print()
for i in range(len(l)):
    print(l[l1.index(l2[i])],l2[i])
