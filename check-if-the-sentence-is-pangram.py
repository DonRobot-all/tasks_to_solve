"""
https://leetcode.com/problems/check-if-the-sentence-is-pangram

A pangram is a sentence where every letter of the English 
alphabet appears at least once.

Given a string sentence containing only lowercase English 
letters, return true if sentence is a pangram, or false otherwise.


"""

class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        example = set(chr(i) for i in range(97, 123))
        return not bool(example.difference(sentence))
        # return len(set(sentence)) == 26



a = Solution()
print(a.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))  # True
print(a.checkIfPangram("leetcode"))  # False