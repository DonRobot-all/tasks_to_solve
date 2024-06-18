"""
https://leetcode.com/problems/faulty-keyboard/

Your laptop keyboard is faulty, and whenever 
you type a character 'i' on it, it reverses 
the string that you have written. Typing other
characters works as expected.

You are given a 0-indexed string s, and you 
type each character of s using your faulty keyboard.

Return the final string that will be present 
on your laptop screen.
"""

class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        for i in s:
            if i == 'i' or i == 'I':
                result = result[::-1]
            else:
                result += i
        return result
        


a = Solution()
print(a.finalString("string"))  # "rtsng"
print(a.finalString("poiinter"))  # "ponter"