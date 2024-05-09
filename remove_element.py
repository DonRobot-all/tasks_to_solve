"""
https://leetcode.com/problems/remove-element/

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
 The order of the elements may be changed. Then return the number of elements in nums which are 
 not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you 
need to do the following things:

    Change the array nums such that the first k elements of nums contain the elements which 
    are not equal to val. The remaining elements of nums are not important as well as the 
    size of nums.
    Return k.

"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums[:] = [i for i in nums if i != val]
        return len(nums)


a = Solution()
print(a.removeElement([3,2,2,3], 3))  # 2
print(a.removeElement([0,1,2,2,3,0,4,2], 2))  # 5
