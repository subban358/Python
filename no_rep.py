'''
Given an input stream of N characters consisting only of lower case alphabets. The task is to find the first non repeating character, each time a character is inserted to the stream. If no non repeating element is found print -1.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains an integer N denoting the size of the stream. Then in the next line are x characters which are inserted to the stream.

Output:
For each test case in a new line print the first non repeating elements separated by spaces present in the stream at every instinct when a character is added to the stream, if no such element is present print -1.

Constraints:
1 <= T <= 200
1 <= N <= 500

Example:
Input:
2
4
a a b c
3
a a c

Output:
a -1 b b
a -1 c

'''

def res(str):
    n = len(str)
    j=0
    keys=[]
    num=[]
    res = []
    while j<=n:
        keys=[]
        num=[]
        for i in range(0,j):
            keys.append(str[i])
        for i in range (len(keys)):
            num.append(keys.count(str[i]))      
        j+=1 
        if num.count(1) is 0:
            res.append('-1')
        for i in range(len(num)):
            if num[i] is 1:
                res.append(keys[i])
                break
    res.remove(res[0])   
    e=""
    r=e.join(res)
    return r

if __name__ == '__main__':
    ans=[]
    test = int(input())
    for i in range(test):
        n = int(input())
        str =input()
        ans.append(res(str))
    for i in ans:
        print(i,end="\n")
        
