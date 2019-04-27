# -*- coding:utf-8 -*-

# 在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到
# 第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.

# 输入：字符串序列
# 输出：字符索引或者-1 （区分字母大小写）

# 这是一个统计，查找问题，由于需要知道一个字母出现的次数，必然要遍历整个字符串，因此理论最低的时间复杂度是O(N)
# 可以通过字典来{字母：[次数，索引]}，统计遍历，返回索引最小的次数为1的字符索引

# 快捷方法： return s.index(list(filter(lambda c:s.count(c)==1,s))[0]) if s else -1
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if s == '':
            return -1
        dicts = {}
        n = len(s)
        ret = s[0]
        for i in range(n):
            if s[i] not in dicts.keys():
                dicts[s[i]] = [1,i]
            else:
                dicts[s[i]][0] +=1
        ret = -1
        for value in dicts.values():
            if value[0] == 1:
                if ret == -1:
                    ret = value
                else:
                    if ret[1] > value[1]:
                        ret = value
        return ret[1]
# 测试
s = 'google'
S = Solution()
print(S.FirstNotRepeatingChar(s))