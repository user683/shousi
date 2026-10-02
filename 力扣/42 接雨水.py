'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

 

示例 1：



输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
示例 2：

输入：height = [4,2,0,3,2,5]
输出：9


'''

class Solution:
    def trap(self, height):
        if not height:
            return 0

        n = len(height)

        # left_max[i]：i 及其左边最高的柱子
        left_max = [0] * n
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        # right_max[i]：i 及其右边最高的柱子
        right_max = [0] * n
        right_max[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        # 每个位置能接的水 = min(左边最高, 右边最高) - 自身高度
        total_water = 0
        for i in range(n):
            total_water += min(left_max[i], right_max[i]) - height[i]

        return total_water


if __name__ == "__main__":
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
                    
                        
                    

# 为什么要「谁矮动谁」？ 比如 height[left] < height[right] 时，
# 虽然右边还没扫完、不知道右边真正的最高墙是多少，但右边至少已经有 height[right] 这么高 > 左边，所以左墙 left 
# 这一格的水量上限就是 left_max，一定不会被右边更高的墙影响，可以放心结算。