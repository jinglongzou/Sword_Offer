# -*- coding:utf-8 -*-
# 从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。

# z直接BFS遍历，分层输出就好了
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        ret = []
        if pRoot is None:
            return ret
        nodelist = []
        nodelist.append(pRoot)
        while (nodelist):
            newlist = []
            layer = []
            for node in nodelist:
                layer.append(node.val)
                if node.left:
                    newlist.append(node.left)
                if node.right:
                    newlist.append(node.right)
            ret.append(layer)
            nodelist = newlist
        return ret