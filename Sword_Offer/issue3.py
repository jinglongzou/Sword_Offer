# -*- coding:utf-8 -*-

# 3 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        seq = []
        if listNode is None:
            return seq
        while listNode:
            seq.append(listNode.val)
            listNode = listNode.next
        return seq[::-1]