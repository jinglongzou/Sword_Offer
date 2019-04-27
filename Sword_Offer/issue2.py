# -*- coding:utf-8 -*-

# 2 请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，
#   当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

# 基于python字符串函数，可以很方便的替换

# 逐个字符替换：
# 基本思路：由于替换后字符长度变化了，因此需要首先统计空白字符的个数，计算出替换后字符的长度
#           然后从字符末尾开始遍历，不是空白直接加入字符序列，遇到空白就替换为%20,直到首个字符
class Solution:
    def method(self,s):
        if s == '':
            return s
        count = 0
        n = len(s)
        for i in range(n):
            if s[i] == ' ':
                count +=1
        new_n = count*2 + n
        ret = [0 for i in range(new_n)]
        new_idx = new_n -1
        n_idx = n - 1
        while(n_idx >= 0 and new_idx>=n_idx):
            if s[n_idx] == ' ':
                ret[new_idx] = '0'
                new_idx -= 1
                ret[new_idx] = '2'
                new_idx -= 1
                ret[new_idx] = '%'
                new_idx -=1
            else:
                ret[new_idx] = s[n_idx]
                new_idx -=1
            n_idx -=1
        print(ret)
        return ''.join(ret)
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        s = s.replace(' ','%20')
        return s
s = "hello world"
SO = Solution()
print(SO.replaceSpace(s))
print(SO.method(s))