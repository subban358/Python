""" 
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

def run(a,p):
	a.sort()
	for i in range (1,p-1):
		if(a[i+1]!=a[i]+1):
			s=a[i]+1
			break
		else:
			s=a[p-1]+1
	return s			

a=[3,4,-1,1]
p=len(a)
print (run(a,p))

