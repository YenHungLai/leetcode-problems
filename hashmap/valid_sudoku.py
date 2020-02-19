from collections import defaultdict

board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]


def isValidSudoku(board):
    row_map = defaultdict(list)
    col_map = defaultdict(list)
    box_map = defaultdict(list)

    for row in range(len(board)):
        for col in range(len(board[0])):
            num = board[row][col]
            if num != '.':
                if num in row_map[row]:
                    print(row, col, '------', num)
                    return False
                else:
                    row_map[row].append(num)

                if num in col_map[col]:
                    print(row, col, '------', num)
                    return False
                else:
                    col_map[col].append(num)

                box_index = (row / 3) * 3 + col / 3
                if num in box_map[box_index]:
                    print(row, col, '------', num)
                    return False
                else:
                    box_map[box_index].append(num)

    print(col_map)
    print(row_map)
    return True


print(isValidSudoku(board))
