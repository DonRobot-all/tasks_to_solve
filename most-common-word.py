"""
https://leetcode.com/problems/most-common-word

Given a string paragraph and a string array of 
the banned words banned, return the most frequent 
word that is not banned. It is guaranteed there 
is at least one word that is not banned, and that 
the answer is unique.

The words in paragraph are case-insensitive and 
the answer should be returned in lowercase.


"""

class Solution(object):
    def key(self, d):
        return d[1]

    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        s = ''
        for char in paragraph:
            if char.isalpha() or char == ' ':
                s += char.lower()
            else:
                s += ' '
        d = {}
        for word in s.split():
            if word not in banned:
                if word in d:
                    d[word] += 1
                else:
                    d[word] = 1
        word = ''
        length = 0
        for w, l in d.items():
            if l > length:
                length = l
                word = w
        return word

a = Solution()
# print(a.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))  # "ball"
# print(a.mostCommonWord("a.", []))  # a
print(a.mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))  # "b"