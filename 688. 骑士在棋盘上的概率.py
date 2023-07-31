#超时版本
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        #
        #每一步在棋盘内的概率，且最终每个点在棋盘内的概率并不尽相同，所有的可能点都得加起来
        dir_tuple=((1,-2),(1,2),(2,-1),(2,1),(-1,-2),(-1,2),(-2,-1),(-2,1))
        #point_times=0
        #去过的点怎么处理，目前已剔除会落在棋盘外的点
        mydict={}
        def call_back(poslist,lasttime):
            nxtlist=[]
            if lasttime==0:
                return len(poslist)
            for pos in poslist:
                print(nxtlist)
                if (pos[0],pos[1]) in mydict:
                    nxtlist+=mydict[(pos[0],pos[1])]
                else:
                    for way in dir_tuple:
                        if 0<=pos[0]+way[0]<n and 0<=pos[1]+way[1]<n:
                            if (pos[0],pos[1]) not in mydict:
                                mydict[(pos[0],pos[1])]=[]
                            mydict[(pos[0],pos[1])].append((pos[0]+way[0],pos[1]+way[1]))
                    if (pos[0],pos[1]) in mydict:
                        nxtlist+=mydict[(pos[0],pos[1])]
            return call_back(nxtlist,lasttime-1)
        point_times=call_back([[row,column]],k)
        return point_times/(8**k)

#改进版本，进行记录
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        #
        #每一步在棋盘内的概率，且最终每个点在棋盘内的概率并不尽相同，所有的可能点都得加起来
        dir_tuple=((1,-2),(1,2),(2,-1),(2,1),(-1,-2),(-1,2),(-2,-1),(-2,1))
        #point_times=0
        #去过的点怎么处理，目前已剔除会落在棋盘外的点
        #宁愿尽量少进行数据结构的调整
        cur_pos=[[0]*n for _ in range(n)]
        cur_pos[row][column]=1
        #总的次数，
        #当前位置，下一级位置,
        point_times=0
        def call_back(now_pos,lasttime):
            if lasttime==0:
                return now_pos
            new_pos=[[0]*n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    if now_pos[r][c]>0:
                        for way in dir_tuple:
                            if 0<=r+way[0]<n and 0<=c+way[1]<n:
                                print(r+way[0],c+way[1],new_pos[r+way[0]][c+way[1]])
                                new_pos[r+way[0]][c+way[1]]+=now_pos[r][c]
                                #new_pos[r+way[0]][c+way[1]]*=now_pos[r][c]
                                #前一个pos能到当前pos，后一个也可以到该pos，要避免多加，其实就是当前的pos的次数
            print(now_pos,new_pos)
            return call_back(new_pos,lasttime-1)
        final_pos=call_back(cur_pos,k)
        for i in range(n):
            for j in range(n):
                point_times+=final_pos[i][j]
        #print(point_times/(8**k))
        return point_times/(8**k)


n = 3
k = 2 
row = 0
column = 0
Solution().knightProbability(n, k, row, column)