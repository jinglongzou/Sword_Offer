# -*- coding:utf-8 -*-

# 请实现一个函数用来找出字符流中第一个只出现一次的字符。
# 例如，当从字符流中只读出前两个字符"go"时，
# 第一个只出现一次的字符是"g"。当从该字符流中读出前
# 六个字符“google"时，第一个只出现一次的字符是"l"。

# 复杂度分析：由于查找第一个只出现一次的字符，因此不遍历完索引字符是无法确定某个字符只出现一次的
# 因此最低时间复杂度为O(n)。
# 字符检查，这和在一个数组中找第一个重复的数，是类似的
#第一个重复的字符，那么可以构建一个和字符集同等大小的列表，每个位置标记字符是否访问,以及第一访问的索引
# 遍历字符集，并返回索引最小的只出现一次的字符
# 法1：借助列表，并统计
class Solution1:
    # 返回对应char
    def __init__(self):
        self.Max_num = float('inf')
        self.sets = [[0,self.Max_num]]*256
        self.char_idx = -1
        self.strs = ''
    def FirstAppearingOnce(self):
        # write code here
        min_idx = self.Max_num
        sets = self.sets
        for i in range(256):
            if sets[i][0] == 1:
                if min_idx > sets[i][1]:
                    min_idx = sets[i][1]
        if min_idx != self.Max_num:
            return self.strs[min_idx]
        return '#'
    def Insert(self, char):
        # write code here
        self.char_idx +=1
        self.strs = self.strs + char
        idx = ord(char)
        if self.sets[idx][1] == self.Max_num:
            self.sets[idx] = [1,self.char_idx]
        else:
            self.sets[idx] = [self.sets[idx][0]+1,self.sets[idx][1]]
# 法2：借助队列、列表来统计，将出现一次的字符来入队；
#       解析题意：返回第一个只出现一次的字符：因此要记录或者表征两个关键信息才能找出这样的字符：
#           ①对字符串中的字符需要表征先后顺序；②要记录字符出现的次数；
#           表示顺序：可以索引，可以队列、栈；记录次数：可以设置整数变量来记录；
#       每次返回只出现一些的队首字符；如果队首字符的次数不为1，那么就弹出；
#       当队列为空是就返回#
class Solution:
    # 返回对应char
    def __init__(self):
        from collections import deque
        self.queue = deque()
        self.sets = [0]*256
        self.strs = ''
    def FirstAppearingOnce(self):
        # write code here
        while(self.queue):
            ch = self.queue.popleft()
            idx = ord(ch)
            if self.sets[idx] == 1:
                self.queue.appendleft(ch)
                return ch
        return '#'
        min_idx = self.Max_num
        sets = self.sets
    def Insert(self, char):
        # write code here
        self.strs = self.strs + char
        idx = ord(char)
        self.sets[idx] +=1
        if self.sets[idx] == 1:
            self.queue.append(char)

# 测试
chars = 'google'
s = Solution()
for ch in chars:
    s.Insert(ch)
    print(s.FirstAppearingOnce())