# -*- coding:utf-8 -*-

# 输入一个链表，输出该链表中倒数第k个结点。

# 法一：通过两次遍历实现：第一次遍历统计节点个数n；第二次遍历返回索引为n-k的节点值
# 法2：借助一个辅助的列表，一次遍历实现

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head is None:
            return None
        point = head
        L = []
        while(point):
            L.append(point)
            point = point.next
        if k <= len(L) and k >0:
            return L[-k]
        else:
            return None