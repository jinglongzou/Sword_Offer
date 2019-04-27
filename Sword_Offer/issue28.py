# -*- coding:utf-8 -*-
# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
# 例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
# 由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。
# 如果不存在则输出0。

# 查找超过一半的众数
# 输入：一个装有数据序列的列表
# 输出：超过半数的数字或者0

# 分析：如何查找超过半数的数字？
# 由于要判断是否有数字超过半数，因此必然要遍历所有数字，所以最低时间复杂度为O(n)
# 尝试：
#   ①遍历并计数，这需要借助辅助结构存储数字和它的次数，然后比较；
#   ②当一定存在时，排序后取中位数，在统计该数字的数量；
#   ③找中位数，并统计中位数的次数；

#采用方法①
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        dict = {}
        for no in numbers:
            if not dict.has_key(no):
                dict[no] = 1
            else:
                dict[no] = dict[no] + 1
            if dict[no] > len(numbers)/2:
                return no
        return 0