def subarray_sum(nums, target):
    map = {}
    sum = 0
    ans = []

    for i in range(len(nums)):
        if sum not in map:
            map[sum] = [i]
        else:
            map[sum].append(i)

        if sum - target in map:
            ans.extend([[start, i] for start in map[sum - target]])
        sum += nums[i]

    if sum - target in map:
        ans.extend([[start, len(nums)] for start in map[sum - target]])

    return ans


print(subarray_sum([1, 5, 3, 6, -1, 13, 5], 18))
print(subarray_sum([1, 5, 3, 6, -1, 13, 5], 0))
print(subarray_sum([1, 5, 3, 6, -1, 13, 5], 9))
print(subarray_sum([], 0))
print(subarray_sum([1, 5, 3, 6, -1, 13, 60], 60))
