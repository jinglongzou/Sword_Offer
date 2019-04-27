# -*- coding:utf-8 -*-
# 输入两个整数序列，第一个序列表示栈的压入顺序，
# 请判断第二个序列是否可能为该栈的弹出顺序。
# 假设压入栈的所有数字均不相等。例如序列1,2,3,4,5
# 是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应
# 的一个弹出序列，但4,3,5,1,2就不可能是该压栈
# 序列的弹出序列。（注意：这两个序列的长度是相等的）

# 考察出入栈的特性
class Solution:
    def IsPopOrder(self, pushV, popV):
        #借助辅助栈，来重现入栈过程，并与出栈栈顶元素比较；
        # write code here
        s = [] #assistant stack
        n = len(pushV)
        j = 0
        for i in range(n):
            s.append(pushV[i])
            while(j < n and popV[j] == s[-1]):
                s.pop()
                j += 1
        return s == []