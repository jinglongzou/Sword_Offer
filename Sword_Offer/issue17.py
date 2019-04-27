# -*- coding:utf-8 -*-
# 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

# 关键词：子结构，要求从A的某个节点开始与B的根节点匹配，那么之后的B的每个节点都与A的节点匹配，不仅值，还有结构也一致；

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # 定义一个递归函数比较两棵子树是否相同，是否相同的标记是全局的，初始为False
        def is_similar(point1, point2):
            if point2 is None:
                return True
            if point1 is None:
                return False
            if point1.val != point2.val:
                return False
            return is_similar(point1.left, point2.left) & is_similar(point1.right, point2.right)

        # write code hereif
        flag = False
        if pRoot2 is None:
            return flag
        # 是不是子结构的内涵：不仅数据相同，结构也相同
        # 因此首先需要比对B的根节点，在A中是否存在，然后比对B中剩下的子节点
        # 比对的思路，肯定要通过遍历来实现，而且遍历过程的左右子节点都必须比对，可以通过递归来实现
        # 首先遍历A找到与B根节点相同的节点，然后调用递归的比对函数，当完全符合时返回True，
        # 否则继续遍历A的其他节点
        # 采用先根遍历
        # 创建一个栈来存储A遍历中的右子节点
        s1 = []
        point1 = pRoot1
        point2 = pRoot2
        if pRoot1 is None:
            return flag
        while point1 or s1 != []:
            while (point1):
                if point1.val == point2.val:
                    flag = is_similar(point1, point2)
                    if flag == True:
                        return flag
                s1.append(point1.right)
                point1 = point1.left
            point1 = s1.pop(-1)
        return flag
