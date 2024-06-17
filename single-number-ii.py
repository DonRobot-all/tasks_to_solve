"""
https://leetcode.com/problems/single-number-ii

Given an integer array nums where every 
element appears three times except for one, 
which appears exactly once. Find the single 
element and return it.

You must implement a solution with a linear 
runtime complexity and use only constant 
extra space.
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for key, value in d.items():
            if value == 1:
                return key

a = Solution()
print(a.singleNumber([2,2,3,2]))  # 3
print(a.singleNumber([0,1,0,1,0,1,99]))  # 99