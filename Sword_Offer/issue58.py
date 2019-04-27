# -*- coding:utf-8 -*-
# 请实现一个函数，用来判断一颗二叉树是不是对称的。
# 注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

# 关键词：函数、判断、二叉树、对称；
#         对称：值左右子树的结构和结点值都相同。对称的节点值很容易比较，但是结构如何比较呢？
#         转化为判断根节点的两个子树A和B是互为镜像的,也就是A的左子节点== B的右子节点，A的右子节点== B的左子节点
# 法1：通过递归来实现
# 法2：通过非递归DFS来实现：每次成对的入栈，成对的出栈；
#                           当成对出栈的元素，元素不匹配时返回False,否者继续下一对检查
# 法3：通过非递归的BFS来实现:每次成对的入队，成对的出队，#
#                            当元素不匹配返回False,否者继续下对检查
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def DFS_method(self,pRoot):
        if pRoot is None:
            return True
        s = []
        left = pRoot.left
        right = pRoot.right
        s.append(left)
        s.append(right)
        while(s):
            right = s.pop()
            left = s.pop()
            if right and left:
                if left.val == right.val:
                    s.append(left.left)
                    s.append(right.right)
                    s.append(left.right)
                    s.append(right.left)
                else:
                    return False
            elif left is None and right is None:
                    continue
            else:
                return False
        return True
    def BFS_method(self,pRoot):
        from collections import deque
        if pRoot is None:
            return True
        qu = deque()
        qu.append(pRoot.left)
        qu.append(pRoot.right)
        while(qu):
            left = qu.popleft()
            right = qu.popleft()
            if left and right:
                if left.val == right.val:
                    qu.append(left.left)
                    qu.append(right.right)
                    qu.append(left.right)
                    qu.append(right.left)
                else:
                    return False
            elif left is None and right is None:
                continue
            else:
                return False
        return True
    def isSymmetrical(self, pRoot):
        # write code here
        def is_similar(tree1,tree2):
            if tree1 is None and tree2 is None:
                return True
            if tree1 and tree2:
                # 先比较值
                if tree1.val != tree2.val:
                    return False
                #分别比较左右子树
                return is_similar(tree1.left,tree2.right) and is_similar(tree1.right,tree2.left)
            else:
                return False
        if pRoot is None:
            return True
        return is_similar(pRoot.left,pRoot.right)
