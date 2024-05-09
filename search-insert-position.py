"""
https://leetcode.com/problems/search-insert-position/

Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the 
index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.


"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle  
            elif nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
        if nums[middle] > target:
            return middle
        return middle + 1



a = Solution()
print(a.searchInsert([1,3,5,6], 5))
print(a.searchInsert([1,3,5,6], 2))
print(a.searchInsert([1,3,5,6], 7))

