# A = [-3, -1, 3, 5, 7]
# B = [1, 3, 3, 5, 7]

# A = [-6, -4, -1, 3, 5, 7]
# result = [1, 3, 4, 5, 6, 7]


def abs_sort(array):
    if not array:
        return []

    left_idx = 0
    right_idx = len(array) - 1

    result = [0] * len(array)
    resultIdx = len(result) - 1

    while left_idx <= right_idx:
        if abs(array[left_idx]) > abs(array[right_idx]):
            result[resultIdx] = abs(array[left_idx])
            left_idx += 1
        else:
            result[resultIdx] = abs(array[right_idx])
            right_idx -= 1

        resultIdx -= 1

    return result


print(abs_sort([-3, -1, 3, 5, 7]))
print(abs_sort([-6, -4, -1, 3, 5, 7]))
print(abs_sort([-6, -4, -3, -1]))
print(abs_sort([3, 4, 9, 10]))
