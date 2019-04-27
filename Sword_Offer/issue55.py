# -*- coding:utf-8 -*-

# 给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null

# 分析：考察链表遍历、环的概念、检测环的方法、
#   环：也就是遍历链表时，能够再次访问
#   为每个节点设置一个访问标记，或者借助列表来,每次如表，都检查是否在表中，不在就加入，在就返回该节点，
#   这个时间复杂度是O(n)，但是空间复杂度也为O(n)
#   法2：
#   因此改进算法降低空间复杂度：通过双指针实现，一个指针走一步，一个指针走两步；
#   当指针为空，时返回None，当两个指针相同时返回节点
# 理论基础：设置快慢指针fast和low，fast每次走两步，low每次走一步。假如有环，
#           两者一定会相遇（因为low一旦进环，可看作fast在后面追赶low的过程，
#           每次两者都接近一步，最后一定能追上）。
#
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def method1(self,pHead):
        if pHead is None:
            return None
        slow = pHead
        fast = pHead
        while(slow and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if slow is None or fast.next is None:
            return None
        p2 = pHead
        while(fast!= slow):
            fast = fast.next
            slow = slow.next
        return slow
    def EntryNodeOfLoop(self, pHead):
        # write code here
        s = []
        if pHead is None:
            return None
        p = pHead
        while(p):
            if p in s:
                return p
            else:
                s.append(p)
            p = p.next
        return None

# 测试
pHead = ListNode(1)
pHead.next = ListNode(2)
pHead.next.next = pHead
s = Solution()
print(s.method1(pHead))
print(s.EntryNodeOfLoop(pHead))
