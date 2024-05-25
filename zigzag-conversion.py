"""
https://leetcode.com/problems/zigzag-conversion/

The string "PAYPALISHIRING" is written in a zigzag
pattern on a given number of rows like this: (you 
may want to display this pattern in a fixed font 
for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make 
this conversion given a number of rows:

"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        result = ""
        for row in range(numRows):
            step = (numRows - 1) * 2
            for a in range(row, len(s), step):
                result += s[a]
                if row > 0 and row < numRows - 1 and a + step - 2 * row < len(s):
                    result += s[a + step - 2 * row]       
        return result

a = Solution()
print(a.convert("PAYPALISHIRING", 3))  # PAHNAPLSIIGYIR
print(a.convert("PAYPALISHIRING", 4))  # PINALSIGYAHRPI
print(a.convert("PAYPALISHIRING", 1))  # PAYPALISHIRING
