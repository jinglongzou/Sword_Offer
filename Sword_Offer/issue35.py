# -*- coding:utf-8 -*-

# 在数组中的两个数字，如果前面一个数字大于后面的数字，
# 则这两个数字组成一个逆序对。输入一个数组,求出这个数
# 组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007

# 输入：一个人数字序列
# 输出：逆序对数对1000000007的余数

# 需要求出每一个数字的逆序对数，查找的方法:就是从该数开始向前遍历，统计比它大的数；时间复杂度是O(n^2),这是暴力解法
# 改进算法，利用分治归并排序算法来统计逆序对数；

# 在归并的过程中统计逆序对数
class Solution:
    def InversePairs(self, data):
        # write code here
        ret = 0
        n = len(data)
        for i in range(n):
            for j in range(i-1,-1,-1):
                if data[i] < data[j]:
                    ret +=1
        return ret%1000000007
    def InversePairs_merge(self,data):
        def merge(data, temp, start, mid,end):
            count = 0
            left_rear = mid
            right_rear = end
            rear = end  # 合并列表的尾指针
            while (left_rear >= start and right_rear > mid):
                if data[left_rear] > data[right_rear]:
                    count = count + right_rear - mid
                    temp[rear] = data[left_rear]
                    left_rear -= 1
                    rear -= 1
                else:
                    temp[rear] = data[right_rear]
                    right_rear -= 1
                    rear -= 1
            while (left_rear >= start):
                temp[rear] = data[left_rear]
                left_rear -= 1
                rear -= 1
            while (right_rear > mid):
                temp[rear] = data[right_rear]
                right_rear -= 1
                rear -= 1
            data[start:end+1] = temp[start:end+1]
            return count
        def merge_sort(data,temp,start,end):
            if start >= end :
                return 0
            mid = (start + end) // 2
            left = merge_sort(data,temp,start,mid)
            right = merge_sort(data,temp,mid+1,end)
            count = merge(data, temp, start, mid,end)
            count = left + right + count
            return count
        n = len(data)
        temp = [0]*n
        start = 0
        end = n-1
        count = merge_sort(data, temp, start, end)
        return count

# 测试
#data = [1,2,3,4,5,8,7,0]
data = [364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]
s = Solution()
print(s.InversePairs_merge(data))