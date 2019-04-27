# -*- coding:utf-8 -*-

# 输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）
# 形成树的一条路径，最长路径的长度为树的深度。

# 二叉树遍历算法考察：深度优先遍历，宽度优先遍历
# 遍历算法可以采用递归和非递归两种类型
# 递归就是：采用分治的思想来处理遍历
# 但是需要记录深度，那么就需要在遇到None时比较深度，在返回

# 非递归的深度优先遍历就是：借助栈的回溯法来实现
# 本题的非递归算法就就可以采用回溯法，用一个变量dep来记录深度，一个temp来记录遍历过程中的深度变化,
# 当遇到None时表明到叶结点了，这里就可以比较dep和temp了；弹出一个元素，temp就减1
# 特别备注：回溯法，为了比避免重复处理节点，节点入栈时一定要添加访问标记，在处理节点是修改节点标记



def find_depth(pRoot):
    dep = 0
    temp = 0
    if pRoot is None:
        return dep
    p = pRoot
    s = []
    while(p or s):
        while(p):
            temp +=1
            p = p.left
        if dep < temp:
            dep = temp
        p = s[-1]
        if p.right:
            p = p.right
        else:
            p = p.pop()
            temp -=1
    return dep

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def TreeDepth_recursive(self, pRoot):
        def depth(pRoot,dep,temp):
            if pRoot is None:
                return temp
            left = depth(pRoot.left,dep,temp+1)
            right = depth(pRoot.right,dep,temp+1)
            if dep < left:
                dep = left
            if dep < right:
                dep = right
            return dep
        dep = 0
        temp = 0
        dep = depth(pRoot, dep, temp)
        return dep
    def TreeDepth(self, pRoot):
        # write code here
        dep = 0
        temp = 0
        if pRoot is None:
            return dep
        p = pRoot
        s = []
        while (p or s):
            while(p):
                temp += 1
                s.append([p,0])
                p = p.left
            if dep < temp:
                dep = temp
            p,flag= s[-1]
            if p.right and flag == 0:
                s[-1][-1] = 1
                p = p.right
            else:
                s.pop()
                p = None
                temp -=1
        return dep

# 测试
pRoot = TreeNode(1)
pRoot.left = TreeNode(2)
pRoot.right = TreeNode(3)
pRoot.left.right = TreeNode(4)

s = Solution()
print(s.TreeDepth(pRoot))
print(s.TreeDepth_recursive(pRoot))