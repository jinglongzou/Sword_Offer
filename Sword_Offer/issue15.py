# -*- coding:utf-8 -*-

# 输入一个链表，反转链表后，输出新链表的表头。

# 考察链表的遍历和修改、节点指针的变化

# 从第一个节点开始，让新加入的节点的next指向已有的链表头
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def method(self,pHead):
        if pHead is None:
            return pHead
        pre = None
        cur = pHead
        while(cur):
            nextcur = cur.next
            cur.next = pre
            pre = cur
            cur = nextcur
        return pre
    def ReverseList(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        pre = None
        cur = pHead
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre