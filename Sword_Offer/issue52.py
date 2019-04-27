# -*- coding:utf-8 -*-

# 请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，
# 而'*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有
# 字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配

# 考察字符串操作，匹配,

'''
做字符串匹配的基础是逐个比较字符；
字符串匹配算法的设计关键：①怎样选择开始比较的字符对？②发现了不匹配后，下一步应该怎么做？
这两个不同的处理策略就获得了，不同匹配算法；

朴素匹配算法：
设置一个头指针、一个尾指针
①尾指针从左到右逐个字符匹配；②当发现不匹配时，尾指针转而考虑下一个字符，并修改尾指针为头指针；
③当完全匹配时，保存一个[头指针,尾指针]对，并将头指针改为尾指针的下一个位置，尾指针改为头指针；
直达尾指针或者头指针访问完所有位置。
KMP匹配算法：
在原来的朴素匹配算法中，由于重复匹配了某些目标串的字符，有回溯，
因此效率低，KMP算法，就是跳过哪些不匹配的字符，避免回溯。
KMP算法的基本思想是不回溯。如果模式串的里P[i]匹配某个T[j]时失败了，就找某个特定的P[k](0<=k<i),
用模式串中的P[k]来和目标串中的T[j]比较.
##############################################
难点：这里的k如何找，它有什么特点？
这里的k使得P[0:k] 与P[i-k:i]完全匹配，所以模式串中的每个位置的都找一个这样的k,然后更新模式串，就向前移动i-k位；
为了避免跳过可能的匹配，移动的距离尽可能短，因此k应该使P[0:i]中的P[0:k]尽可能长；
这个问题可以转化为找最长公共前后缀，一个字符串的前缀和另一个字符串的后缀完全匹配，并且最长；
备注：python列表的切片表示是右开区间；
这里基于递推的来计算最长相等前缀的长度：假设对P[:i]的最长前缀为pnext[i-1]=k-1,这时就可以分为两种情况:
    ①P[i] = P[k],那么P[0:i+1]的最长相等前缀长度就为k,即pnext[i] = k
    ②不等，则P[0:i]的最长相等前缀移过来继续检查。
实现：
    已知pnext[0] = -1,和pnext[:i],求pnext[i]的算法：
    ①已知pnext[i-1] = k-1,若P[i] = P[k],那么P[0:i+1]的最长相等前缀长度就为k,即pnext[i] = k，将i加1继续循环
    ②不等，由于此时的k是大于pnext[k]的，所以将k设置为pnext[k] 的值
    （也就是转去考虑前一个保证更短保证匹配的前缀，可以基于它继续检查）
    缩短前缀字符，那就要再次检查索引为pnext[k]的字符是否与P[i]匹配；
    ③如果k的值等于-1，那么P[0],....,P[i]的最长前缀长度为0，设置pnext[i] = 0,将i加1继续循环
        def gen_pnext(pattern):
            # 生成针对pattern中各位置i的下一个检查位置
            index, nextpos, length = 0, -1, len(pattern)
            pnext = [-1]*length
            while(index < length-1):
                if nextpos == -1 or pattern[index] == pattern[nextpos]:
                    index,nextpos = index + 1,nextpos + 1
                    pnext[index] = nextpos
                else: #转到检查索引为pnext[nextpos]的字符是否与P[i]匹配；
                    nextpos = pnext[nextpos]
            return pnext
还可以优化这个算法：由于模式串和目标串匹配失败时，P[i] 不等于T[j]，假设pnext[i] = k,如果
                    发现P[i] = P[k],那么一定也有P[i] 不等于T[j],
                    所以这种情况下模式子串应该右移到pnext[k],
                    下一步应该用索引为pnext[k]的字符与T[j]比较；
        def gen_pnext(pattern):
            # 生成针对pattern中各位置i的下一个检查位置
            index, nextpos, length = 0, -1, len(pattern)
            pnext = [-1]*length
            while(index < length-1):
                if nextpos == -1 or pattern[index] == pattern[nextpos]:
                    index,nextpos = index + 1,nextpos + 1
                    if pattern[index] == pattern[nextpos]:
                        pnext[index] = pnext[nextpos]
                    else:
                        pnext[index] = nextpos
                else: #转到检查索引为pnext[nextpos]的字符是否与P[i]匹配；
                    nextpos = pnext[nextpos]
            return pnext
#####
因此，匹配失败时就把模式串前移若干位，用模式串里匹配失败字符之前的某个字符与目标字符串中匹配失败的字符比较，
也就是更新模式串中与目标串当前字符比较的字符；

要实现这种策略，关键在于确定匹配失败时模式串如何前移。
在P[i]匹配失败时，所有的P[k] ( 0<= k < i) 都已经成功匹配。也就是说在目标串T的前前i个字符和模式串的前i个字符相同；
因此原本通过目标串决定模式串前移的位置，可以直接通过模式串本身来决定，通过找出0~（i-1）字符的最长公共前后缀的长度，
来决定模式串前移的长度k,也就是用0~（i-1）字符的第k+1个字符和目标串的当前字符比较；
实现：
        def matching_KMP(pattern,text):
            #计算模式串的每一个位置的匹配失败的移动参数
            pnext = gen_pnext(pattern)
            pindex = 0
            tindex = 0
            plen = len(pattern)
            tlen = len(text)
            #当遍历完目标串，或者找到一个匹配就退出
            while pindex < plen and tindex < tlen:
                if pindex == -1 or text[tindex] == pattern[pindex]:
                    pindex,tindex = pindex + 1,tindex + 1
                else: #当不匹配时就移动模式串，更新模式串中与当前目标串字符比较的字符
                    pindex = pnext[pindex]
            if pindex == plen:# 找到一个匹配串
                return tindex - plen
            return -1
#################################################################################################################################
小结：
朴素匹配算法的关键点：每次匹配失败，就将模式串向前移动一个字符
（也就是将目标串的索引设置为tindex-pindex+1，模式串的索引设置为0)

kmp匹配算法的关键点：1、每次匹配失败时，就将模式串向前移动pindex-k个字符
                        (也就是将模式串的索引设置为k, 目标串索引不变）；
                    2、而对模式串的每个位置的的k的计算，则通过找一个字符串的的
                        最长前后缀子串算法来确定，k即为最长前后缀子串的长度；
                    3、最长前后缀子串算法，则通过递推算法来实现；初始pnext[0] = -1,
                        然后针对k== -1 or p[k] == p[i]来更新pnext[i+1]的值，
                        因此递推的范围是模式串长度-1，一直到倒数第二个字符；
###################################################################################################################################
'''
# 分析1：错误了
# 匹配结束，要求模式串和目标串的索引都为串长度，否则就不匹配；
#       目标串的每个字符，不仅要与当前的模式串字符比较，还要与模式串的下一个字符比较
#       ①都为空
#       ②一个为空，一个不为空: 目标串为空或者模式串为空
#       ③都不为空：
#           每次检查pattern第二个元素是否为‘*’
#           A: t[i] == p[j] and p[j+1] != '*'，都加1，继续比较
#           B: t[i] == p[j] and p[j+1] == '*',那么检查目标串后续的字符是否等于t[i],等于就匹配，，否则跳出
#           C：p[j] == '.', 那么t[i] == p[j]，那么i,j都加1，
#           D: t[i] != p[j] and p[j+1] == '*'，那么j+1,继续比较
#           E:t[i] != p[j] and p[j+1] != '*'

