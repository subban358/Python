#Write a program that, given an array A[] of n numbers and another number x, 
#determines whether or not there exist two elements in S whose sum is exactly x.
def eve(l,n,target):
    l1=set()
    for i in range(n):
        if target-l[i] in l1:
            return True
        else:
            l1.add(l[i])

if __name__ == '__main__':
    l=[1,3,7]
    target=6
    if(eve(l,len(l),target)):
        print("YES")
    else:
        print("NO")    
