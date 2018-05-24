def hungry_rabbit_util(garden, row, col):
    max = 0
    next_row = None
    next_col = None

    for r, c in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        if row + r >= 0 and row + r < len(garden) and \
                col + c >= 0 and col + c < len(garden[row]):
            if garden[row + r][col + c] > max:
                max = garden[row + r][col + c]
                next_row = row + r
                next_col = col + c

    carrots = garden[row][col]
    garden[row][col] = 0

    if max > 0 and next_row is not None and next_col is not None:
        carrots += hungry_rabbit_util(garden, next_row, next_col)

    return carrots


def find_center(garden):
    row_options = [len(garden) // 2, len(garden) // 2]
    col_options = [len(garden[0]) // 2, len(garden[0]) // 2]

    # If even, 1st option is one less than half the length
    if len(garden) % 2 == 0:
        row_options[0] -= 1

    if len(garden[0]) % 2 == 0:
        col_options[0] -= 1

    max = 0
    row = None
    col = None

    for r_option in row_options:
        for c_option in col_options:
            if garden[r_option][c_option] > max:
                max = garden[r_option][c_option]
                row = r_option
                col = c_option

    return row, col


def hungry_rabbit(garden):
    if len(garden) == 0 or len(garden[0]) == 0:
        return 0

    # create a copy of the garden so we can mutate it
    copy = [g_row[:] for g_row in garden]
    row, col = find_center(copy)

    if row is None or col is None:
        return 0

    return hungry_rabbit_util(copy, row, col)


if __name__ == "__main__":
    garden = [
        [5, 7, 8, 6, 3],
        [0, 0, 7, 0, 4],
        [4, 6, 3, 4, 9],
        [3, 1, 0, 5, 8]
    ]

    print hungry_rabbit(garden)
