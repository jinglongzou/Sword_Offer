# -*- coding:utf-8 -*-

# 小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
# 但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
# 没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,
# 你能不能也很快的找出所有和为S的连续正数序列? Good Luck!

# 输入：一个整数值
# 输出：一个连续的整数序列，该序列的和为给定的整数值
#等差数列求和公式:a1*n + n(n-1)*d/2 = sum
# 法1：由于连续，所以d为1,因此公式可以转化为一个关于n的一元二次方程，对不同的a1可以求出对应n,从而得到连续序列
# 法2：n的个数一定小于等于n(n-1)/2 = sum 的解n,因此对这个范围的n遍历求出对应的a1，就可以了
# 法3：双指针技术或者滑动窗口技术
class Solution:
    def FindContinuousSequence(self, tsum): # 等差数列求和公式，固定n
        # write code here
        from math import sqrt, floor
        n_range = int(sqrt(2*tsum)) + 1
        for i in range(n_range,1,-1):
            a = (2*tsum - i*i + i)/(2.0*i)
            tmp = a
            if floor(tmp) == a and a >0:
                a = int(a)
                L = [a + j for j in range(i)]
                print(L)
    def method1(self,tsum): # 滑动窗法
        phigh = 2
        plow = 1
        ret = []
        while(phigh > plow):
            cur = (phigh + plow) * (phigh -plow + 1) / 2
            if cur < tsum:
                phigh +=1
            if cur == tsum:
                L = [i for i in range(plow,phigh+1)]
                ret.append(L)
                plow +=1
            if cur > tsum:
                plow +=1
        return ret
    def method2(self,tsum):# 等差数列求和公式，固定a1
        from math import sqrt, floor
        ret = []
        for i in range(1, tsum):
            tmp = sqrt((2 * i - 1) * (2 * i - 1) + 8 * tsum)
            fl = tmp
            if floor(fl) == tmp:
                tmp = int(tmp)
            else:
                continue
            n = int((1 - 2 * i + tmp) / 2.0)
            L = [i + j for j in range(n)]
            print(L)
            ret.append(L)
            '''
            n = (1 - 2 * i + tmp) / 2.0
            tmp_n = floor(n)
            if tmp_n == n:
                n = int(n)
                L = [i + j for j in range(n)]
                print(L)
                ret.append(L)
            else:
                continue
            '''

        return ret
        #L = [i + j for j in range(n)]
        #if sum(L) == tsum:
            #print(L)

        #return ret
#测试
tsum = 3
s = Solution()
s.FindContinuousSequence(tsum)