# -*- coding:utf-8 -*-

# 一个整型数组里除了两个数字之外，其他的数字都出现了两次。
# 请写程序找出这两个只出现一次的数字。

# 输入：一个数组（一个列表）
# 输出：找出数组中只出现一次的数字

# 考察算法技巧，如何使得时间复杂度更小;考察位运算，逻辑运算的应用；

# 暴力法：借助字典，遍历并计数每个数字出现的次数，然后遍历字典返回计数为1的数字，时间复杂度为O(n)

# 异或法，由于题强调了两个数字出现一次，其他都出现两次,因此对数字异或后只有出现一次的数字为1.
# 异或法实现的思路：
# 1、对于出现两次的元素，使用“异或”操作后结果肯定为0，
# 那么我们就可以遍历一遍数组，对所有元素使用异或操作，
# 那么得到的结果就是两个出现一次的元素的异或结果。
# 2、那么就可以从异或结果中为1的那一位（这个为1的位是这两个出现一次数字的某个位异或得到的），
# 根据这个位将两个出现一次的数字分到两个子数组中
# 3、再次对每个子数组异或就得到了这两个出现一次的数字
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        #return filter(array.count, array)
        tmp = 0
        # 遍历做异或处理

        for i in array:
            tmp ^= i
        # 找异或结果中为1的位
        idx = 0
        flag = 1
        while ((tmp & flag) == 0):
            flag = flag << 1
        # 找出出现一次的数字
        a = b = 0
        for i in array:
            if ((i & flag) == 0):
                a ^= i
            else:
                b ^= i
        return [a, b]
        '''
        if not array:
            return []
        # 对array中的数字进行异或运算
        tmp = 0
        for i in array:
            print(tmp, )
            tmp ^= i
            print(i,tmp)
        # 获取tmp中最低位1的位置
        idx = 0
        while (tmp & 1) == 0:
            tmp >>= 1
            idx += 1
        a = b = 0
        for i in array:
            if self.isBit(i, idx):
                a ^= i
            else:
                b ^= i
        return [a, b]
        
    def isBit(self, num, idx):
        """
        判断num的二进制从低到高idx位是不是1
        :param num: 数字
        :param idx: 二进制从低到高位置
        :return: num的idx位是否为1
        """
        num = num >> idx
        return num & 1
        '''
#  测试
#array = [2,4,3,6,3,2,5,5]
array = [2,3,3]
s = Solution()
print(s.FindNumsAppearOnce(array))