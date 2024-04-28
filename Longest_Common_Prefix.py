"""
https://leetcode.com/problems/longest-common-prefix
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings
Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.

"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        lenght_min = len(strs)
        lenght_word = min([len(i) for i in strs])
        if lenght_word == 0:
            return ""
        for idx in range(lenght_word):
            for i in range(lenght_min):
                if strs[i][idx] != strs[0][idx]:
                    return strs[0][0:idx]
        return strs[0][0:idx+1]
        

example = Solution()
assert example.longestCommonPrefix(["flower","flow","flight"]) == "fl"
assert example.longestCommonPrefix(["dog","racecar","car"]) == ""
assert example.longestCommonPrefix([""]) == ""
assert example.longestCommonPrefix(["", ""]) == ""
assert example.longestCommonPrefix(["a"]) == "a"
assert example.longestCommonPrefix(["ab", "a"]) == "a", print(example.longestCommonPrefix(["ab", "a"]))
