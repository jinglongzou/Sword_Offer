# -*- coding:utf-8 -*-
# 请实现两个函数，分别用来序列化和反序列化二叉树

# 关键词：序列化、反序列化、二叉树
#         序列化：指遍历二叉树，输出节点数据序列
#         反序列化：由节点数据序列构建二叉树

# 思路：序列化：通过BFS遍历来存储每个节点，但未None时，该节点用'#'代替，从而构建序列
#       反序列：通过两个队列来实现，分别是数据队列和结点队列；对节点队列的每个节点，
#       每次弹出数据队列两个元素来构建节点的左右子节点。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        # 采用BFS遍历的方法来实现
        ret = []
        if root is None:
            return ret
        from collections import deque
        qu = deque()
        qu.append(root)
        while (qu):
            point = qu.popleft()
            if point:
                ret.append(point.val)
                qu.append(point.left)
                qu.append(point.right)
            else:
                ret.append('#')
        return ret

    def Deserialize(self, s):
        # write code here
        # 首先由s构建数据队列
        root = None
        if not s:
            return root
        from collections import deque
        L = s
        ch_idx = 0
        node_qu = deque()
        data = L[ch_idx]
        ch_idx += 1
        node = TreeNode(data)
        root = node
        node_qu.append(root)
        while (node_qu):
            node = node_qu.popleft()
            # if node:
            left = L[ch_idx]
            right = L[ch_idx + 1]
            ch_idx += 2
            if left == '#':
                node.left = None
            else:
                node.left = TreeNode(int(left))
                node_qu.append(node.left)
            if right == '#':
                node.right = None
            else:
                node.right = TreeNode(int(right))
                node_qu.append(node.right)
        return root

# 测试
root = TreeNode(8)
root.left = TreeNode(6)
root.right = TreeNode(10)
root.left.left = TreeNode(5)
root.left.right = TreeNode(7)
root.right.left = TreeNode(9)
root.right.right = TreeNode(11)

s = Solution()
strs = s.Serialize(root)
print(strs)
head = s.Deserialize(strs)
print(s.Serialize(head))