"""
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5 
"""
def run(a,l):
	inclusive=a[0]
	exclusive=0
	for i in range(1,l):
		new_inclusive=max(inclusive,exclusive)
		inclusive=exclusive+a[i]
		exclusive=new_inclusive
	return(max(inclusive,exclusive))	

a=[5, 5, 10, 100, 10, 5]
l=len(a)
print (run(a,l))	
