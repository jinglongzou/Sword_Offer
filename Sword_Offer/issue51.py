# -*- coding:utf-8 -*-
# 给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
# 其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。
# 不能使用除法。

# 这里的B[i]是有数组A中除了A[i]元素的所有元素乘积
# 将B[i]分成两个部分来计算，一个是<i,一个大于i
class Solution:
    def multiply(self, A):
        # write code here
        n = len(A)
        if n <=1:
            return [1]
        B = [1] * n
        #先计算小于i的部分
        for i in range(1,n):
            B[i] = B[i-1]*A[i-1]
        #再计算大于i的部分
        C = [1] * n
        for i in range(n-2,-1,-1):
            C[i] = C[i+1] * A[i+1]
        for i in range(n):
            B[i] = B[i]*C[i]
        return B
