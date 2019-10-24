"""
Problem: Find smallest common number in list of sorted arrays.
e.g. array1: [1, 3, 5, 10, 20] array2: [2, 4, 5, 10, 20] array3: [2, 4, 10, 20]
common elements = > 10 & 20 result = > 10
Constraints:
* Any number of arrays
* Each array could be of any size
* [execution time limit] 4 seconds(js)

10
10
10
"""


def smallest_common_num(arrays):
    idxs = [0] * len(arrays)

    largest_num = float('-inf')
    largest_arrays_idxs = set()

    while len(largest_arrays_idxs) != len(arrays):
        for idx, array in enumerate(arrays):
            if idxs[idx] >= len(array):
                return None

            if array[idxs[idx]] > largest_num:
                largest_num = array[idxs[idx]]
                largest_arrays_idxs = {idx}
            elif array[idxs[idx]] == largest_num:
                largest_arrays_idxs.add(idx)

        for idx in range(len(idxs)):
            if idx not in largest_arrays_idxs:
                idxs[idx] += 1

    return largest_num


print(smallest_common_num([[1, 3, 5, 10, 20],
                           [1, 2, 4, 5, 10, 20],
                           [2, 4, 10, 20]]))
