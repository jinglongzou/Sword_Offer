# -*- coding:utf-8 -*-
# 输入一棵二叉树，判断该二叉树是否是平衡二叉树。

# 考察二叉树的概念，平衡二叉树的概念，递归算法，分治思想
# 平衡二叉树：左右子树的高度差的绝对值不超过1，且都是平衡树；
# 平衡二叉树的常用实现方法有红黑树、AVL、替罪羊树、Treap、伸展树等
# 最小二叉平衡树的节点总数的公式如下 F(n)=F(n-1)+F(n-2)+1

# 递归算法：判断一个树是不是平衡树：分解为分别判断左右子树是否是平衡树，和左右子树的高度差的绝对值是否不大于1
#
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        def depth(pRoot,temp):
            # temp是辅助记录深度的变量
            if pRoot is None:
                return temp,True
            left,left_flag = depth(pRoot.left,temp + 1)
            #这里可以加入减枝操作
            if left_flag is False:
                return left_flag,left_flag
            right,right_flag = 1 + depth(pRoot.right,temp + 1)
            if right_flag is False:
                return right_flag,right_flag
            if left_flag is True and right_flag is True: #判断左右子树是否是平衡树
                if abs(left - right) <=1: #判断当前树是否是平衡树
                    return max(left,right),True
                else:
                    return max(left,right),False
            else:
                return max(left,right),False
        temp = 0
        temp,flag = depth(pRoot, temp)
        return flag
