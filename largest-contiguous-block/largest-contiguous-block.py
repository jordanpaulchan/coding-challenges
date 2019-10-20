"""
Given an 2-dimensional array of integers, find the size of the largest contiguous block (horizontally/vertically connected only) of numbers with the same value.

1 2 3 
1 4 5
1 1 7

4 (of 1s)


1 2 5 1 7 
1 9 9 7 4
1 1 9 9 0

4

"""

directions = [[1, 0], [-1, 0], [0, 1], [0, -1],
              [1, 1], [1, -1], [-1, -1], [-1, 1]]


def dfs(matrix, row, col, visited):
    visited[row][col] = 1

    contiguousBlock = 1
    for r, c in directions:
        nextRow = row + r
        nextCol = col + c
        if (nextRow < 0 or nextRow >= len(matrix) or nextCol < 0 or nextCol >= len(matrix[row])):
            continue

        if (matrix[row][col] == matrix[nextRow][nextCol] and visited[nextRow][nextCol] == 0):
            num, count = dfs(matrix, nextRow, nextCol, visited)
            contiguousBlock += count

    return matrix[row][col], contiguousBlock


def largestContiguousBlock(matrix):
    if not matrix or not matrix[0]:
        return None, 0

    visited = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    largestBlock = 0
    largestNum = None

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if visited[row][col] == 0:
                num, block = dfs(matrix, row, col, visited)
                if block > largestBlock:
                    largestBlock = block
                    largestNum = num

    return largestNum, largestBlock


matrix = [
    [1, 2, 3],
    [1, 4, 5],
    [0, 1, 7]
]

matrix2 = [
    [1, 2, 5, 1, 7],
    [1, 7, 5, 7, 8],
    [1, 7, 7, 8, 5]
]

largestMatrix = largestContiguousBlock(matrix)
print('Number: {} Count: {}'.format(largestContiguousBlock(
    matrix2)[0], largestContiguousBlock(matrix2)[1]))