# 分析2：逐个字符比较，采用递归算法
#       ①p,s的索引都为其长度，True
#       ②s的索引不是其长度，p的索引是其长度,False
#       ③根据第二个字符是否是*来处理:
#           备注：下一个字符不等于'*'要分为两种情况，一种是p[i+1]不存在，因此不等于'*';二是p[i+1] != '*'
#           当模式串存在下一个字符是：
#               当前p[i],t[j],如果p[i+1] =='*',
#                   p[i] == t[j]:
#                       子串前移一个，模式不变，这是接下来比较：t[j+1] == t[j]
#                       子串前移一个，模式串前移两个，这是接下来比较子串的下一个字符和模式串*后面的字符
#                       字符串不动，模式串前移两个，这是子串当前字符不匹配模式串的字符，接下来转而比较模式串*后的字符
#                   p[i] != t[j]:
#                       子串不动，模式串前移两个，这是：接下来比较当前字符与模式串的*后面的字符
#               p[i+1] != '*':
#                   p[i] == t[j]：
#                       接下来比较各自的下一个字符
#                   p[i] != t[j]：False
#           模式串不存在下一个字符：
#                   p[i] == t[j]：
#                       接下来比较各自的下一个字符
#                   p[i] != t[j]：False
##############################################################
# 总结：
#      递归算法关键在于分治，要能够将问题分解为循环子问题；把握住临界点，以邻接点来分解问题；
#      本题的邻接点就是下一个字符是否为'*'，这个决定着下一步比较的字符
#############################################################
class Solution:
    # s, pattern都是字符串
    def match(self,s,pattern):
        def method(s,sidx,pattern,pidx):
            slen,plen = len(s),len(pattern)
            if sidx == slen and pidx == plen:
                return True
            elif sidx != slen  and pidx == plen:
                    return False
            else:
                #接下来分别处理第二个字符是*,不是*的情况
                if pidx + 1 < plen:#也就是模式串存在下一个字符
                    if pattern[pidx + 1] == '*': #为*
                        #当匹配时
                        if (sidx <= slen and pattern[pidx] == '.') or (sidx< slen and s[sidx] == pattern[pidx]):
                            return method(s,sidx,pattern,pidx + 2) or method(s,sidx+1,pattern,pidx) \
                                   or method(s,sidx+1,pattern,pidx + 2)
                        #当不匹配
                        else:
                            return method(s,sidx,pattern,pidx + 2)
                    else:#不为*
                        if sidx < slen and (pattern[pidx] == '.' or s[sidx] == pattern[pidx]):
                            return method(s,sidx+1,pattern,pidx+1)
                        else:
                            return False
                else: #存在下一个字符，也就是说下一个字符不是'*'
                    if sidx < slen and (pattern[pidx] == '.' or s[sidx] == pattern[pidx]):
                        return method(s, sidx + 1, pattern, pidx + 1)
                    else:
                        return False
        sidx,pidx = 0,0
        return method(s,sidx,pattern,pidx)

    def match1(self, s, pattern):
        # write code here
        import re
        flag = re.match("(?:" + pattern + r")\Z",s)
        if flag :
            return  True
        else:
            return False



