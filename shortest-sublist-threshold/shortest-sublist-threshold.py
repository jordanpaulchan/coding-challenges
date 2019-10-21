"""
Given a list of positive numbers and a threshold. 
Find the shortest sub list which sum up to greater than the threshold
"""


def shortestThreshold(nums, threshold):
    if not nums:
        return []

    left = right = 0
    current = 0
    minList = (float('inf'), -1, -1)

    while right < len(nums):
        current += nums[right]

        while current >= threshold and left <= right:
            if right - left + 1 < minList[0]:
                minList = (right - left + 1, left, right + 1)

            current -= nums[left]
            left += 1

        right += 1

    while current >= threshold and left < right:
        if right - left < minList[0]:
            minList = (right - left, left, right)

        current -= nums[left]
        left += 1

    return nums[minList[1]:minList[2]]


print(shortestThreshold([3, 5, 2], 10))
print(shortestThreshold([4, 1, 3, 5, 2, 1, 8], 10))
print(shortestThreshold([3, 5, 2, 1, 9], 10))
print(shortestThreshold([9, 1, 3, 5, 2], 10))
print(shortestThreshold([3, 5, 1, 9, 10], 10))
print(shortestThreshold([3, 5, 10, 1, 9], 10))
print(shortestThreshold([10, 3, 5, 1, 9], 10))
