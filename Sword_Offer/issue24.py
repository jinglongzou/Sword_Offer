#-*- coding:utf-8 -*-
# 24
# 输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
# 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
# (注意: 在返回值的list中，数组长度大的数组靠前)

# 这是一种基于栈的深度优先遍历，通过标记来避免重复访问，这和图的遍历有类似之处

# 输入：根节点、整数
# 输出：节点路径

# 关键词：路径、等于整数
# 路径是根节点到叶结点
# 分析：要记录节点路径需要一个列表，对每一路径的求解过程需要一个列表，
# 对到一个节点的时候需要一个数来记录和，方便和整数比较

# 第一种：递归法
#         传入两个列表，一个存所有路径，一个存单条路径；还有一个整数变量，存和
# 第二种:基于栈
# 第三种：基于队列
# 特殊情况：1、根节点为空，返回空
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def method1(self,root,expectNumber):
        all_path = []
        path = []
        def find_path(root,expectNumber,all_path,path):
            if root is None:
                return all_path
            else:
                expectNumber = expectNumber - root.val
                path.append(root.val)
                if expectNumber == 0 and root.left is None and root.right is None:
                    all_path.append(path)
                find_path(root.left,expectNumber,all_path,path)
                find_path(root.left, expectNumber, all_path, path)
                return all_path

        all_path = find_path(root, expectNumber, all_path, path)
        return all_path
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        #定义三个列表：一个用于存储节点和长度，一个用于存储一条路径，一个用于存储所有路径
        s = [] #栈
        path = [] #单条路径
        paths = [] #所有路径
        if root:
            s.append([root,root.val,0])
            path.append(root.val)
            point = root
            while point or s :
                while point:
                    if point.left and s[-1][-1] < 1: #将左子节点入栈
                        point = point.left
                        s[-1][-1] = 1
                        s.append([point,s[-1][1]+point.val,0])
                        path.append(point.val)
                    else:
                        point = None
                point, length, flag = s[-1]
                if point.right: #若右子节点存在，则考虑是否将右子节入栈
                    if s[-1][-1] < 2: #右子节点没有入过栈
                        point = point.right
                        s[-1][-1] = 2 #更改为父节点的标记
                        s.append([point,s[-1][-2] + point.val,0])
                        path.append(point.val)
                    else:#右子节点已经入过栈了
                        s.pop() #清除这个已经处理完左右节点的父节点
                        path.pop()
                        point = None
                else:#右子节点不存在，可以输出一条路径了
                    point,length,flag = s.pop()
                    if length == expectNumber:
                        #temp = path.copy()
                        paths.append(path[:])
                    path.pop()
                    point = point.right
            def lengths(elem):
                return len(elem)
            paths.sort(key = lengths,reverse=True)
            return paths
        else:
            return paths
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(12)
root.left.left = TreeNode(4)
root.left.right = TreeNode(7)

s = Solution()
paths = s.FindPath(root,22)

print(paths)
print(s.method1(root,22))