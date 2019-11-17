from collections import deque
from heapq import heapify, heappush, heappop


def leastInterval(tasks, n):
    min_heap = []
    queue = deque([(0, '0') for _ in range(n)])

    tasks_map = {}
    for task in tasks:
        if task not in tasks_map:
            tasks_map[task] = 1
        else:
            tasks_map[task] += 1

    min_heap = [(-num, task) for task, num in tasks_map.items()]
    heapify(min_heap)

    done_tasks = 0
    num_cycles = 0
    while done_tasks < len(tasks):
        if min_heap:
            num, task = heappop(min_heap)
            queue.append((num + 1, task))
            done_tasks += 1
        else:
            queue.append((0, '0'))

        cooled_task = queue.popleft()
        if cooled_task[0] < 0:
            heappush(min_heap, cooled_task)

        num_cycles += 1

    return num_cycles


print(leastInterval(["A", "A", "A", "B", "B", "B"], 2))
