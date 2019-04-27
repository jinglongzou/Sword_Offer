
# -*- coding:utf-8 -*-

# 1 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
#   每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，
#   判断数组中是否含有该整数。

# 从二维数组的左下角或者右上角开始；
# 从右上角：如果key大于当前值，那么行就加1；小于当前值，列就减1
# 特殊情况：列表为空
class Solution:
    def method1(self,target,array):
        # write code here
        if array == []:
            return False
        m = len(array)
        n = len(array[0])
        # 从左下角开始
        i = m-1
        j = 0
        while (i < m and j >= 0):
            if array[i][j] > target:
                i -= 1
            elif array[i][j] < target:
                j += 1
            else:
                return True
        return False
    # array 二维列表
    def Find(self,target, array):
    # write code here
        if array == []:
            return False
        m = len(array)
        n = len(array[0])
        # 从右上角开始
        i = 0
        j = n - 1
        while(i < m and j >=0):
            if array[i][j] > target:
                j -=1
            elif array[i][j] <target:
                i +=1
            else:
                 return True
        return False
s = Solution()
array = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
target = 15
ret = []
ret.append(s.method1(target,array))
ret.append(s.Find(target,array))
print(ret)