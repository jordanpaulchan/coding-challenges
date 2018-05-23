directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def dfs(map, row, col):
    if row < 0 or row >= len(map) or \
            col < 0 or col >= len(map[row]) or \
            map[row][col] == 0:
        return None

    map[row][col] = 0
    for r, c in directions:
        dfs(map, row + r, col + c)

    return None


def num_islands(map):
    if not map or not map[0]:
        return 0

    islands = 0
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] == 1:
                dfs(map, row, col)
                islands += 1

    return islands
