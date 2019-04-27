# -*- coding:utf-8 -*-
# 5 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

# 用两个栈来实现队列：考察队列、栈的特性

# 由于队列要先进先出，因此存在栈中，那就要求先入队的元素，要最后入栈；
# 因此通过将先将入队元素，先加入一个栈，然后再弹出加入另一个栈，这样就构成了队的出队顺序；
# 每次有元素入队时，要先将原本用作队列的栈的里的元素，先压人辅助栈，并进新入队元素压人辅助栈，
# 最后再全部弹出压人代表队列的栈
class Solution:
    def __init__(self ,s1 = [] ,s2 = []):
        self.s1 = s1
        self.s2 = s2
    def push(self, node):
        # write code here
        while self.s2 != []:
            self.s1.append(self.s2.pop(-1))
        self.s1.append(node)
        while self.s1 != []:
            self.s2.append(self.s1.pop(-1))


    def pop(self):
        # return xx
        return self.s2.pop(-1)