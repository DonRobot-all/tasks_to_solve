"""
https://leetcode.com/problems/maximum-product-of-three-numbers/

Given an integer array nums, find three numbers whose product 
is maximum and return the maximum product.

"""

class Solution:
    def maximumProduct(self, nums) -> int:
        nums.sort()
        if nums[0] * nums[1] * nums[-1] > nums[-2] * nums[-3] * nums[-1]:
            return nums[0] * nums[1] * nums[-1]
        return nums[-1] * nums[-2] * nums[-3]



a = Solution()
print(a.maximumProduct([1,2,3]))  # 6
print(a.maximumProduct([1,2,3,4]))  # 24
print(a.maximumProduct([-1,-2,-3]))  # -6
print(a.maximumProduct([-100,-98,-1,2,3,4]))  # 39200
print(a.maximumProduct([-8,-7,-2,10,20]))  # 1120
print(a.maximumProduct([-1,-2,-3,-4]))  # -12

