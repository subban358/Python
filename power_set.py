'''
Generate the power set of set[1,2,3]
the ans would be [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]

'''

def subsets(nums):
  no_of_subs=2**len(nums)
  result=[]
  for i in range(no_of_subs):
    subset=[]
    for j in nums:
      if i%2==1:
        subset.append(j)
      i//=2
    result.append(subset)
  return result  
def convert(list): 
  res = sum(d * 10**i for i, d in enumerate(list[::-1])) 
  return(res)      
list1=[1,2,3,4]
l1=[]
l1=subsets(list1)
l2=[]
k=0
while(k<len(l1)):
  m=convert(l1[k])
  l2.append(m)
  k+=1
l2.sort() 
print(l2)