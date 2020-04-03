rooms = [[2147483647, -1, 0, 2147483647],
         [2147483647, 2147483647, 2147483647, -1],
         [2147483647, -1, 2147483647, -1],
         [0, -1, 2147483647, 2147483647]]


def wallsAndGates(rooms):
    """Start from gate."""
    queue = []
    for row in range(len(rooms)):
        for col in range(len(rooms[0])):
            if rooms[row][col] == 0:
                distance = 0
                queue.append((row, col, distance))
                while queue:
                    r, c, distance = queue.pop(0)
                    rooms[r][c] = distance
                    # Do not override rooms closer to other gates.
                    if r - 1 >= 0 and rooms[r-1][c] > distance:
                        queue.append((r - 1, c, distance + 1))
                    if r + 1 <= len(rooms) - 1 and rooms[r+1][c] > distance:
                        queue.append((r + 1, c, distance + 1))
                    if c - 1 >= 0 and rooms[r][c-1] > distance:
                        queue.append((r, c - 1, distance + 1))
                    if c + 1 <= len(rooms[0]) - 1 and rooms[r][c+1] > distance:
                        queue.append((r, c + 1, distance + 1))


wallsAndGates(rooms)
for i in rooms:
    print(i)
print()


def wallsAndGates2(rooms):
    """DFS, the same approach as BFS, how to differentiate?"""
    distance = 0
    for row in range(len(rooms)):
        for col in range(len(rooms[0])):
            if rooms[row][col] == 0:
                dfs(row, col, distance, rooms)


def dfs(r, c, distance, rooms):
    if r < 0 or c < 0 or r >= len(rooms) or c >= len(rooms[0]) or rooms[r][c] < distance:
        return
    rooms[r][c] = distance
    dfs(r + 1, c, distance + 1, rooms)
    dfs(r - 1, c, distance + 1, rooms)
    dfs(r, c + 1, distance + 1, rooms)
    dfs(r, c - 1, distance + 1, rooms)


wallsAndGates2(rooms)
for i in rooms:
    print(i)
