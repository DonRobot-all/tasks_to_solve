"""
https://leetcode.com/problems/valid-palindrome-ii

Given a string s, return true if the s can be 
palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true

Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:

Input: s = "abc"
Output: false


"""

# class Solution(object):
#     def validPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         left = 0
#         right = len(s) - 1
#         a = list(s)
#         if a == a[::-1]:
#             return True
#         while left < right:
#             if a[left] != a[right]:
#                 temp = a.pop(left)
#                 if a == a[::-1]:
#                     return True
#                 a.insert(left, temp)
#                 temp = a.pop(right)
#                 if a == a[::-1]:
#                     return True
#                 return False
#             left += 1
#             right -= 1


class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] == s[right]:
                left += 1 
                right -= 1
            else:
                return s[left:right] == s[left:right][::-1] or s[left+1:right+1] == s[left+1:right+1][::-1]
        return True


obj = Solution()
print(obj.validPalindrome("abca"))
print(obj.validPalindrome("deeee"))

if __name__ == "__main__":
    a = Solution()
    print(a.isPalindrome("A man, a plan, a canal: Panama")) # true
    print(a.isPalindrome("race a car"))  # false
    print(a.isPalindrome(" "))  # true
    print(a.isPalindrome("0P"))  # false
