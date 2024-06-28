"""
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

Given an array nums of n integers where nums[i] is in 
the range [1, n], return an array of all the integers 
in the range [1, n] that do not appear in nums.

"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = set(range(1, len(nums) + 1))
        return list(result.difference(nums))

a = Solution()
print(a.findDisappearedNumbers([4,3,2,7,8,2,3,1]))  # [5,6]
print(a.findDisappearedNumbers([1,1]))  # [2]
