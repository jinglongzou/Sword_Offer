# -*- coding:utf-8 -*-

# 输入两个单调递增的链表，输出两个链表合成后的链表，
# 当然我们需要合成后的链表满足单调不减规则

# 利用归并算法就可实现，可以认为是考察排序算法
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        point1 = pHead1
        point2 = pHead2
        head = None
        point = head
        while(point1 and point2):
            if point1.val <= point2.val:
                if head is None:
                    head = point1
                    point = point1
                    point1 = point1.next
                else:
                    point.next = point1
                    point1 = point1.next
                    point = point.next
            else:
                if head is None:
                    head = point2
                    point = point2
                    point2 = point2.next
                else:
                    point.next = point2
                    point2 = point2.next
                    point = point.next
        while(point1):
            if head is None:
                head = point1
                point = point1
                point1 = point1.next
            else:
                point.next = point1
                point1 = point1.next
                point = point.next
        while(point2):
            if head is None:
                head = point2
                point = point2
                point2 = point2.next
            else:
                point.next = point2
                point2 = point2.next
                point = point.next
        return head