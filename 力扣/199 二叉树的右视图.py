'''
给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

'''

class TreeNode:
    def __init__(self, val =0, left =None, right = None):
        self.val = val
        self.left = left
        self.right = right

# 每次取最后的一个元素，然后整体替换为下一层
class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        res = []
        queue = [root] 
        while queue:
            res.append(queue[-1].val)
            new_queue = []
            for node in queue:
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue
        return res

# 怎么构造一棵树用treenode
# 例如：root = TreeNode(1)
#       root.left = TreeNode(2)
#       root.right = TreeNode(3)
#       root.left.left = TreeNode(4)
#       root.left.right = TreeNode(5)