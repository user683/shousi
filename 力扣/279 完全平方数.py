'''

给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

'''

# 解题思路

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)   # 初始化为无穷大，表示还没有算出来/不可达
        dp[0] = 0                       # 凑出0需要0个数字
        for i in range(1, n + 1):       # 从小往大填表
            j = 1
            while j * j <= i:           # 枚举所有 <= i 的完全平方数
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1

        return dp[n]
        