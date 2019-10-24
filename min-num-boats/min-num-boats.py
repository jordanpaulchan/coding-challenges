# weight the boat can carry 190kg
# max 2 people per boat
# list of peoples weights [20, 30, 40, 60, 60, 90]

"""
90
60 + 20
60 + 30
40

90
60
60 + 20
40 + 30

90 + 20
60 + 30
60 + 40
"""


def min_num_boats(max_weight, people):
    if not people:
        return 0

    if max_weight <= 0:
        raise Exception('invalid max weight')

    min_num = 0
    left = 0
    right = len(people) - 1
    while left <= right:
        currentWeight = people[right]
        if currentWeight > max_weight:
            raise Exception('boat not heavy enough for person')

        right -= 1
        if currentWeight + people[left] <= max_weight:
            left += 1
        min_num += 1

    return min_num


weight = 100
people = [20, 30, 40, 60, 80, 90]
print(min_num_boats(weight, people))
