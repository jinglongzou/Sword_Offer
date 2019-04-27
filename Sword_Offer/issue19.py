# -*- coding:utf-8 -*-

# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
# 例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
# 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

# 难点：情景分类、边界处理

#  解本题遇到两个问题：
#         当为一维列表时：
#             第二维的大小无法用len计算，因为常数没有len属性
#             无法通过双重索引来引用元素，因为常数没有索引。
#         如何解决二维列表的重复访问的问题：
#             第一维只有一行时，在从左到右遍历完后，避免从右到左再次遍历，
#             因此在从右到左的遍历中需要判断，当前的行号是否与从左到右遍历的的行号相同
#             第二维只有一行时，在从上到下遍历完，避免从下到上再次遍历，
#             因此在从下到上遍历钟需要判断，当前的列号是否与从上到下的遍历的列号相同
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        # 首先计算计算需要循环的圈数
        #一维列表
        if not isinstance(matrix[0],list):
            return matrix
        #二维列表
        else:
            m = len(matrix)
            n = len(matrix[0])
        s = []
        if m >= n:
            circle = (n-1)//2 + 1
        else:
            circle = (m -1)//2 + 1
        for c in range(circle):
            # 从左到右
            i=c
            j=c
            for j in range(c,n-c):
                s.append(matrix[i][j])
            # 从上到下
            print(i,j)
            for i in range(c+1,m-c):
                s.append(matrix[i][j])
            # 从右到左
            print(i,j)
            for j in range(n-c-2,c-1,-1):
                if i == c:
                    break
                s.append(matrix[i][j])
            # 从下到上
            print(i,j)
            print('\n')
            for i in range(m-c-2,c,-1):
                if j==n-c-1 :
                    break
                s.append(matrix[i][j])
        return s

    def method(self, matrix):
            res = []
            while matrix:
                res += matrix.pop(0)
                if matrix and matrix[0]:
                    for row in matrix:
                        res.append(row.pop())
                if matrix:
                    res += matrix.pop()[::-1]
                if matrix and matrix[0]:
                    for row in matrix[::-1]:
                        res.append(row.pop(0))
            return res
