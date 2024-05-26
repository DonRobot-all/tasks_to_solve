"""
https://leetcode.com/problems/longest-substring-without-repeating-characters

Given a string s, find the length of the longest
substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}
        left = 0
        lenght = 0
        for right in range(len(s)):
            if s[right] in seen and seen[s[right]] >= left:
                left = seen[s[right]] + 1
            else:
                lenght = max(lenght, right - left + 1)
            seen[s[right]] = right

        return lenght

a = Solution()
print(a.lengthOfLongestSubstring("abcabcbb"))  # 3
print(a.lengthOfLongestSubstring("bbbbb"))  # 1
print(a.lengthOfLongestSubstring("pwwkew"))  # 3
print(a.lengthOfLongestSubstring(" "))  # 1
print(a.lengthOfLongestSubstring("au"))  # 2
print(a.lengthOfLongestSubstring("dvdf"))  # 3