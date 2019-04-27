# -*- coding:utf-8 -*-
# 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，
# 重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

# 关键词： 排序的链表、重复、删除重复
# 法1：通用方法分析：
#   删除重复节点，这里的重复节点都不保留了，关键是检查给节点的值是否已经存在，那么就需要记录每个节点的值，
#   以便后续判断比较是否存在，因此空间复杂度为O(n)
#   必然要遍历每个节点，因此最低时间复杂度为O(n)
#   删除节点操作：将pre的next改一下，特殊情况，头结点就是重复的，那么头结点需要更改
# 法2：特殊方法分析：
#   因为链表时拍好序的，因此重复的节点必然在一起，因此只需要判断下一个节点和当前节点是否相同，
#   并做相应的节点修改处理，如果相同，就修改当前节点的next,否则向一个节点前进

# 问题总结：1、审题不仔细，没有充分利用题干信息
#           2、算法逻辑图不清晰
#           3、特殊情景没有考虑到，总是漏处理某些情况
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def method1(self,pHead):
        if pHead is None:
            return None
        p = pHead
        pre = None
        while(p and p.next):
            next_p = p.next
            if p.val == next_p.val: #检测到重复
                while(next_p and next_p.val == p.val): #处理第一个重复后的重复节点
                    next_p = next_p.next
                if pre is None:
                    pHead = next_p
                else:
                    pre.next = next_p
                p = next_p
            else:
                pre = p
                p = p.next
        return pHead



    def deleteDuplication(self, pHead):
        # write code here
        s = []
        dump = []
        if pHead is None:
            return None
        p = pHead
        pre = None
        while(p):
            if p.val in s:
                dump.append(p.val)
                p = p.next
            else:
                s.append(p.val)
                p = p.next
        p = pHead
        while(p):
            if p.val in dump:
                if pre is None:
                    pHead = p.next
                    p = p.next
                else:
                    pre.next = p.next
                    p = p.next
            else:
                pre = p
                p = p.next
        return pHead
# 测试
pHead = ListNode(1)
pHead.next = ListNode(2)
pHead.next.next =  ListNode(2)
s = Solution()
pHead=s.method1(pHead)
while(pHead):
    print(pHead.val)
    pHead = pHead.next
