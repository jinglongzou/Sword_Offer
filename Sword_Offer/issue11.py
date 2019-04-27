# -*- coding:utf-8 -*-

# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

# 考察二进制编码：原码、反码、补码
# 计算机中数据的存储形式是反码
# 位运算符：
class Solution:

    def NumberOf1(self,n):
        count = 0
        if n<0:
            n = n &0xFFFF # 限定位数
        while(n):
            count +=1
            n = (n-1)&n
        return count

# 测试
s= Solution()
n = -1
print(s.NumberOf1(n))