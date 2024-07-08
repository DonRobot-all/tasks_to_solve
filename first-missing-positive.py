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
        # lenght = len(nums)
        # temp_array = [False] * (lenght + 2)
        # temp_array[0] = True
        # for num in nums:
        #     if num > 0 and num < lenght + 1:
        #         temp_array[num] = True
        # return temp_array.index(False)
        nums = set(nums)
        nums = list(sorted(nums))
        if 1 not in nums: return 1
        left = nums.index(1)
        result = 1
        for i in range(left,len(nums)):
            if nums[i] != result:
                return result
            result += 1
        return nums[-1] + 1 


a = Solution()
print(a.firstMissingPositive([1,2,0]))  # 3
print(a.firstMissingPositive([3,4,-1,1]))  # 2
print(a.firstMissingPositive([7,8,9,11,12]))  # 1
print(a.firstMissingPositive([1]))  # 2
print(a.firstMissingPositive([2]))  # 1
print(a.firstMissingPositive([1,1000]))  # 2