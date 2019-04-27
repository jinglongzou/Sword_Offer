# -*- coding:utf-8 -*-

# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
# 如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

# 考察二叉搜索树的概念、遍历，二叉搜索树的根节点小于右子节点，大于左子节点
# 要检查是否是后续遍历的结果，最后一个元素是根节点，那么可以将序列分层两段:
# 一段小于root,一段大于root;前一段小于root,后一段大于root,同时后一段中不存在小于root的元素
# 递归进行就可以了
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if sequence == []:
            return False
        n = len(sequence)
        if n == 1:
            return True
        else:
            root = sequence[-1]
            index = 0
            while(index < n-1): # 找出小于root的前一段 ，如果存在重复的元素，那么可以等于root
                if sequence[index] < root:
                    index += 1
                else:
                    break
            for i in range(index,n-1): #判断后一段是否有元素大于root,如果存在重复的元素，那么可以等于root
                if sequence[i] < root:
                    return False
            left = True
            right= True
            if index >0: # 递归对两段调用函数
                left = self.VerifySquenceOfBST(sequence[:index])
            if index < n -1:
                right = self.VerifySquenceOfBST(sequence[index:n-1])
            return left  and right