"""
https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa
John and Mary want to travel between a few towns A, B, C ... Mary has on a sheet of paper a list
 of distances between these towns. ls = [50, 55, 57, 58, 60]. John is tired of driving and he says
   to Mary that he doesn't want to drive more than t = 174 miles and he will visit only 3 towns.

Which distances, hence which towns, they will choose so that the sum of the distances is the 
biggest possible to please Mary and John?
Example:

[50, 55, 56, 57, 58]
With list ls and 3 towns to visit they can make a choice between: [50,55,57],[50,55,58],[50,55,60],
[50,57,58],[50,57,60],[50,58,60],[55,57,58],[55,57,60],[55,58,60],[57,58,60].


The sums of distances are then: 162, 163, 165, 165, 167, 168, 170, 172, 173, 175.
   
"""


from itertools import combinations

def choose_best_sum(t, k, ls):
    result = 0
    for combination in combinations(ls, k):
        s = sum(combination)
        if s <= t and s > result:
            result = s
    if result == 0:
        return None
    return result


ts = [50, 55, 56, 57, 58]
print(choose_best_sum(163, 3, ts))  # 163

ts = [50]
print(choose_best_sum(163, 3, ts))  # None

ts = [91, 74, 73, 85, 73, 81, 87]
print(choose_best_sum(331, 5, ts))   # None

# e1 = product('ABCD')
# print(list(e1))

# e2 = product('ABCD', [1, 2])
# print(list(e2))

# e3 = product([1, 2], [3, 4], [5, 6])
# print(list(e3))

# e1 = permutations('ABC', 2)
# print(list(e1))

# e2 = permutations([1,2,3], 2)
# print(list(e2))

# e1 = combinations('ABC', 2)
# print(list(e1))
