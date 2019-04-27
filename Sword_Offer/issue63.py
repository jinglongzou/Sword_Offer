# -*- coding:utf-8 -*-
# 如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，
# 那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，
# 那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，
# 使用GetMedian()方法获取当前读取数据的中位数。

# 考察：数据流的读取，以及总体数据参数的获取；
# 中位数查找算法：
#   全排序，再查找：
#     普通算法：再分类找中位数查找
#     最佳方法：利用了取反数和为1的特性，通过列表负索引来获得列表中位数：
#     half = len(data//2)
#     mid_data = (data[half] + data[~half]) // 2
#     备注基于：half + (~half) = 1。
#  局部排序，再查找：
#     中位数查找算法转化为查找第 len(data) // 2 大的数,


# 法1：得到所有数据后，来排序来获得中位数
class Solution:
    def __init__(self):
        self.data = []

    def Insert(self, num):
        # write code here
        self.data.append(num)

    def GetMedian(self):
        # write code here
        self.data.sort()
        n = len(self.data)
        mid = n // 2
        return (self.data[mid] + self.data[~mid]) / 2.0
# 法2：维护堆，通过大顶堆、小顶堆来实现
#       将前n/2小的数存在大顶堆，将之后的数存在小顶堆；
#       这样当总个数为奇数时，中位数就是大顶堆的堆顶元素；当为偶数个时，就是两个堆顶元素和的一半
#       对第k个数，k为奇数，要进入大顶堆，那么首先将该数和小顶堆堆顶元素比较，将两者小的加入大顶堆
#       对第k个数，k为偶数，要进入小顶堆，那么首先将该数和大顶堆堆顶元素比较，将两者大的加入大顶堆
import heapq
class Solution1:
    def __init__(self):
        self.bigheap = []
        self.leastheap = []
        self.count = 0

    def Insert(self, num):
        # write code here
        self.count += 1
        if self.count % 2 == 1: #应该加入大顶堆
            if self.leastheap != [] and self.leastheap[0] < num:
                temp =heapq.heappop(self.leastheap)
                heapq.heappush(self.leastheap,num)
                num = temp
            # 由于heapq只实现了小顶堆，大顶堆，通过对数据取反来实现
            heapq.heappush(self.bigheap,-num)
        else: #应该加入小顶堆
            if self.bigheap != [] and -self.bigheap[0] > num:
                temp = -heapq.heappop(self.bigheap)
                heapq.heappush(self.bigheap,-num)
                num = temp
            heapq.heappush(self.leastheap,num)

    def GetMedian(self):
        # write code here
        big = self.bigheap
        least = self.leastheap
        if self.count % 2 == 1:
            return -self.bigheap[0]
        else:
            return (-self.bigheap[0] + self.leastheap[0]) / 2.0
# 测试
s = Solution1()
L = [5,2,3,4,1,6,7,0,8]
for i in L:
    s.Insert(i)
    print(s.GetMedian())