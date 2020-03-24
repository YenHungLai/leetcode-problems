class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    count += 1
                    # Sinking adjacent lands.
                    self.dfs(row, col, grid)
        return count

    def dfs(self, row, col, grid):
        # Do nothing if out of bounds or not land.
        if row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[0]) - 1 or grid[row][col] == '0':
            return

        grid[row][col] = '0'
        # DFS adjacent lands.
        self.dfs(row, col + 1, grid)
        self.dfs(row, col - 1, grid)
        self.dfs(row + 1, col, grid)
        self.dfs(row - 1, col, grid)


input = [["1", "1", "1", "1", "0"],
         ["1", "1", "0", "1", "0"],
         ["1", "1", "0", "0", "0"],
         ["0", "0", "0", "0", "0"]]


def numIslands(grid) -> int:
    """BFS"""
    count, queue = 0, []

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '1':
                count += 1
                grid[row][col] == '0'
                queue.append((row, col))
                while queue:
                    r, c = queue.pop(0)
                    # Push all neighbors.
                    if r + 1 <= len(grid) - 1 and grid[r+1][c] == '1':
                        queue.append((r + 1, c))
                        grid[r+1][c] = '0'
                    if r - 1 >= 0 and grid[r-1][c] == '1':
                        queue.append((r - 1, c))
                        grid[r-1][c] = '0'
                    if c + 1 <= len(grid[0]) - 1 and grid[r][c+1] == '1':
                        queue.append((r, c + 1))
                        grid[r][c+1] = '0'
                    if c - 1 >= 0 and grid[r][c-1] == '1':
                        queue.append((r, c - 1))
                        grid[r][c-1] = '0'

    return count


print(numIslands(input))
