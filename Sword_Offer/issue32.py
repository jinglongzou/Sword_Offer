# -*- coding:utf-8 -*-

# 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
# 打印能拼接出的所有数字中最小的一个。
# 例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。

# 这也就是要求按照某个规则来排序[3,32,321]使得合并后的数字最小,即对任意相邻的两个数字[a,b]，要求ab < ba，因此获得了新的比较规则，
# 按照这个规则来比较排序，就使得最后合并成的数最小。

# 这就可以利用列表的排序函数，list.sort(),或者sorted()，通过key来传入新的排序规则，来排序列表
#######################################################################################################
# pthon2版本有cmp，可以传入两个参数来设定比较的规则                                                   #
# 由于python3中只有key，且key值接受一个参数，返回一个值；因此要传入两个参数来设定排序规格，就要借助   #
# functools.cmp_to_key(cmp)来将自己写的接受两个参数的cmp规则转化为key可以接受的规则                   #
#######################################################################################################
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        strs_list = [str(i) for i in numbers]
        def cmps(str1,str2):
            s1 = str1 + str2
            s2 = str2 + str1
            if s1 < s2:
                return -1
            elif s1 > s2:
                return 1
            else:
                return 0
        strs_list.sort(cmp=lambda x,y:cmps(x,y) )

        return strs_list



# 测试
a = [3,323,32123]
s = Solution()
strs = s.PrintMinNumber(a)
print(strs)

import operator
import functools
b = ['3','323','32123']
def cmps(str1, str2):
    s1 = str1 + str2
    s2 = str2 + str1
    if s1 < s2:
        return -1
    elif s1 > s2:
        return 1
    else:
        return 0
b.sort(key = functools.cmp_to_key(cmps))
print(b)
