'''
1. Generate all prime numbers between a range in a list
2. Make all possible combinations taking the first mentioned list and store it in another list
3. Now from 2nd list find all prime numbers and store in another list
4. From 3rd list find the maximum and minimum element
5. The min element will be first and max element will be the 2nd element of the fibonacci series
6. Find the length of the 3rd list suppose n and generate the nth fibonnacci number as output where 1st and and 2nd elemnts 
will be min and max respectively.

'''


import itertools as it
lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))  

def convert(list):  
    res = int("".join(map(str, list)))    
    return res   
def is_prime(na):
	if na>1:
		for j in range (2,na):
			if(na % j)== 0:
				break
		else:
			return True	    

def fibonacci(length,minimum,maximum): 
	a = minimum
	b = maximum
	if length < 0: 
		print("Incorrect input") 
	elif length == 0: 
		return a 
	elif length == 1: 
		return b 
	else: 
		for i in range(2,length): 
			c = a + b 
			a = b 
			b = c 
		return b 


l1=[]  
for num in range(lower,upper + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           l1.append(num)
l2=[]
l2=list(it.permutations(l1,2)) 
l3=[]
l3=[list(i) for i in  l2]   
l4=[]
k=0
while(k<len(l3)):
  m=convert(l3[k])
  l4.append(m)
  k+=1    
print(l4)
print() 
l5=[]
for k in range(len(l4)):
	if  is_prime(l4[k]):
		l5.append(l4[k])		

maximum=max(l5)
minimum=min(l5)
length=len(l5)
print()
print()
print(l5)
print()
print(length)
print()
print(fibonacci(length,minimum,maximum))

