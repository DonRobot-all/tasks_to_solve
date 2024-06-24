"""
https://leetcode.com/problems/sort-vowels-in-a-string

Given a 0-indexed string s, permute s to get a new string t such that:

    All consonants remain in their original places. More formally, 
    if there is an index i with 0 <= i < s.length such that s[i] 
    is a consonant, then t[i] = s[i].
    The vowels must be sorted in the nondecreasing order of their 
    ASCII values. More formally, for pairs of indices i, j with 
    0 <= i < j < s.length such that s[i] and s[j] are vowels, 
    then t[i] must not have a higher ASCII value than t[j].

Return the resulting string.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear
 in lowercase or uppercase. Consonants comprise all letters 
 that are not vowels.
"""

class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels=sorted([c for c in s if c.lower() in "aeiou"],reverse=True)
        res=[]

        for char in s:
            if char.lower() in "aeiou":
                res.append(vowels.pop())
            else:
                res.append(char)

        return "".join(res)
        # vowels = []
        # result = [None] * len(s)
        # example = ['a', 'y', 'o', 'e', 'i', 'u']
        # for i in range(len(s)):
        #     if s[i].lower() not in example:
        #         result[i] = s[i]
        #     else:
        #         vowels.append(s[i])
        # vowels = sorted(vowels)
        # left = 0
        # for i in range(len(result)):
        #     if result[i] == None:
        #         result[i] = vowels[left]
        #         left += 1
        # return ''.join(result)
            

a = Solution()
print(a.sortVowels("lEetcOde"))  # "lEOtcede"
print(a.sortVowels("lYmpH"))  # "lYmpH"