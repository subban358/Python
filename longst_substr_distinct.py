'''
Given a string, print the longest substring without repeating characters. 
For example, the longest substrings without repeating characters for “ABDEFGABEF” are “BDEFGA” and “DEFGAB”, with length 6. 
For “BBBB” the longest substring is “B”, with length 1. 
The desired time complexity is O(n) where n is the length of the string.
'''
def func(string):
    l=list(string)
    j=0
    b=[]
    c=[]
    while(j<len(l)):
        i=j+1
        while(i<len(l)):
            if l[i] in l[j:i]:
                b.append(l[j:i])
                break
            else:
                i+=1
        j+=1        
    for i in b:
        c.append(len(i))
    mx=max(c)
    print("".join(b[c.index(mx)]))
    print(len(b[c.index(mx)]))
    
if __name__ == '__main__':
    ip="bbb"
    func(ip)    
