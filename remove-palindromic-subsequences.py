"""
https://leetcode.com/problems/remove-palindromic-subsequences

You are given a string s consisting only of 
letters 'a' and 'b'. In a single step you can 
remove one palindromic subsequence from s.

Return the minimum number of steps to make the
 given string empty.

A string is a subsequence of a given string if 
it is generated by deleting some characters of a 
given string without changing its order. Note that 
a subsequence does not necessarily need to be contiguous.

A string is called palindrome if is one that reads 
the same backward as well as forward.

"""

class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        return 1 if s == s[::-1] else 2

if __name__ == "__main__":
    a = Solution()
    print(a.removePalindromeSub("ababa")) # 1
    print(a.removePalindromeSub("abb"))  # 2
    print(a.removePalindromeSub("baabb"))  # 2
