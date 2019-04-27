# -*- coding:utf-8 -*-

# 从上往下打印出二叉树的每个节点，同层节点从左至右打印。

# 考察二叉树的遍历：宽度优先遍历，基于队列来实现

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        from collections import deque
        q = deque() #队列
        ret = []
        if root is None:
            return ret
        point = root
        q.append(point)
        while(q!=[]):
            point = q.popleft()
            ret.append(point.val)
            if point.left is not None:
                q.append(point.left)
            if point.right is not None:
                q.append(point.right)
        return ret