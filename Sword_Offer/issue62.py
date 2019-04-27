# -*- coding:utf-8 -*-

# 给定一棵二叉搜索树，请找出其中的第k小的结点。
# 例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。

# 考察：二叉搜索树、查找算法
# 二叉搜索树：左子节点小于等于根节点，右子节点大于等于根节点
# 采用中序遍历，并将第k个数输出
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        # 特殊情况
        if pRoot is None:
            return
        s = []
        p = pRoot
        count = 0
        while(p or s):
            while(p):
                s.append(p)
                p = p.left
            p = s.pop()
            count +=1
            if count == k:
                return p.val
            p = p.right
        return None