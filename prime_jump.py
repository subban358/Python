'''
You have to move from one location in an array to another location. If suppose A is an array so if starting location is
Ai and target is Aj the the jump will be called a prime jump only if Aj=Ai*P where P is a prime number.
So we have to find the number of prime jumps possible to traverse through an array.
If no jumps possible then it will be 
Test case (3,6,12)

the ans would be (3,2,1)

as from oth location he can jump twice (3->6->12)
and so on and so forth .
'''

import math
def prime(na):
	if na>1:
		for j in range (2,na):
			if(na % j)== 0:
				break
		else:
			return True	 

def res(n):
    l=[]
    for k in range(0,len(n)):
        l.append(1)
    c=0
    for i in range(len(n)):
        p=n[i]
        for j in range(len(n)):
            f=n[j]%p 
            if(f==0):
                b=n[j]/p 
                if prime(math.ceil(b)):
                    l[c]+=1
                    p=n[j]
        c+=1            
            
    return l        
list1=[3,6,12]
print(res(list1))
