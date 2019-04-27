# -*- coding:utf-8 -*-

# 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
# 路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，
# 向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。
# 例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，
# 但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，
# 路径不能再次进入该格子。

# 关键词：字母矩阵、字符串路径、一个格子只能访问一次
# 考察：图、考察路径规划、路径匹配
# 常规思路：选择起点，然后递归的对器件周围的字符进行宽度优先遍历，当四个字符中没有字符与
# 子串的下一个字符匹配时返回False

# 实现：以每个字符作为起点，来查找匹配；
#       位于四周的字符只有三个方向,为了统一，设计flag比matrix多一圈，也就是flag的row = rows+2,col = cols+2
# 设计一个辅助函数，从一个字符出发，匹配一段字符，宽度优先遍历该起点字符周围的四个字符，
# 为了避免重复访问，还需要设计访问标记,对每个节点先标记

# 小结：
# 考察：递归算法、宽度优先遍历、回溯法
# ####回溯无非就是对使用过的字符进行标记后和处理后的去标记####
# 出现错误的地方：1、列表的浅拷贝特性，创建独立的元素方法；2、牛客中没有numpy模块；
#                 3、访问标记的设定，并不需要扩充矩阵，只要访问范围超过边界就提前返回已经访问过就行了；
#                 4、为了避免同级的访问标记干扰，再访问结束后要恢复原来标记；
#                 5、由于采用递归，因此递归的结束条件要考虑清楚：已经找到结果、超过索引界限、不匹配、匹配下一步执行
#                 6、将一个序列映射为矩阵的方法:idx = row_idx*cols + col_idx；
class Solution1:
    def helper(self,matrix, rows,cols,start_row, start_col, path, path_idx, flag):
        # 检查是否比较完毕
        #if path_idx == len(path):
            #return True
        # 比较字符是否相同
        if matrix[start_row][start_col] != path[path_idx]:
             return False
        else:
            # 标记当前格子
            flag[start_row][start_col] = -1
            # 宽度优先遍历，比较下一个字符
            direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            ret = []
            for value in direction:
                new_row = start_row + value[0]
                new_col = start_col + value[1]
                # 检查是否比较完毕
                if path_idx + 1 == len(path):
                    return True
                if (new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols)or flag[new_row][new_col] == -1:
                    ret.append(False)
                else:
                    temp = self.helper(matrix, rows,cols,new_row, new_col, path, path_idx+1, flag)
                    ret.append(temp)
            if ret[0] or ret[1] or ret[2] or ret[3]:
                return True
            else:
                flag[start_row ][start_col] = 0
                return False
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if rows == 0 or cols == 0 or path == '':
            return False
        L = list(matrix)
        M = []
        for i in range(rows):
            M.append(list(matrix[i * cols:(i + 1) * cols]))
        matrix = M
        path_idx = 0
        flag = [[0 for i in range(cols)] for j in range(rows)]
        for start_row in range(rows):
            for start_col in range(cols):
                temp = self.helper(matrix,rows,cols,start_row,start_col,path,path_idx,flag)
                if temp is True:
                    return temp
        return False
class Solution:
    def helper(self,matrix, rows,cols,start_row, start_col, path, path_idx, flag):
        # 检查是否比较完毕
        if path_idx == len(path):
            return True
        #对超过索引或者已经访问过的直接返回False
        if start_row < 0 or start_row >= rows or start_col < 0 or start_col >= cols or flag[start_row][start_col] == -1:
            return  False
        # 比较字符是否相同
        if start_row < 0 or start_row >= rows or start_col < 0 or start_col >= cols:
            print(1)
        idx = start_row*cols + start_col
        if path_idx == 11:
            print(1)
        if matrix[idx] != path[path_idx]:
             return False
        else:
            # 标记当前格子
            flag[start_row][start_col] = -1
            # 宽度优先遍历，比较下一个字符
            direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            ret = []
            for value in direction:
                new_row = start_row + value[0]
                new_col = start_col + value[1]
                temp = self.helper(matrix, rows,cols,new_row, new_col, path, path_idx+1, flag)
                ret.append(temp)
            if ret[0] or ret[1] or ret[2] or ret[3]:
                return True
            else:
                flag[start_row ][start_col] = 0
                return False
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if rows == 0 or cols == 0 or path == '':
            return False
        path_idx = 0
        flag = [[0 for i in range(cols)] for j in range(rows)]
        for start_row in range(rows):
            for start_col in range(cols):
                temp = self.helper(matrix,rows,cols,start_row,start_col,path,path_idx,flag)
                if temp is True:
                    return temp
        return False
# 测试
#matrix = "AAAAAAAAAAAA"
matrix = "ABCEHJIGSFCSLOPQADEEMNOEADIDEJFMVCEIFGGS"
rows = 5
cols = 8
#path = "AAAAAAAAAAAA"
path = "SLHECCEIDEJFGGFIE"
s = Solution1()
print(s.hasPath(matrix,rows,cols,path))