"""
https://www.codewars.com/kata/5270d0d18625160ada0000e4
Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.

Example scoring

 Throw       Score
 ---------   ------------------
 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)  

"""


# def score(dice):
#     total = 0
#     for i in range(1, 7):
#         if dice.count(i) >= 3:
#             if i == 1:
#                 total += i * 1000
#             else:
#                 total += i * 100
#             dice.remove(i)
#             dice.remove(i)
#             dice.remove(i)
#     for i in dice:
#         if i == 1:
#             total += 100
#         elif i == 5:
#             total += 50
#     return total

def score(dice):
    total = 0
    for i in range(1, 7):
        count = dice.count(i)
        if count >= 3:
            total += 1000 * i if i == 1 else 100 * i
            count -= 3
        total += 100 * count if i == 1 else 50 * count if i == 5 else 0
    return total


if __name__ == "__main__":
    print(score( [5, 1, 3, 4, 1] ))
    print(score( [1, 1, 1, 3, 1]))
    print(score( [2, 3, 4, 6, 2]))
    print(score( [6, 6, 6, 3, 3]))

