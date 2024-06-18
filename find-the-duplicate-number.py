"""
https://leetcode.com/problems/find-the-duplicate-number

Given an array of integers nums containing n + 1 
integers where each integer is in the range [1, n] 
inclusive.

There is only one repeated number in nums, 
return this repeated number.

You must solve the problem without modifying the array
 nums and uses only constant extra space.
"""

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # d = {}
        # for num in nums:
        #     if num in d:
        #         return num
        #     d[num] = 1

        tortoise = nums[0]
        hare = nums[0]
        
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break    
        return tortoise

a = Solution()
print(a.findDuplicate([1,3,4,2,2]))  # 2
print(a.findDuplicate([3,1,3,4,2]))  # 3
print(a.findDuplicate([3,3,3,3,3]))  # 3