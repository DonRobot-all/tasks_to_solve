"""
https://leetcode.com/problems/plus-one/

You are given a large integer represented as 
an integer array digits, where each digits[i] 
is the ith digit of the integer. The digits 
are ordered from most significant to least 
significant in left-to-right order. The large 
integer does not contain any leading 0's.

Increment the large integer by one and return 
the resulting array of digits.


"""

class Solution(object):
    # def plusOne(self, digits):
    #     """
    #     :type digits: List[int]
    #     :rtype: List[int]
    #     """
    #     temp = 0
    #     digits[-1] = digits[-1] + 1
    #     if digits[-1] == 10:
    #         digits[-1] = 0
    #         temp = 1
    #     for i in range(len(digits) - 2, -1, -1):
    #         digits[i] = digits[i] + temp
    #         temp = 0
    #         if digits[i] == 10:
    #             digits[i] = 0
    #             temp = 1
    #     if temp:
    #         digits.insert(0, 1)
    #     return digits

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return list(map(int, str(int(''.join(map(str, digits))) + 1)))

a = Solution()
print(a.plusOne([1,2,3]))  # [1,2,4]
print(a.plusOne([4,3,2,1]))  # [4,3,2,2]
print(a.plusOne([9]))  # [1,0]
print(a.plusOne([9,9]))  # [1,0,0]