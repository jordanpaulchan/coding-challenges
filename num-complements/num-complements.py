# l = [2, 1, 3, 4], k = 2; num of complements 2
# l = [4, 1, 3, 2], k = 2; num of complements 2


def numComplements(l, k):
    seen = set()
    counter = 0

    for num in l:
        if num in seen:
            counter += 1

        seen.add(num + k)
        seen.add(num - k)

    return counter


print(numComplements([22, 21, 23, 24], 2))
print(numComplements([24, 21, 23, 22], 2))
print(numComplements([2, 1, 3, 4], 2))
print(numComplements([2, 1, 3, 4], 1))
print(numComplements([2, 1, 3, 4], 0))
print(numComplements([2, 1, 3, 4, -1], 2))
