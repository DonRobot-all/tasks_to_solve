"""
https://leetcode.com/problems/valid-palindrome

A phrase is a palindrome if, after converting all 
uppercase letters into lowercase letters and 
removing all non-alphanumeric characters, it reads
the same forward and backward. Alphanumeric characters
include letters and numbers.

Given a string s, return true if it is a palindrome, 
or false otherwise.

"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = ''
        new_s += ''.join(i.lower() for i in s if i.isalpha() or i.isdigit())
        return new_s == new_s[::-1]


if __name__ == "__main__":
    a = Solution()
    print(a.isPalindrome("A man, a plan, a canal: Panama")) # true
    print(a.isPalindrome("race a car"))  # false
    print(a.isPalindrome(" "))  # true
    print(a.isPalindrome("0P"))  # false
