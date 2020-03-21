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

    for i in range(len(board[0])):
        for j in range(len(board)):
            num = board[i][j]
            if num != '.':
                if num in row_map[i]:
                    return False
                else:
                    row_map[i].append(num)

                if num in col_map[j]:
                    return False
                else:
                    col_map[j].append(num)

                box_index = (i // 3) * 3 + j // 3
                if num in box_map[box_index]:
                    return False
                else:
                    box_map[box_index].append(num)

    return True


print(isValidSudoku(board))
