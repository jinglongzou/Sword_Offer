# -*- coding:utf-8 -*-

# 将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，
# 但是string不符合数字要求时返回0)，要求不能使用字符串转换整数的库函数。
# 数值为0或者字符串不是一个合法的数值则返回0。

# 考察综合能力：能够分析边界条件、是否熟悉ASII码
# 分析边界条件：
    # 数据上下 溢出
    # 空字符串
    # 只有正负号
    # 有无正负号
    # 错误标志输出

class Solution:
    def method1(self,s): #借助乘法来实现
        n = len(s)
        if n == 0:
            return 0
        ret = 0
        flag = 1
        if s[0] == '-':
            flag=-1
        start = 0
        if s[0] in ['-','+']:
            start = 1
        for i in range(start,n):
            if s[i]<'0' or s[i] >'9':
                return 0
            ret = ret * 10 + int(s[i])
        return flag*ret




    def StrToInt(self, s):
        # write code here
        if s == '':
            return 0
        ret = 0
        if s[0] == '-':
            flag = -1
        if s[0] in ['+', '-']:
            for i in range(1, len(s)):
                if s[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    return 0
            if len(s) == 1:
                return 0
            return int(s)
        else:
            for i in range(len(s)):
                if s[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    return 0
            return int(s)

# 测试

s = '123'
S = Solution()
print(S.method1(s))
print(S.StrToInt(s))
