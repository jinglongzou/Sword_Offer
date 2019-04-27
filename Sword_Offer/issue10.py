# -*- coding:utf-8 -*-

# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
# 请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，
# 总共有多少种方法？

# 考察递归和迭代，归纳法思想，发现规律
class Solution:
    def rectCover(self, number):
        # write code here
        if number <=0:
            return number
        a = 0
        b = 1
        while(number>0):
            c = a + b
            a,b = b,c
            number -=1
        return b