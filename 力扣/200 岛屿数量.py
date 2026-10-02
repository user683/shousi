'''
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。


示例 1：

输入：grid = [
  ['1','1','1','1','0'],
  ['1','1','0','1','0'],
  ['1','1','0','0','0'],
  ['0','0','0','0','0']
]
输出：1
示例 2：

输入：grid = [
  ['1','1','0','0','0'],
  ['1','1','0','0','0'],
  ['0','0','1','0','0'],
  ['0','0','0','1','1']
]
输出：
'''


# 什么解题思路
class sulution:
    def numIslands(self, grid):
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        def dfs(r,c): # r是啥c又是啥
          #r 如果越界huoze
          if  r < 0 or r >= rows or c < 0 or c>= cols or grid[r][c] == '0':
              return
          grid[r][c] = '0' # 标记为已经访问
          dfs(r-1,c)
          dfs(r+1,c)
          dfs(r,c-1)
          dfs(r,c+1)

        for r in range(rows):
          for c in range(cols):
            if grid[r][c] == '1':
              count += 1
              dfs(r,c)
        return count


if __name__ == '__main__':
    solution = sulution()
    grid1 = [
        ['1','1','1','1','0'],
        ['1','1','0','1','0'],
        ['1','1','0','0','0'],
        ['0','0','0','0','0']
    ]
    res = solution.numIslands(grid1)
    print(res)

   