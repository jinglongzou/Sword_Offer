# -*- coding:utf-8 -*-

# 输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
# 如果有多对数字的和等于S，输出两个数的乘积最小的。

# 结合上一题经验，同样可以用双指针，一个指小的，一个指大的

# 注意要考虑特殊情况,当考虑一个算法后，就要分析下是否处理了特殊情况
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if array == []:
            return []
        n = len(array)
        low = 0
        high = n-1
        ret = []
        a = tsum
        b = tsum
        while(low < high):
            cur = array[low] + array[high]
            if cur > tsum:
                high -=1
            if cur == tsum:
                if array[low]*array[high] < a*b:
                    a = array[low]
                    b = array[high]
                high -=1
            if cur < tsum:
                low +=1
        if a + b >tsum:
            return []
        else:
            return [a,b]

# 测试
array = [2,3,12,13,5,16,15,8,9,11,4,10,40,32]
array.sort()
tsum = 15
s = Solution()
print(s.FindNumbersWithSum(array,tsum))