# -*- coding:utf-8 -*-

# 把只包含质因子2、3和5的数称作丑数（Ugly Number）。
#例如6、8都是丑数，但14不是，因为它包含质因子7。
# 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。


# 考察：这是一个规律发现题，找到规律并实现就可以了
#       那么发现规律的方法：归纳法，类比法，推理法

# 我的第一感觉是通过生成器来做，但是看了别人的有列出全部丑数来取的，有通过循环逐步迭代到第N个丑数

# 每一个丑数都可以通过：2^m * 3^n * 5^k 来表示，第一个丑数为1，可以迭代乘以2,3,5，得到2，3,5，然后每个数
# 在分别乘以2,3,5得到：4,6,10,6,9,15,10,15,25，这样有重复
# 因此将乘以2,3,5 得到的数分别放在三个队列里，每次将队首最小的数加入，丑数序列
# arr=[1]
# q2 = [2]
# q3 = [3]
# q5 = [5]
# arr =[1,2],因此q2的队首元素变成了2，下一次用2乘的话就乘以arr中的2，下一次用3乘的话就乘以arr中的原来的1，下一次用5乘的话就乘以arr中的原来的1；
# 实现方法是：通过指针来维护arr中每次乘以2,3,5的数的位置，生成一个丑数后，只移动对应乘数的arr指针
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 7:
            return index
        arr = [1]
        q2 = 0
        q3 = 0
        q5 = 0
        while(len(arr) < index):
            elem = min(arr[q2]*2,arr[q3]*3,arr[q5]*5)
            arr.append(elem)
            if elem == arr[q2] * 2: q2 += 1
            if elem == arr[q3] * 3: q3 += 1
            if elem == arr[q5] * 5: q5 += 1
        return arr[index-1]

# 测试
index = 10
s = Solution()
print(s.GetUglyNumber_Solution(index))
