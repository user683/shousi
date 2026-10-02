'''
给定一个字符串数组 strs ，将 变位词 组合在一起。 可以按任意顺序返回结果列表。

注意：若两个字符串中每个字符出现的次数都相同，则称它们互为变位词。

 

示例 1：

输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
示例 2：

输入: strs = [""]
输出: [[""]]
示例 3：

输入: strs = ["a"]
输出: [["a"]]

'''

# 直接一手暴力法

class Solution:
    def groupAnagrams(self, strs):
        ans = []
        for s in strs:
            found = False
            for group in ans:
                if sorted(group[0]) == sorted(s):
                    group.append(s)
                    found = True
                    break
            if not found:
                ans.append([s])
        return ans

        
if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrames(strs))