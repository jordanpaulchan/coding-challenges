"""
Given an array of integers like the following:

[1, 6, 3, 8, 9]

Reverse the order of the integers in the array, but only those divisible by 3, while keeping all the other integers in the same positions as before. E.g.

[1, 9, 3, 8, 6]
"""


def reverseDivThree(array):
    left = 0
    right = len(array) - 1

    while left < right:
        if array[left] % 3 != 0:
            left += 1
        elif array[right] % 3 != 0:
            right -= 1
        else:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    return array


print(reverseDivThree([1, 6, 3, 8, 9]))
print(reverseDivThree([15, 3, 2, 0, 7, -3, 5]))
print(reverseDivThree([-3, 3, 9, 12]))
print(reverseDivThree([1, 2, 4, 5, 7]))
