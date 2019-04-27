# -*- coding:utf-8 -*-
# 求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case
# 等关键字及条件判断语句（A?B:C）。

# 其实只要先看我们手里有什么牌就能一步一步想到利用短路特性了
# 我们手里现在可以使用（按优先级高低）单目运算符：++和--,双目运算符：+,-，移位运算符<<和>>，
# 关系运算符>,<等，逻辑运算符and，or,not,位逻辑运算符&,|,^，赋值=，单目和双目的作用是一样的，移位显然没有规律性，
# 因为一个二进制位并不能区分某个数和其他数，这也就排除了&,|,^,因为不需要做位运算了；
# 关系运算符要和if匹配，但这是不行的，这时看看剩下的运算符只能选&&,||了
# 如果做过Java笔试题，会对这两个运算符非常敏感，他们有短路特性，前面的条件判真（或者假）了，
# 就不会再执行后面的条件了，这时就能联想到--n,直到等于0就能返回值

# 法1：利用逻辑运算符的特性，来实现递归的退出
# and:	x and y	布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。
# or:   x or y	布尔"或"	- 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值。
# not:	not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。

# 注意：递归的层数不能太大(<3000)，太大就会超过递归的限度

# 法2：使用构造函数
# 使用虚函数来构造递归，在基类种定义虚函数Sum(n)返回0，通过将指针数组的两个元素分别绑定到基类和派生类，
# 其中基类的Sum() 结束递归，!!n来构造true(1) false(0)来对指针数组进行访问
class Solution:
    def Sum_Solution(self, n):
        # write code here
        ans = n
        temp = ans and self.Sum_Solution(n - 1)
        ans = ans + temp
        return ans

# 测试
n = 3000
s = Solution()
print(s.Sum_Solution(n))
