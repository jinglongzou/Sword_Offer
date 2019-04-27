# -*- coding:utf-8 -*-

# 写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。

# 考察位运算符
class Solution:
    def Add(self, num1, num2):
        # write code here
        while(num1&num2):
            a = num1 ^ num2
            b = (num1 & num2) << 1
            num1 = a
            num2 = b
        return num1
# 测试
num1 = -1
num2 = 1
s = Solution()
print(s.Add(num1,num2))