#测试
#pattern = 'ab*aB*a*'
#s = 'aaa'
s ="a"
pattern =".*"
S = Solution()
print(S.match(s,pattern))
print(S.match1(s,pattern))


def gen_pnext(pattern):
    # 生成针对pattern中各位置i的下一个检查位置
    index, nextpos, length = 0, -1, len(pattern)
    pnext = [-1] * length
    while (index < length-1):
        if nextpos == -1 or pattern[index] == pattern[nextpos]:
            index, nextpos = index + 1, nextpos + 1
            pnext[index] = nextpos
        else:
            nextpos = pnext[nextpos]
    return pnext
def gen_pnext1(pattern):
    # 生成针对pattern中各位置i的下一个检查位置
    index, nextpos, length = 0, -1, len(pattern)
    pnext = [-1] * length
    while (index < length-1):
        if nextpos == -1 or pattern[index] == pattern[nextpos]:
            index, nextpos = index + 1, nextpos + 1
            if pattern[index] == pattern[nextpos]:
                pnext[index] = pnext[nextpos]
            else:
                pnext[index] = nextpos
        else:  # 转到检查索引为pnext[nextpos]的字符是否与P[i]匹配；
            nextpos = pnext[nextpos]
    return pnext
def kmp_match(pattern,text):
    #计算模式串的每一个位置的匹配失败的移动参数
    pnext = gen_pnext(pattern)
    pindex = 0
    tindex = 0
    plen = len(pattern)
    tlen = len(text)
    #当遍历完目标串，或者找到一个匹配就退出
    while pindex < plen and tindex < tlen:
        if pindex == -1 or text[tindex] == pattern[pindex]:
            pindex,tindex = pindex + 1,tindex + 1
        else: #当不匹配时就移动模式串，更新模式串中与当前目标串字符比较的字符
            pindex = pnext[pindex]
    if pindex == plen:# 找到一个匹配串
        return tindex - plen
    return -1
#pattern = 'abcabcacd'
pattern = 'abbcabcaabbcaa'
print(gen_pnext(pattern))
print(gen_pnext1(pattern))
print(pattern,)

'''
   def method1(self,s,pattern):
       slen = len(s)
       plen = len(pattern)
       if slen == 0 and plen == 0: #①
           return  True
       elif pattern == '.*':
           return True
       elif slen != 0 and plen != 0: #③
           sidx,pidx = 0,0
           while(sidx < slen and pidx < plen):
               #首先检查pattern下一个元素是否是'*'
               if s[sidx] == pattern[pidx]:
                   if pidx + 1 < plen:
                       if pattern[pidx +1] == '*': # A
                           pidx += 1
                           temp = s[sidx]
                           sidx +=1
                           while(sidx < slen and s[sidx] == temp  ):
                               sidx +=1
                           pidx +=1
                       else: # B
                           sidx, pidx = sidx + 1, pidx + 1
                   else: # B
                       sidx, pidx = sidx + 1, pidx + 1
               else: #s[sidx] != pattern[pidx]
                   if  pattern[pidx] == '.': # C
                       if pidx + 1 < plen:
                           pidx +=1
                           if pattern[pidx] == '*':
                               sidx +=1
                               while(sidx < slen and s[sidx]): #
                                   s += 1
                               pidx +=1
                           else:
                               sidx,pidx = sidx + 1,pidx + 1
                       else:
                           sidx, pidx = sidx + 1, pidx + 1
                   elif pattern[pidx] == '*': #D
                       pidx +=1
                   else: # E
                       return False
           if sidx == slen:
               if  pidx == plen:
                   return True
               elif pidx + 1 < plen:
                   if pattern[pidx+1] == '*' and pidx + 2 == plen:
                       return True
                   else:
                       return False
               else:
                   if pattern[pidx] == '*':
                       return True
                   else:
                       return False
           else:
               return False
       else:# ②
           if slen != 0: #目标串不为空
               return False
           else:
               if plen < 2 or plen > 2:
                   return False
               else:
                   if pattern[1] == '*':
                       return True
                   else:
                       return False
           return False
   '''