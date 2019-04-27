# -*- coding:utf-8 -*-

# LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,
# 2个小王(一副牌原本是54张^_^)...他随机从中抽出了5张牌,想测测自己的手气,
# 看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！
# “红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....
# LL不高兴了,他想了想,决定大\小 王可以看成任何数字,并且A看作1,
# J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),
# “So Lucky!”。LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,
# 然后告诉我们LL的运气如何， 如果牌能组成顺子就输出true，否则就输出false。
# 为了方便起见,你可以认为大小王是0。

# 输入：56张扑克牌，每一种都有四个
# 输出：模拟抽牌，并检测是否是顺子

# 因此这是一个构建随机数序列的模拟，并检查是否是连续的5个数
# 使用随机函数，从0到13，每个数字出现的概率相同

# 这里已经有五个随机数组成的列表了，因此主要任务是判断是否构成顺子；
# 顺子必然没有对,最大最小之差小于5
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if len(numbers):
            while min(numbers) == 0:
                numbers.remove(0)
            if max(numbers) - min(numbers) <= 4 and len(numbers) == len(set(numbers)):
                return True
        return False



# 测试
#numbers = [1,3,0,5,4]
#numbers = [1,3,0,7,0]
numbers = [0,3,2,6,4]
s = Solution()
print(s.IsContinuous(numbers))