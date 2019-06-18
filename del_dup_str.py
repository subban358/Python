"""
Delete the the duplicate elements from a list
"""
s="abaacbd"
lis=list(s)
lis=list(dict.fromkeys(lis))
for i in lis:
	print(i,end='')
