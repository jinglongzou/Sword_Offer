# -*- coding:utf-8 -*-
# 数组中的重复数字
# 在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，
# 但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个
# 重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。

# 找重复数字，遍历，当遇到重复数字就退出：
# 法1：遍历，并将借助一个标记列表，当遇到数字的标记不为None，（或者字典，这样适用范围更广些）就退出返回
# 法2：分析题，由于长度为n,且数字都在范围0~n-1，因此可以基于数组中数字所指的位置来，标记数字是否访问；
    # 在本数组上标记已经访问过的数字，将访问过的数字所对应的位置的数加n;
    # 通过遍历一遍数组，对位置i的数字k所指的位置k的数字num加n,当再次遇到数字k时，
    # 发现位置k的数字大于等于n,则返回数字k;
    # 要注意的是，对每一个位置的数字需要先做一个判断是否大于等于n，大于就要先减n，
    # 恢复，该位置本来的数字。
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def method1(self,numbers,dumplicaion):#利用原来数组
        n = len(numbers)
        for i in range(n):
            temp = numbers[i]
            if temp >= n: #这里要加上等于号是因为当数字为零的情况
                temp = temp -n
            if numbers[temp] > n:
                return True,temp
            numbers[temp] +=n
        return False
    def method2(self,numbers,duplication): #利用字典
        dict = {}
        for i in range(len(numbers)):
            if numbers[i] in dict.keys():
                duplication[0] = numbers[i]
                return True
            dict[numbers[i]] = 1
        return False
    def duplicate(self, numbers, duplication):#利用列表
        # write code here
        L = [None]*len(numbers)
        for i in range(len(numbers)):
            p = numbers[i]
            if L[p] is not None:
                duplication.append( numbers[i])
                return True,duplication[-1]
            L[numbers[i]] = 1
        return False

# 测试
#numbers = [2,1,3,1,4]
numbers = [2,1,3,0,4]#[2,4,3,1,4]
number = [2,4,3,1,4]
dump = []
s = Solution()
print(s.method1(numbers,dump))
print(s.duplicate(number,dump))