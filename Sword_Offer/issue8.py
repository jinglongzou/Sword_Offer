# -*- coding:utf-8 -*-

# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的
# 台阶总共有多少种跳法（先后次序不同算不同的结果）。

# 这个考察就是能够发现规律
class Solution:
    def jumpFloor(self, number):
        if number <=2:
            return number
        a = 1
        b = 2
        while(number > 2):
            c = a + b
            a,b = b,c
            number -=1
        return b