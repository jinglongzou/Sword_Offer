# -*- coding:utf-8 -*-
# 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

# 考察一个考虑是否全面的问题：
# 分别对exponent 的情况，对base的情况进行组合考虑
class Solution:
    def Power(self, base, exponent):
        # write code here
        import math
        return math.pow(base,exponent)