# -*- coding:utf-8 -*-

# 统计一个数字在排序数组中出现的次数。

# 这是一个考察查询算法例子：
# 1. 顺序查找：无序查找算法，O(n)时间复杂度
# 2. 二分查找: 有序查找算法，O(logn)时间复杂度；mid = (low + high) / 2
# 3. 插值查找：有序查找算法；基于二分查找算法，将查找点的选择改进为自适应选择，可以提高查找效率。
#              mid = low + (key-a[low]) / (a[high] - a[low]) * (high - low)
# 4. 斐波那契查找: 也是二分查找的一种提升算法，通过运用黄金比例的概念在数列中选择查找点进行查找，
#                  提高查找效率。同样地，斐波那契查找也属于一种有序查找算法。
#                  裴波那契算法要求开始表中记录的个数为某个裴波那契数小1，及n = F(k) -1
#                  开始将k值与第F(k-1)位置的记录进行比较(及mid=low+F(k-1)-1),比较结果也分为三种
# 　　            1）相等，mid位置的元素即为所求
# 　　            2）>，low=mid+1,k-=2;
# 5. 树表查找
# 6. 分块查找
# 7. 哈希查找
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        return data.count(k)
