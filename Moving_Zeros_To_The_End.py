"""
https://www.codewars.com/kata/52597aa56021e91c93000cb0
Write an algorithm that takes an array and moves all of the zeros to the end, 
preserving the order of the other elements
move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""


# def main(lst):
#     array = []
#     zero = 0
#     for element_lst in lst:
#         if element_lst != 0:
#             array.append(element_lst)
#         else:
#             zero += 1
#     array.extend([0] * zero)
#     return array


def main(lst):
    return [i for i in lst if i != 0] + [0] * lst.count(0)


if __name__ == "__main__":
    print(main([1, 0, 1, 2, 0, 1, 3]))
