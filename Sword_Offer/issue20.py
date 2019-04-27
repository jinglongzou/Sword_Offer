# -*- coding:utf-8 -*-

# 定义栈的数据结构，请在该类型中实现一个能够得到栈中
# 所含最小元素的min函数（时间复杂度应为O（1））。

# 考察栈的概念、建立、O(1)时间复杂度：则要求要么是顺序表存储，要么是单独一个变量
# 因此构建一个变量来存储最小值，并在，插入和删除时维护最小值

# 构建一个辅助栈来存储最小值，这样出入栈、返回最小值都是O(1);利用空间换取时间
class Solution:
    def __init__(self):
        self.s = []
        self.s_ = []
    def push(self, node):
        # write code here
        least = self.min()
        if not least or node < least:
            self.s_.append(node)
        self.s.append(node)
    def pop(self):
        if self.s:
            elem = self.s.pop()
            least = self.min()
            if elem == least:
                self.s_.pop()
        # write code here
    def top(self):
        if self.s:
            return self.s[-1]
        # write code here
    def min(self):
        if self.s_ != []:
            return self.s_[-1]
        # write code here