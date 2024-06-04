"""
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the
subarray
with the largest sum, and return its sum.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        count = 0
        for i in nums:
            count += i
            if count < 0:
                count = 0
            result = max(result, count)
        if result == 0 and sum(nums) < 0:
            return max(nums)
        return result

a = Solution()
print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
print(a.maxSubArray([5,4,-1,7,8]))  # 23
print(a.maxSubArray([1]))  # 1
print(a.maxSubArray([-1]))  # -1
print(a.maxSubArray([-2,1]))  # 1
print(a.maxSubArray([-2,-1]))  # -1