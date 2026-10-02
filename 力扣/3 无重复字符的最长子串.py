'''
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串的长度。

 

示例 1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。注意 "bca" 和 "cab" 也是正确答案。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

'''
class Solution:
    def lengthOFLongestSubstring(self, s):
        if not s:
            return 0
        n = len(s)
        left, right = 0, 0
        ans = 0
        char_set = set()
        
        while right< n:
            if s[right] not in char_set:
                char_set.add(s[right])
                ans = max(ans, right-left+1)
                right += 1
            else:
                char_set.remove(s[left])
                left += 1
        return ans

if __name__ == '__main__':
    s = Solution
    print(s.lengthOFLongestSubstring(s,"abcabcbb"))
        