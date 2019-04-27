# -*- coding:utf-8 -*-
# 请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
# 第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。

# 关键词：二叉树，之字形遍历
# 法1：理解：是一种BFS遍历的变种，对每一层都是后进先出，同时不同层还要分割开来，因此用两个栈来实现；
# 每次执行都要等一个栈为空，才执行另一个栈；分为编号为偶数的栈，编号为奇数的栈；
# 终止条件是编号偶数层的栈不为空

# 法2：通过一个双向队列来实现
# 法3：直接实现深度遍历，只是分层存储，在输出的时候，不同的层按照原序或者倒叙输出
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def method2(self,pRoot):#通过一个双向队列来实现，用一个标记符来分层,当遇到None时就变换出队方向
        ret = []
        if pRoot is None:
            return ret
        from collections import deque
        pass

    def method2(self,pRoot):
        # 直接实现深度遍历，只是分层存储，在输出的时候，不同的层按照原序或者倒叙输出
        ret = []
        if pRoot is None:
            return ret
        nodelist = []
        nodelist.append(pRoot)
        while(nodelist):
            newlist = []
            layer = []
            for node in nodelist:
                layer.append(node.val)
                if node.left:
                    newlist.append(node.left)
                if node.right:
                    newlist.append(node.right)
            ret.append(layer)
            nodelist = newlist
        result = []
        for i,v in enumerate(ret):
            if i % 2 == 0:
                result.append(v)
            else:
                result.append(v[::-1])
        return result











    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return None
        s_even = []
        s_odd = []
        s_even.append(pRoot)
        ret = []
        layer = []
        while(s_even):
            while(s_even):
                point = s_even.pop()
                layer.append(point.val)
                if point.left:
                    s_odd.append(point.left)
                if point.right:
                    s_odd.append(point.right)
            if layer:
                ret.append(layer[:])
                layer = []
            while(s_odd):
                point = s_odd.pop()
                layer.append(point.val)
                if point.right:
                    s_even.append(point.right)
                if point.left:
                    s_even.append(point.left)
            if layer:
                ret.append(layer[:])
                layer = []
        return ret
# 测试
pHead = TreeNode(1)
pHead.right = TreeNode(2)
pHead.right.left =  TreeNode(2)

s = Solution()
print(s.Print(pHead))