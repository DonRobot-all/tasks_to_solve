"""
https://leetcode.com/problems/climbing-stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In 
how many distinct ways can you climb to the top?

"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        b = 1
        for i in range(n - 1):
            a, b = b, b + a
        return b




a = Solution()
print(a.climbStairs(2))  # 2
print(a.climbStairs(3))  # 3
print(a.climbStairs(4))  # 5
print(a.climbStairs(5))  # 8

