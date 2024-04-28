"""
https://leetcode.com/problems/roman-to-integer/

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

III - 3
IIII - 4
IV - 4

VIIII - 9
IX - 9

"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s = s.replace('IV', 'IIII').replace('IX', 'VIIII')
        s = s.replace('XL', 'XXXX').replace('XC', 'LXXXX')
        s = s.replace('CD', 'CCCC').replace('CM', 'DCCCC')
        return sum(d[i] for i in s)

        # result = 0
        # for i in s:
        #     result += d[i]
        # return result


        # roman_to_int: dict[int] = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # result: int = 0
        # prev_value: int = 0
        # for char in s:
        #     value: int = roman_to_int[char]
        #     if value > prev_value:
        #         result += value - 2 * prev_value
        #     else:
        #         result += value
        #     prev_value = value
        # return result

a = Solution()
print(a.romanToInt('LVIII'))
print(a.romanToInt('MCMXCIV'))
print(a.romanToInt('CD'))
