"""
https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n. 
There are n vertical lines drawn such that the two 
endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a
 container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0
        for i in range(len(height)):
            for a in range(i + 1, len(height)):
                temp = min(height[i], height[a]) * (a - i)
                result = max(result, temp)
        return result

a = Solution()
print(a.maxArea([2,6,1,5,4]))  # 49
print(a.maxArea([1,8,6,2,5,4,8,3,7]))  # 49
print(a.maxArea([1,1]))  # 1
