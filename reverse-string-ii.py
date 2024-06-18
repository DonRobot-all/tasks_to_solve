"""
https://leetcode.com/problems/reverse-string

Given a string s and an integer k, reverse 
the first k characters for every 2k characters 
counting from the start of the string.

If there are fewer than k characters left, 
reverse all of them. If there are less than 
2k but greater than or equal to k characters, 
then reverse the first k characters and leave 
the other as original.
"""

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # a = list(s)
        # revers = True
        # for i in range(0, len(a), k):
        #     if revers:
        #         a[i:i+k] = a[i:i+k][::-1]
        #     revers = not revers
        # return ''.join(a)
        for i in range(0,len(s),2*k):
            if(i+k<len(s)):
                s=s[0:i]+s[i:i+k][::-1]+s[i+k:]
            else:
                s=s[0:i]+s[i:i+k][::-1]
        return s

a = Solution()
print(a.reverseStr("abcdefg", 2))  # "bacdfeg"
print(a.reverseStr("abcd", 2))  # "bacd"
print(a.reverseStr("abcdef", 3))  # "cbadef"