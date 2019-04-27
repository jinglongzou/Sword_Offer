# -*- coding:utf-8 -*-

# 操作给定的二叉树，将其变换为源二叉树的镜像。

# 主要子节点交换，对应的子树也要交换

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回镜像树的根节点
    def method(self,root):
        if root is None:
            return None
        node = root.left
        root.left = root.right
        root.right = node
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root
    def method2(self,root):
        # 通过递归的思路来变换
        # 通过一个中间变量来交换左右子节点
        # 并对子节点递归调用镜像
        def T_mirror(root):
            if root is None:
                return None
            node = root.left
            root.left = T_mirror(root.right)
            root.right = T_mirror(node)
            return root
        return T_mirror(root)
    def Mirror(self, root):
        # write code here
        # 通过栈来实现交换
        # 利用先根遍历，在遇到根时就交换左右子树，并将交换后的右子树入栈
        s = []  # 创建栈，存右子树
        point = root
        while point is not None or s != []:
            while point is not None:
                node = point.left
                point.left = point.right
                point.right = node
                s.append(point.right)
                point = point.left
            point = s.pop(-1)
        return root


