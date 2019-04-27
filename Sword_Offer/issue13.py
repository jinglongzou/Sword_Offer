# -*- coding:utf-8 -*-
# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
# 使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
# 并保证奇数和奇数，偶数和偶数之间的相对位置不变。

#
class Solution:
    # 法1、法2引用’华科平凡'的解答
    def method1(self, array):
        # write code here
        odd, even = [], []
        for i in array:
            odd.append(i) if i % 2 == 1 else even.append(i)
        return odd + even
    # 借助列表的排序特性，输入新的排序规则
    def method2(self, array):
        return sorted(array, key=lambda c: c % 2, reverse=True)
    def reOrderArray(self, array):
        # write code here
        # 基于插入排序的思路，两个循环
        #第一个循环是列表的大小，第二个循环是找到同类停止
        n = len(array)
        if n <=1:
            return array
        for i in range(n):
            m = array[i] % 2
            if m == 1:
                temp = array[i] #奇数
                j = i
                while(j >0 and array[j-1] % 2 ==0): #将它前面的偶数向后移动
                    array[j] = array[j - 1]
                    j -=1
                array[j] = temp #找到j位置前一个元素为奇数，因此将i元素赋值给j
        return array