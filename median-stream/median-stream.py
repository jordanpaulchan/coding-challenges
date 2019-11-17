from random import randint


def find_median(array):
    if not array:
        return None

    smallest = float('inf')
    largest = float('-inf')
    count = 0

    for num in array:
        count += 1
        smallest = min(smallest, num)
        largest = max(largest, num)

    median = count // 2
    guess = (largest + smallest) // 2

    while smallest <= largest:
        running_median = 0
        num_equals = 0
        for num in array:
            if num < guess:
                running_median += 1
            elif num == guess:
                num_equals += 1

        if running_median <= median:
            if num_equals > 0 and running_median + num_equals > median:
                return guess
            smallest = guess + 1
        else:
            largest = guess - 1
        guess = (largest + smallest) // 2

    return smallest


print(find_median([]))

print(find_median([1, 2, 3, 5, 8]))
print(find_median([8, 2, 1, 5, 3]))

print(find_median([1, 1, 1, 2, 2, 2, 8]))
print(find_median([1, 1, 1, 2, 2, 2, 8, 9, 10, 11]))

print(find_median([8, 8, 1, 8, 8, 1]))
print(find_median([8, 8, 8, 8, 8, 8]))
print(find_median([1, 1, 1, 1, 1, 1]))
print(find_median([2**31 - 1, 2**31 - 1, 2 **
                   31 - 1, 2**31 - 1, 2**31 - 1, 2**31 - 1]))
print(find_median([-2**31, -2**31, -2**31, -2**31, -2**31, -2**31]))

print(find_median([1]))

elements = [randint(1, 100) for _ in range(100)]
sorted_elements = sorted(elements)
print('Expected median: {}'.format(sorted_elements[len(elements)//2]))
print('Median fn: {}'.format(find_median(elements)))
