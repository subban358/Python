'''
finding the longest increasing subsequence
like in this example [3 10 40 80]
so we have to write a function which returns the length of max length of longest increasing subsequence which is=4 here !! 
'''

def lis(a,b):
	for i in range(1,len(a)):
		for j in range(0,i):
			if(a[i]>=a[j]):
				b[i]= max(b[i],b[j]+1)
	return max(b)			

a=[50, 3, 10, 7, 40, 80] #subsequence=[3 10 40 80]=>> length=4
b=[1]*len(a) #making a list initializing all values by 1
print("The length of longest increasing subsequence is:"+str(lis(a,b)))	
