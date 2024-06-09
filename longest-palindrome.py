"""
https://leetcode.com/problems/longest-palindrome

Given a string s which consists of lowercase 
or uppercase letters, return the length of the 
longest
palindrome
 that can be built with those letters.

Letters are case sensitive, for example, "Aa" 
is not considered a palindrome.

"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        temp = []
        flag = True
        for char in s:
            if char not in temp:
                count = s.count(char)
                if count % 2 != 0 and flag:
                    result += 1
                    flag = False
                result += count if count % 2 == 0 else count - 1 # (count // 2) * 2
                temp.append(char)
        return result

if __name__ == "__main__":
    a = Solution()
    print(a.longestPalindrome("abccccdd")) # 7
    print(a.longestPalindrome("a"))  # 1
    print(a.longestPalindrome("bb"))  # 2
    print(a.longestPalindrome("ccc"))  # 3
    print(a.longestPalindrome("ababababa"))  # 9
