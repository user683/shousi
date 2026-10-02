# 给你一个字符串 s ，考虑其所有 重复子串 ：即 s 的（连续）子串，在 s 中出现 2 次或更多次。这些出现之间可能存在重叠。

# 返回 任意一个 可能具有最长长度的重复子串。如果 s 不含重复子串，那么答案为 "" 。

 
# 示例 1：

# 输入：s = "banana"
# 输出："ana"
# 示例 2：

# 输入：s = "abcd"
# 输出：""
 

# 提示：

# 2 <= s.length <= 3 * 104
# s 由小写英文字母组成


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        base, mod = 131, 2**64

        def check(L):
            h = 0
            for i in range(L):
                h = (h * base + ord(s[i])) % mod
            
            seen = {h}
            p = pow(base, L - 1, mod)
            
            for i in range(1, n - L + 1):
                # 修正：整个表达式取模，且旧字符要乘以 p
                h = ((h - ord(s[i - 1]) * p) * base + ord(s[i + L - 1])) % mod
                
                if h in seen:
                    return s[i:i + L]
                seen.add(h)
            return ""
        
        left, right = 1, n - 1
        ans = ''
        while left <= right:
            mid = (left + right) // 2
            res = check(mid)
            if res:
                ans = res
                left = mid + 1
            else:
                right = mid - 1
        return ans

if __name__ == '__main__':
    s = Solution()
    print("答案")
    x = s.longestDupSubstring("banana") # 输出: "ana"
    print(x)
