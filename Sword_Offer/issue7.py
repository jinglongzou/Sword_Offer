# -*- coding:utf-8 -*-

# 7 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。

class Solution:
    def Fibonacci(self, n):
        # write code here
        if n <=1 :
            return n
        a = 0
        b = 1
        for i in range(2,n+1):
            c = a + b
            a,b = b,c
        return c