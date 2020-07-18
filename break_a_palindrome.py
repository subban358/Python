"""
In this problem we had to break a palindromic string which means if a given string is a palindrome we have to make it a non palindrome such a way that it is also lexicographically 
smallest possible. so let's say for example the palindrome string is given as "abba" so to make it non palindrome we can just change any character from a or b to anything apart from
a , b but to make it lexicographically smallest the choice is to make first non 'a' character to 'a' so the answer in this case is "aaba" which indeed is non palindrome
and also smallest possible. Now there may come a case like for odd length string where middle element is non 'a' for example: "aacaa". Here if we follow the previous logic and replace 'c' 
with 'a' it still remains a palindrome. so for that case we have to skip middile element and after middle if no non 'a' elements are found like let's say for "aaa" here no non 'a'
is present so we have to make the last character as 'b' because 'b' comes just after 'a' in lexicographical ordering. So hence by doing so we maintain both our requirements.

Time Complexity: O(N) [cause we are just doing a linear pass with some constant time if checks]
Space Complexity: O(1) [just because strings are immutable in python we have used a list but for c++ and java(StringBuilder) it is constant space]

video explanation: https://www.youtube.com/watch?v=6_VKCJRKD1Y
"""


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        l = list(palindrome)
        for i in range(n):
            j = n-i-1
            if i == j:
                continue 
            if l[i] != 'a':
                l[i] = 'a'
                return "".join(l)
            
        l[n-1] = 'b'
        return "".join(l)
    
