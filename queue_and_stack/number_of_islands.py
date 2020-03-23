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
