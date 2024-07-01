"""
https://leetcode.com/problems/richest-customer-wealth/

You are given an m x n integer grid accounts where 
[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has 
in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest 
customer has.

A customer's wealth is the amount of money they have 
in all their bank accounts. The richest customer is 
the customer that has the maximum wealth.


"""

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        # return max(sum(money) for money in accounts)
        return max(map(sum, accounts))

a = Solution()
print(a.maximumWealth([[1,2,3],[3,2,1]]))  # 6
print(a.maximumWealth([[1,5],[7,3],[3,5]]))  # 10
print(a.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))  # 17