"""
https://leetcode.com/problems/number-of-good-pairs

Given an array of integers nums, return the 
number of good pairs.

A pair (i, j) is called good 
if nums[i] == nums[j] and i < j.


"""

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # result = 0
        # for n in set(nums):
        #     n = nums.count(n)
        #     result += n * (n - 1) // 2
        # return result
        return sum(nums.count(n) * (nums.count(n) - 1) // 2 for n in set(nums))

a = Solution()
print(a.numIdenticalPairs([1,2,3,1,1,3]))  # 4
print(a.numIdenticalPairs([1,1,1,1]))  # 6