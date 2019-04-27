# -*- coding:utf-8 -*-
# 输入一个字符串,按字典序打印出该字符串中字符的所有排列。
# 例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有
# 字符串abc,acb,bac,bca,cab和cba。

# 输入描述:
# 输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
# 输出描述：
# 输出所有可能的字母排列，并且按照字典序输出
'''
分析：考察字符的"字典序"概念，指的是从左到右以及对应位置字母的顺序来比较词汇的顺序。
      考察排列组合的数学知识：对这里的字符应该按照排列来进行处理;
      考察全排列实现算法：递归法，回溯法
      同时由于有字符重复，这增加了难度，也就是相同的两个字母，在不同的位置，交换后仍是同一个词。
      疑问：如何处理重复字符的情况？

      由于按照字典序输出，因此可以先拍序字符，然后再排列
《《不考虑去除重复》》
采用递归的思想：
    先固定第一个字母，全排列剩余字母；固定第二个字母，全排列剩余字母；.....；因此是递归调用算法,
    当只剩下一个字母时，确定一种输出；由于是要在到最后一个字母时，返回一种排列，
    所以每次需要传入整个字母列表，这样才能在最后返回一种排列；同时由于每一次递归操作的字母都比前一层递归少一个字母，
    因此通过更改索引，来确保每次递归操作的字母范围；

非递归思想：
    非递归全排列算法的基本思想是:依据字典序的大小比较规则来建立每一排列
    1.找到所有排列中最小的一个排列P.
    2.找到刚刚好比P大比其它都小的排列Q,
    3.循环执行第二步,直到找到一个最大的排列,算法结束.

采用回溯法的思想：

《《考虑去除重复》》
'''
import itertools
class Solution:
    def Permutation(self,ss):
        def PermutationHelper(List,stack,start,end):
            if start == end:
                stack.append(''.join(List))
                return
            for i in range(start,len(List)):
                if start != i and List[start] == List[i]:
                    continue
                else:
                    List[start],List[i] = List[i],List[start]
                    PermutationHelper(List,stack,start+1,end)
                    List[start], List[i] = List[i], List[start]  #还原，确保for循环中每一次的初始状态相同
            return

        n = len(ss)
        stack = []
        if n < 1:
            return stack
        List = sorted(list(ss))
        PermutationHelper(List,stack,0,n-1)
        #print(stack)
        return sorted(stack)

    def Permutation_not_recursive(self,ss):
        n = len(ss)
        s = [] #用来存所以的排列
        #对字符数为零
        if n < 1:
            return s
        #对字符数不为零，用非递归算法
        L = sorted(list(ss)) #转换字母为列表，从而方便排序
        #接下来从最小的排列到最大的排列：当找不到左边的字符比右边的字符小时，就已经排列玩所以的可能了
        s.append(''.join(L))
        if n < 2:
            return s
        '''
        while(True):
            frontpos = n-2
            while(frontpos>=0 and L[frontpos] > L[frontpos+1]):
                frontpos -=1
            if frontpos < 0:
                break
            endpos = n-1
            while(L[frontpos] > L[endpos]):
                endpos -=1
            L[frontpos], L[endpos] = L[endpos], L[frontpos]
            temp = L[frontpos + 1:]
            temp.reverse()
            L[frontpos + 1:] = temp
            s.append(''.join(L))
        return s
        '''
        while(True):
            frontpos = n - 1
            #找到
            while(frontpos >=1 and L[frontpos-1] >= L[frontpos]):
                frontpos -=1
            #判断是否是最大的排列
            if frontpos == 0:
                break
            #找到
            endpos = frontpos
            frontpos -=1
            while (endpos < n  and L[endpos] > L[frontpos]):
                endpos +=1
            endpos -=1
            L[frontpos],L[endpos] = L[endpos],L[frontpos]
            temp = L[frontpos+1:]
            temp.reverse()
            L[frontpos+1:]=temp
            s.append(''.join(L))
        return s


# 测试
if __name__ == '__main__':
    ss = 'aabc'
    S = Solution()
    s_set = S.Permutation(ss)
    print(s_set)

    s = S.Permutation_not_recursive(ss)
    print(s)
'''
        s_set = []
        if len(ss) < 2:
            return  list(ss)
        s = list(ss)
        s.sort()
        n = len(s)
        temp = s[:]
        for i in range(n):
            strs = ''.join(temp)
            if strs not in s_set:
                s_set.append(strs)
            print(strs)
            for j in range(n-1,1,-1):
                temp[j],temp[j-1] = temp[j-1],temp[j]
                strs = ''.join(temp)
                if strs not in s_set:
                    s_set.append(strs)
                print(strs)
            if i+1 < n:
                s[0],s[i+1] = s[i+1],s[0]
                temp = s[:]
            s
        return  s_set
'''


