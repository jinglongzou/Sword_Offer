# -*- coding:utf-8 -*-

# 6 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
#   例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
#   NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

# 考虑特殊情况，完全单调增，则第一个元素就是最小值；
# 考虑全面
# 利用循环链表就很好实现
# 对于一个数组需要，找突变的元素
# 数组旋转：
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        n = len(rotateArray)
        if n == 0:
            return 0
        if n == 1:
            return rotateArray[0]

        i = 0
        while (i < n-1): #这里要小于n-1，避免i+1超出索引
            if rotateArray[i] <= rotateArray[i + 1]:
                i += 1
            else:
                break
        if i == n-1:
            return  rotateArray[0]
        else:
            return rotateArray[i + 1]


a = [1,2,3, 4, 5]
s = Solution()
print(s.minNumberInRotateArray(a))