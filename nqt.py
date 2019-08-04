'''
Let a person starting his journey from co-ordinate (0,0)
he always follows a certain trajectory like first Righr->Upwords->Left->Downwords.
So with each move the distance he traves is increased by 10 like first moves 10 in right
then 20 up 30 left and 40 down 50 again right and so on.
so for a given input in number of steps find his co-ordinate.

sample:

input=3
output= (-20,20)
'''

ip=int(input())
l1=[]
a=10
x=0
y=0
c=0
c1=0
i=0
while(i<ip):
    if c%2==0:
        l1.append(a)
        a+=10
        c1+=1
    else:
        l1.append(0-a)
        a+=10
        c1+=1
    if c1==2:
        c+=1
        c1=0
    i+=1
for i in range(len(l1)):
    if i%2==0:
        x+=l1[i]
    else:
        y+=l1[i]
print(x,y)
