"""
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices 
of the two numbers 
such that they add up to target.
You may assume that each input would have exactly one solution, and
 you may not use the 
same element twice.
You can return the answer in any order.
[2,7,11,15] -> 9
Constraints:
    2 <= nums.length <= 10 ** 4
    -109 <= nums[i] <= 10 ** 9
    -109 <= target <= 10 ** 9
Follow-up: Can you come up with an algorithm that is less than O(n2) 
    time complexity?

[2,11,15,3,7,9,1,0,2,13,7,86,34,23]   target = 9

"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for index1, num1 in enumerate(nums):
        #     for index2 in range(len(nums) - 1):
        #         if num1 + nums[index2] == target:
        #             result = [index2, index1]
        #             break
        # return result
        d = {}
        for idx, num in enumerate(nums):
            result = target - num
            if result in d:
                return [d[result], idx]
            d[num] = idx

a = Solution()
print(a.twoSum([3,2,4], 6))

