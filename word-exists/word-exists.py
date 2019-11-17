def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    def dfs(row, col, position):
        letter = board[row][col]
        board[row][col] = '#'

        for ro, co in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr = ro + row
            nc = co + col

            if nr < 0 or nr >= len(board) or nc < 0 or nc >= len(board[row]):
                continue

            if board[nr][nc] != word[position + 1]:
                continue

            if position + 1 == len(word) - 1 or dfs(nr, nc, position + 1):
                return True

        board[row][col] = letter
        return False

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == word[0] and dfs(row, col, 0):
                return True

    return False


print(exist([["A", "B"]], "AB"))
