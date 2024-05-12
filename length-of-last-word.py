"""
https://leetcode.com/problems/length-of-last-word/

Given a string s consisting of words and spaces, 
return the length of the last word in the string.

A word is a maximal
substring
consisting of non-space characters only.


"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split()[-1])


a = Solution()
print(a.lengthOfLastWord("Hello World"))  # 5
print(a.lengthOfLastWord('   fly me   to   the moon  '))  # 4
print(a.lengthOfLastWord('luffy is still joyboy'))  # 6