'''
给定两个字符串 s 和 t 。返回 s 中包含 t 的所有字符的最短子字符串。如果 s 中不存在符合条件的子字符串，则返回空字符串 "" 。

如果 s 中存在多个符合条件的子字符串，返回任意一个。

 

注意： 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。

 

示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC" 
解释：最短子字符串 "BANC" 包含了字符串 t 的所有字符 'A'、'B'、'C'
示例 2：

输入：s = "a", t = "a"
输出："a"
示例 3：

输入：s = "a", t = "aa"
输出：""
解释：t 中两个字符 'a' 均应包含在 s 的子串中，因此没有符合条件的子字符串，返回空字符串
'''

class Solution:
    def minWindow(self, s, t):
        # 1. 统计 t 中每个字符需要的数量
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        window = {}          # 当前窗口内各字符数量
        left = 0
        valid = 0            # 已满足需要数量的字符种类数
        start, length = 0, len(s)+1

        # 2. right 向右扩张
        for right, c in enumerate(s):
            if c in need:
                window[c] = window.get(c, 0) + 1
                # 该字符数量恰好达标时，valid 才 +1（只加一次）
                if window[c] == need[c]:
                    valid += 1

            # 3. 窗口已覆盖 t，开始收缩 left
            while valid == len(need):
                # 先更新最短窗口
                if right - left + 1 < length:
                    start, length = left, right - left + 1

                # 移出左指针指向的字符
                d = s[left]
                left += 1
                if d in need:
                    # 移出前恰好达标，移出后就不达标了
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        if start == 0 and length == len(s) + 1:
            return ""
        return s[start:start + length]