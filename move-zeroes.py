"""
https://leetcode.com/problems/move-zeroes

Given an integer array nums, move all 0's to 
the end of it while maintaining the relative 
order of the non-zero elements.

Note that you must do this in-place without 
making a copy of the array.
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Simple
        # for i in nums:
        #     if i == 0:
        #         nums.remove(i)
        #         nums.append(i)
        
        # Better
        left = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[left] = nums[i]
                left += 1
        for i in range(left, len(nums)):
            nums[i] = 0
        print(nums)

a = Solution()
print(a.moveZeroes([0,1,0,3,12]))  # [1,3,12,0,0]
print(a.moveZeroes([0]))  # [0]
