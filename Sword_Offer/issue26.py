# -*- coding:utf-8 -*-
# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
# 要求不能创建任何新的结点，只能调整树中结点指针的指向。

'''
输入：一棵二叉树
输出：一个拍好序的双向链表

因此一个节点的左右指针，要变为双向链表的前后指针；

分析：考察了二叉树的概念，搜索二叉树的概念；
需要用到二叉树的遍历算法：递归的遍历算法；非递归的遍历算法；

这里考虑对节点的指针更改操作：
    对每个当前节点，其左子针指向链表的尾节点，尾节点的右子针指向当前节点
    有以下特殊情况：对链表的第一个节点，尾节点是None,因此要单独考虑
                    对链表的最后一个节点，其右子节点为None，双向链表中也为None，所以不用单独处理
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        head = None
        rear = None
        node = pRootOfTree
        s = [] #栈
        while node or s != []:
            while node:
                s.append(node)
                node=node.left
            node = s.pop()
            if head is None:
                head = node
                rear = head
            else:
                node.left = rear
                rear.right = node
                rear = node
            node = node.right
        return head

#测试
if __name__ == '__main__':
    pRootOfTree = TreeNode(2)
    pRootOfTree.left = TreeNode(1)
    pRootOfTree.right = TreeNode(3)
    s = Solution()
    head = s.Convert(pRootOfTree)
    while head:
        print(head.val)
        head=head.right
