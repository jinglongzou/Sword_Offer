# -*- coding:utf-8 -*-

# 给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
# 例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，
# 他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
# {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}，
# {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。

# 考察：队列的灵活使用，以及维护队列中单调关系的规则：将新加入元素和队尾元素比较，确保新加入元素是队列中最小的；
# 这是一个滑动窗，来找数据的题；滑动窗应用：TCP协议中、信号处理中、图像处理中都有用到
# 关键在于滑动窗起点和终点索引的变化，因此设置一个start_idx,end_idx来表示滑动窗，
# 其中end_idx - start_idx = size-1
# 输入：
#       数组，窗大小
# 输出：一个窗移动过程中的最大值形成的列表，当数组为空时，返回空；
# 考虑可能情况：size大于等于数组的大小；size小于数组的大小；数组为空；size == 0;

# 实现：对每个窗口都求一次最大值，那么时间复杂度是O((n-1)*size),空间复杂度O(1)
# 优化：由于滑动窗，每次只前进一个数值，因此如果前一窗口下的最大值还在当前窗口，
# 那么就和当前新加入的值比较一下，获得当前窗口最大值；窗口左端比新加入数据小，
# 那么它就不可能是最大值了，因此可以提前删除，减少比较次数

# 思考利用队列来解决问题,只需要遍历一次就找出各窗口下的最大值
# 构建一个队列，这个队列里的元素，队首是索引最小，且是当前窗口最大的元素；队列对单调递减的；

# 法2：O(n)时间复杂度
class Solution1:
    def maxInWindows(self, num, size):
        # write code here
        n = len(num)
        ret = []
        if n == 0 or size == 0 or n < size:
            return ret
        from collections import deque
        qu = deque()
        for i in range(size):
            while (qu and num[i] >= num[qu[0]]):
                qu.popleft()
            qu.append(i)
        for i in range(size, n):
            ret.append(num[qu[0]])
            # 要注意维护队列中元素为单调递减的
            # 这里要处理三种情况：1、qu[0]索引超过size范围，报废了；2、去除超过范围的元素后，
            # 弹出比新元素小的队首元素；3、去除比新元素小的队尾元素
            while (qu and (i - qu[0] >= size or num[i] >= num[qu[0]])):  # 1、2
                qu.popleft()
            while (qu and num[qu[-1]] <= num[i]):  # 3
                qu.pop()
            qu.append(i)
        ret.append(num[qu[0]])
        return ret
    def maxInWindows(self, num, size):
        # write code here
        n = len(num)
        ret = []
        if n == 0 or size == 0 or n < size:
            return ret
        from collections import deque
        qu = deque()
        for i in range(size):
            while(qu and num[i] >= num[qu[0]]):
                qu.popleft()
            qu.append(i)
        for i in range(size,n):
            ret.append(num[qu[0]])
            # 要注意维护队列中元素为单调递减的
            # 这里要处理两种情况：1、去除比新元素小的队尾元素;2、qu[0]索引超过size范围，报废了,去除队首元素；
            while (qu and   num[i] >= num[qu[-1]]): # 1
                qu.pop()
            while (qu and i - qu[0] >= size): # 2
                qu.popleft()
            qu.append(i)
        ret.append(num[qu[0]])
        return ret

# 法1：O((n-1)*size)
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        n = len(num)
        ret = []
        if n == 0 or size == 0 or n < size:
            return ret
        start_idx = 0
        end_idx = size
        while(end_idx<=n):
            ret.append(max(num[start_idx:end_idx]))
            start_idx +=1
            end_idx +=1
        return ret

# 测试
num = [2,3,4,2,6,2,5,1] #[2,3,4,2,8,2,6,4,5,1,2,4,6]
size = 3
s = Solution1()
print(s.maxInWindows(num,size))