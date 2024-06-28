"""
https://leetcode.com/problems/jewels-and-stones

You're given strings jewels representing the types 
of stones that are jewels, and stones representing 
the stones you have. Each character in stones is a 
type of stone you have. You want to know how many 
of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a 
different type of stone from "A".


"""

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        result = 0
        for char in stones:
            if char in jewels:
                result += 1
        return result



a = Solution()
print(a.numJewelsInStones("aA","aAAbbbb"))  # 3
print(a.numJewelsInStones("z", "ZZ"))  # 0