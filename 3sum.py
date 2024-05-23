"""
https://leetcode.com/problems/3sum/

Given an integer array nums, return all 
the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and 
[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain 
duplicate triplets.

"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        




a = Solution()
print(a.threeSum([-1,0,1,2,-1,-4]))  # [[-1,-1,2],[-1,0,1]]
print(a.threeSum([0,1,1]))  # []
print(a.threeSum([0,0,0]))  # [[0,0,0]]
