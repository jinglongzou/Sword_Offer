# -*- coding:utf-8 -*-

# 牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。
# 同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。
# 例如，“student. a am I”。后来才意识到，这家伙原来把句子单词的顺序翻转了，
# 正确的句子应该是“I am a student.”。Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？

# 只是翻转了单词的顺序,因此在遇到空白时返回一个单词，并调整单词的位置
# 这里有一个问题就是，当空白比较多时，该怎么处理？
#
class Solution:
    def ReverseSentence(self, s):
        # write code here
        n = len(s)
        L = n - 1
        R = n
        strs = ''
        while (L > 0):
            if s[L].isspace() == True: #遇到空白，可以返回一个单词了
                strs = strs + s[L + 1:R] + ' '
                R = L
                L -=1
            else:
                L -= 1
        strs = strs + s[L:R]
        return strs
        '''
        temp = list(s.split())
        temp.reverse()
        return ' '.join(temp)
        '''


# 测试
s = "student. a am I"
S = Solution()
print(S.ReverseSentence(s))
