# -*- coding:utf-8 -*-

# 4 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
#   例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

# 考察二叉树的遍历，三种遍历概念、二叉树概念

# 通过递归来构建，通过前序遍历可以找到根节点，由根节点和中序遍历可以得到左右子树的节点，分别对两个子树再次递归
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        def rebuildBtree(pre,tin):
            pre_len = len(pre)
            tin_len = len(tin)
            if pre_len == 0 and tin_len ==0:
                return None
            data = pre[0]
            tree = TreeNode(data)
            index = 0
            # 找到中序遍历的中的根节点索引
            for i in range(len(tin)):
                if tin[i] == data:
                    index = i
                    break
            tree.left = rebuildBtree(pre[1:index+1],tin[0:index])
            tree.right = rebuildBtree(pre[index+1:],tin[index+1:])
            return tree
        return rebuildBtree(pre,tin)
pre = [1,2,4,3,5,6]
tin = [4,2,1,5,3,6]
S = Solution()
tree = S.reConstructBinaryTree(pre,tin)