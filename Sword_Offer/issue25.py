# -*- coding:utf-8 -*-

#考察链表的操作，以及操作的类型的分类
# 对第二种方法：创建新节点，更新random，更新next

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        '''
        #递归法
        # write code here
        # 这是一个很明显的递归问题，next会链接所有的节点，random只需要给它一个值就可以
        # random对应的节点对象，会在next的递归中创建；
        # 但是有个问题，random指向的节点是原来链表的节点，并没有指向复制创建的节点
        # 对递归调用是有条件的,
        root = None
        if pHead is None:
            return root
        point = pHead
        root = RandomListNode(point.label)
        root.random = point.random
        root.next = self.Clone(point.next)
        return root
        '''
        if not pHead:
            return None

        dummy = pHead

        # first step, N' to N next
        while dummy:
            dummynext = dummy.next
            copynode = RandomListNode(dummy.label)
            copynode.next = dummynext
            dummy.next = copynode
            dummy = dummynext

        dummy = pHead

        # second step, random' to random'
        while dummy:
            dummyrandom = dummy.random
            copynode = dummy.next
            if dummyrandom:
                copynode.random = dummyrandom.next
            dummy = copynode.next

        # third step, split linked list
        dummy = pHead
        copyHead = pHead.next
        while dummy:
            copyNode = dummy.next
            dummynext = copyNode.next
            dummy.next = dummynext
            if dummynext:
                copyNode.next = dummynext.next
            else:
                copyNode.next = None
            dummy = dummynext

        return copyHead


def Clone(pHead):
    if pHead is None:
        return None
    point = pHead
    while (point):
        pointnext = point.next
        node = RandomListNode(point.label)
        node.next = pointnext
        point.next = node
        point = pointnext
    point = pHead
    while (point):
        pointrandom = point.random
        node = point.next
        if pointrandom is not None:
            node.random = pointrandom.next
            #print(pointrandom.next.label)
        else:
            node.random = None
        point = node.next
    point = pHead
    root = pHead.next
    while (point):
        node = point.next
        pointnext = node.next
        if node.next is not None:
            node.next = pointnext.next
            print(node.next.label)
        else:
            node.next = None
        point = pointnext
    return root

#测试
head = RandomListNode(1)
head.next = RandomListNode(2)
head.next.next = RandomListNode(3)
head.next.next.next = RandomListNode(4)
head.next.next.next.next = RandomListNode(5)
head.random = head.next.next
head.next.random = head.next.next.next
head.next.next.random = head.next.next.next.next

root = Clone(head)
while root:
    #print(root.label)
    root = root.next