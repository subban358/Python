"""
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5 
"""
def run(a,l):
	s=0
	s1=0
	s2=0
	print(a)
	if( a[0]>max(a[1:l-1]) or a[l-1]>max(a[1:l-1]) ): 
		s=a[0]+a[l-1]
	else:

		for i in range (0,l):
			if(i%2==0):
				s1=s1+a[i]
			else:
				s2=s2+a[i]	
		s=max(s1,s2)
	return s

a=[2, 4, 6, 2, 5]
l=len(a)
print (run(a,l))	
