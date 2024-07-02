"""
https://leetcode.com/problems/first-missing-positive/

Given an unsorted integer array nums. Return the 
smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) 
time and uses O(1) auxiliary space.


"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lenght = len(nums)
        temp_array = [False] * (lenght + 2)
        temp_array[0] = True
        for num in nums:
            if num > 0 and num < lenght + 1:
                temp_array[num] = True
        return temp_array.index(False)



a = Solution()
print(a.firstMissingPositive([1,2,0]))  # 3
print(a.firstMissingPositive([3,4,-1,1]))  # 2
print(a.firstMissingPositive([7,8,9,11,12]))  # 1
print(a.firstMissingPositive([1]))  # 2