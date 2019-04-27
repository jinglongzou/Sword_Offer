# -*- coding:utf-8 -*-
# 地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，
# 每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐
# 标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够
# 进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），
# 因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

# 考察图的遍历算法：深度优先、宽度优先、递归 、非递归、图的逻辑结构：邻接矩阵、邻接表
# 和上一题类似，采用回溯法来统计能进入的格子数
# 一种宽度优先：宽度优先可能导致重复计数（因为对从两个节点出发，他们可能到达相同的节点，因此导致重复计数，
# 要解决重复计数，就需要将访问标记设置为全局的，也就是说访问处理后，不恢复标记）
# 一种深度优先：因此采用深度优先
# 这里直接从（0,0）出发，进行深度优先遍历，对能进入的格子，就统计加1
# 标记：通过同等大小的矩阵来表示
# 进入格子计数：定义一个变量，来计数，对每个节点执行结束，返回从该节点能够到达的
# 结束条件：无路可走时返回，节点计数，节点周围的几点都已经访问，：
# 法1：
# 基于栈的回溯法
# 结束条件：栈为空
# 入栈条件：节点和小于阈值
# 逻辑结构：
#         从（0,0）出发，初始化入栈
#         当栈不空：
#             弹出
#             任选一个方向继续深入
#                 检查是已经访问过
#                 检查是没有访问过
#                     检查是否满足条件，数字之和小于k，增加计数，并入栈

# 法2：基于队列的回溯法
# 入队条件，和小于阈值
# 结束条件：队列为空
# 小结：
#      回溯过程，每次检查复合要求的才能入栈或者队列
#      关键要注意入栈条件、入队条件；对于访问过的元素就不能再入栈、入队了
class Solution:
    def sum_figure(self,data):
        sum = 0
        while(data):
            sum = sum + data%10
            data = data // 10
        return sum
    def method_queue(self,threshold, rows, cols):
        from collections import deque
        ret = 0
        if rows == 0 or cols == 0:
            return ret
        # 创建标记矩阵
        flag = [[0 for i in range(cols)] for j in range(rows)]
        # 创建栈
        qu = deque()
        start_row = 0
        start_col = 0
        flag[start_row][start_col] = -1
        # 检查是否满足进入条件
        if self.sum_figure(start_row) + self.sum_figure(start_col) <= threshold:
            ret += 1
            qu.append([start_row, start_col])
        direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        while(qu):
            start_row, start_col = qu.popleft()
            for i in range(4):
                new_row = start_row + direction[i][0]
                new_col = start_col + direction[i][1]
                # 超过索引、已经访问过
                if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols or flag[new_row][new_col] == -1:
                    continue
                else:
                    flag[new_row][new_col] = -1
                    # 检查是否满足进入条件
                    temp = self.sum_figure(new_row) + self.sum_figure(new_col)
                    if temp <= threshold:  #
                        ret += 1
                        print(new_row, new_col, ret)
                        qu.append([new_row, new_col])
        return ret
    def movingCount(self, threshold, rows, cols):
        # write code here
        # 深度优先遍历，非递归，基于栈来实现
        ret = 0
        if rows == 0 or cols == 0:
            return ret
        #创建标记矩阵
        flag = [[0 for i in range(cols)] for j in range(rows)]
        #创建栈
        s = []
        start_row = 0
        start_col = 0
        flag[start_row][start_col] = -1
        # 检查是否满足进入条件
        if self.sum_figure(start_row) + self.sum_figure(start_col) <= threshold:
            ret +=1
            s.append([start_row,start_col,0])
        direction = [[-1,0],[0,1],[1,0],[0,-1]]
        while(s):
            start_row, start_col, direct = s.pop()
            if direct <4:
                new_row = start_row + direction[direct][0]
                new_col = start_col + direction[direct][1]
                # 超过索引、已经访问过
                if new_row <0 or new_row >=rows or new_col < 0 or new_col >= cols or flag[new_row][new_col] == -1:
                    s.append([start_row, start_col, direct + 1])
                else:
                    flag[new_row][new_col] = -1
                    # 检查是否满足进入条件
                    temp= self.sum_figure(new_row) + self.sum_figure(new_col)
                    if  temp  <= threshold: #
                        ret += 1
                        print(new_row,new_col,ret)
                        s.append([start_row, start_col, direct+1])
                        s.append([new_row,new_col,0])
        return ret

#测试
threshold = 10
rows = 1
cols = 100
s = Solution()
print(s.method_queue(threshold,rows,cols))