rooms = [[2147483647, -1, 0, 2147483647],
         [2147483647, 2147483647, 2147483647, -1],
         [2147483647, -1, 2147483647, -1],
         [0, -1, 2147483647, 2147483647]]


def wallsAndGates(rooms):
    queue = []
    for row in range(len(rooms)):
        for col in range(len(rooms[0])):
            if rooms[row][col] > 0:
                distance = 1
                queue.append((row, col, distance))
                while queue:
                    r, c, distance = queue.pop(0)
                    if rooms[r][c] == 0:
                        print(distance)
                        rooms[row][col] == distance
                        queue.clear()
                    else:
                        if r - 1 >= 0 and rooms[r-1][c] != -1:
                            queue.append((r - 1, c, distance))
                        if r + 1 <= len(rooms) - 1 and rooms[r+1][c] != -1:
                            queue.append((r + 1, c, distance))
                        if c - 1 >= 0 and rooms[r][c-1] != -1:
                            queue.append((r, c - 1, distance))
                        if c + 1 <= len(rooms[0]) - 1 and rooms[r][c+1] != -1:
                            queue.append((r, c + 1, distance))

                    distance += 1


wallsAndGates(rooms)
for i in rooms:
    print(i)
