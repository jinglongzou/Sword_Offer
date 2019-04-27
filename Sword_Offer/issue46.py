# -*- coding:utf-8 -*-

# 每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,今年亦是如此。
# HF作为牛客的资深元老,自然也准备了一些小游戏。其中,有个游戏是这样的:首先,
# 让小朋友们围成一个大圈。然后,他随机指定一个数m,让编号为0的小朋友开始报数。
# 每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,
# 并且不再回到圈中,从他的下一个小朋友开始,继续0...m-1报数....这样下去....
# 直到剩下最后一个小朋友,可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。
# 请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)

# 输入：人数、次序
# 输出：编号

# 考察循环链表，约瑟夫环
# 解法1：循环前进m
# 解法2：通过循环链表模拟
# 解法3：利用约瑟夫环的递归公式
#

class Solution:
    def method1(self,n,m): #每次都前进m个，当前进n次后得到的就是最终的编号
        if n == 0:
            return -1
        s = 0
        for i in range(2, n + 1):
            s = (s + m) % i
        return s
    def LastRemaining_Solution(self, n, m):
        # write code here
        kids = [i for i in range(n)]
        count = n #计数还还在的小孩
        index = -1 #索引
        while(count > 1):
            i = 0
            while(i < m):
                index = (index+1) % n
                if kids[index] != -1:
                    i +=1
            kids[index] = -1
            count -=1
        for i in range(n):
            if kids[i] != -1:
                return kids[i]
        return -1
# 测试
n = 199
m = 205
s = Solution()
print(s.method1(n,m))
print(s.LastRemaining_Solution(n,m))