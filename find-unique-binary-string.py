"""
https://leetcode.com/problems/find-unique-binary-string

Given an array of strings nums containing n unique binary 
strings each of length n, return a binary string of length
n that does not appear in nums. If there are multiple answers, 
you may return any of them.


"""

class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        integers = [int(num, 2) for num in nums]
        for i in range(0, 17):
            if i not in integers:
                ans = bin(i)[2:]
                counts = len(nums[0]) - len(ans)
                return '0' * counts + ans



a = Solution()
# print(a.findDifferentBinaryString(["01","10"]))  # 11
# print(a.findDifferentBinaryString(["00","01"]))  # 11
# print(a.findDifferentBinaryString(["111","011","001"]))  # 101
# print(a.findDifferentBinaryString(["1"]))  # "0"
print(a.findDifferentBinaryString(
    ["0000000000000000","0000000000000001","0000000000000010",
     "0000000000000011","0000000000000100","0000000000000101",
     "0000000000000110","0000000000000111","0000000000001000",
     "0000000000001001","0000000000001010","0000000000001011",
     "0000000000001100","0000000000001101","0000000000001110",
     "0000000000001111"]))  # "0000000000010000"