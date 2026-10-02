'''
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。


示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]


'''


class Solution:
    def generateParenthesis(self, n):
        res = []
        self.dfa(n, n, '', res)
        return res

    def dfa(self, left, right, path, res):
        if left > right:
            return
        if left == 0 and right == 0:
            res.append(path)
            return
        if left > 0:
            self.dfa(left - 1, right, path + '(', res)
        if right > 0:
            self.dfa(left, right - 1, path + ')', res)  

if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))


