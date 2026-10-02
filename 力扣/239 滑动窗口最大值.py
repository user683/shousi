'''
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回 滑动窗口中的最大值 。

'''

class Solution:
    def maxSlidingWindow(self, nums, k):
        from collections import deque
        if not nums:
            return []
        
        n = len(nums)
        result = []
        window = deque()  # 存储索引
        
        for i in range(n):
            # 移除不在窗口范围内的索引
            if window and window[0] < i - k + 1:
                window.popleft()
            
            # 移除所有小于当前元素的索引
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            
            window.append(i)
            
            # 当窗口大小达到 k 时，记录最大值
            if i >= k - 1:
                result.append(nums[window[0]])
        
        return result