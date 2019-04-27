# -*- coding:utf-8 -*-
# 题目描述
# 给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
# 注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

# 关键词：二叉树、中序遍历、返回给定节点的下一个节点、节点包含三个指针
# 考察二叉树的遍历算法：深度优先：先根、中根、后根（递归或者基于栈的非递归；宽度优先：(基于队列的非递归)
# 变种二叉树的优化遍历算法

# 问题：这里所给定一个二叉树和一个节点，初始的函数接口并没二叉树，只有给定节点，如何从根节点开始遍历呢？
#       这里给了有父指针，因此可以回溯

#  法1：通用方法：这里没有考虑使用指向父节点的指针；如果知道根节点，从树的根节点开始，进行中序遍历，并与给定节点比较，相同就返回下一个节点，
#                 否则继续遍历直到遍历完。
# 由于只给了给定节点，以及父指针的特性，因此，利用父节点回溯
# 基本思路：
#           首先检查给定节点是否存在；
#           检查右子节点；
#           检查父节点，并判断当前节点是父节点的左子节点还是右子节点：
#           左：返回父节点；右：就递推的查找父节点，直到子节点是父节点的左子节点，若父节点不存在，就返回None
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode is None:
            return None
        if pNode.right:
            temp = pNode.right
            while(temp.left):
                temp = temp.left
            return temp
        while(pNode.next):
            if (pNode == pNode.next.left):
                return pNode.next
            pNode = pNode.next
        return None