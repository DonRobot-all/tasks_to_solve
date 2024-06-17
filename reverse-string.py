"""
https://leetcode.com/problems/reverse-string

Write a function that reverses a string. 
The input string is given as an array of 
characters s.

You must do this by modifying the input 
array in-place with O(1) extra memory.
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # for i in range(len(s)//2):
        #     s[i], s[~i] = s[~i], s[i]
        # print(s)
        right = len(s) - 1
        for left in range(len(s)//2):
            s[left], s[right] = s[right], s[left]
            right -= 1
        print(s)   

a = Solution()
print(a.reverseString(["h","e","l","l","o"]))  # ["o","l","l","e","h"]
print(a.reverseString(["H","a","n","n","a","h"]))  # ["h","a","n","n","a","H"]