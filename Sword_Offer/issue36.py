# -*- coding:utf-8 -*-
# 输入两个链表，找出它们的第一个公共结点。

# 输入：两个链表的头
# 输出：第一个公共节点，地址或者元素

# 问题：这里的第一个公共节点中的第一是什么概念？
# 公共节点是指同一个节点，也就是两个链表在一个节点汇合，地址、元素都相同才叫公共节点。
# 因此这里这里的公共节点：要求两个链表的某一个节点是同一节点对象

# 考察：链表的概念，公共节点概念
# 暴力解法是：将链表1的每一个节点和链表2的每一个节点做比较，返回相同的节点，时间复杂度是O(mn)

# 由于有公共节点，所以从公共节点之后都是相同的，因此，如果两个两边的长度为m,n，那么可以从长的链表的
# 第|m-n|个元素开始和短的链表比较，只有当两个链表的节点相同时才退出循环
#
# 将两个链表A,B,连成两个链表：AB 和BA，都从第一个节点开始，当节点相同时返回



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        p1 = pHead1
        p2 = pHead2
        while (p1 != p2):
            p1 = pHead2 if p1 is None else p1.next
            p2 = pHead1 if p2 is None else p2.next
        return p1
