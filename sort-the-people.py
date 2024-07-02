"""
https://leetcode.com/problems/sort-the-people/

You are given an array of strings names, 
and an array heights that consists of distinct 
positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote 
the name and height of the ith person.

Return names sorted in descending order by the 
people's heights.


"""

class Solution(object):
    def key(self, s):
        return -s[1]

    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        data = zip(names, heights)
        data = sorted(list(data), key=self.key)
        names, heights = zip(*data)
        return list(names)


a = Solution()
print(a.sortPeople(["Mary","John","Emma"], [180,165,170]))  # ["Mary","Emma","John"]
print(a.sortPeople(["Alice","Bob","Bob"], [155,185,150]))  # ["Bob","Alice","Bob"]  