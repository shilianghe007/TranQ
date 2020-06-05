import numpy as np
import math
import random


########################################

def AG(DD, Cities):
    m = 50  # # m蚂蚁个数
    Alpha = 1  # # Alpha表征信息素重要程度的参数
    Beta = 5  # # Beta表征启发式因子重要程度的参数
    Rho = 0.1  # # Rho信息素蒸发系数
    NC_max = 20  # # 最大迭代次数
    Q = 100  # # 信息素增加强度系数
    # # -------------------------------------------------------------------------
    # # 主要符号说明
    # # Cn个城市的坐标，n×2的矩阵
    # # NC_max最大迭代次数
    # # m蚂蚁个数
    # # Alpha表征信息素重要程度的参数
    # # Beta表征启发式因子重要程度的参数
    # # Rho信息素蒸发系数
    # # Q信息素增加强度系数
    # # R_best各代最佳路线
    # # L_best各代最佳路线的长度
    # #= == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
    # # 第一步：变量初始化
    n = len(Cities)  # n表示问题的规模（城市个数）
    D = np.zeros((n, n))  # 将Cities中的数据放到一个邻接矩阵中，最后最短路径要处理
    for i in range(n):
        for j in range(n):
            D[i, j] = DD[Cities[i, 0], Cities[j, 0]]  # i = j时不计算，应该为0，但后面的启发因子要取倒数，用eps
    Eta = 1 / D  # Eta为启发因子，这里设为距离的倒数
    Tau = np.ones((n, n))  # Tau为信息素矩阵
    Tabu = np.zeros((m, n),dtype=int)  # 存储并记录路径的生成
    NC = 1  # 迭代计数器，记录迭代次数
    R_best = np.zeros((NC_max, n),dtype=int)  # 各代最佳路线
    L_best = float('inf') * np.ones((NC_max, 1))  # 各代最佳路线的长度
    L_ave = np.zeros((NC_max, 1))  # 各代路线的平均长度

    while NC <= NC_max:  # 停止条件之一：达到最大迭代次数，停止
        #print(NC)
        # # 第二步：将m只蚂蚁放到n个城市上
        Randpos = []  # 随即存取
        x = np.arange(n)
        for i in range(math.ceil(m / n)):
            random.shuffle(x)
            Randpos += list(x)
        Randpos = np.mat(Randpos)
        Tabu[:, 0] = list(np.transpose(Randpos[0, :m]))
        # # 第三步：m只蚂蚁按概率函数选择下一座城市，完成各自的周游
        # if (NC == 2):
        #     s =1
        for j in range(1, n):  # 所在城市不计算##############去掉-1
            for i in range(m):
                visited = Tabu[i, :j]  # 记录已访问的城市，避免重复访问
                J = np.zeros((1, n - j),dtype=int)  # 待访问的城市
                P = np.zeros((1, n - j))  # 待访问城市的选择概率分布
                Jc = 0  ##############1->0
                for k in range(n):
                    if not k in visited:  # 开始时置0
                        J[0,Jc] = k
                        Jc += 1  # 访问的城市个数自加1
                # 下面计算待选城市的概率分布
                #print(i, j)
                for k in range(J.shape[1]):
                    # u=visited[-1]
                    # t = Tau[visited[-1], J[0,k]]
                    # t = math.pow(Tau[visited[-1], J[0,k]], Alpha)
                    P[0,k] = math.pow(Tau[visited[-1], J[0,k]], Alpha) * math.pow(Eta[visited[-1], J[0,k]], Beta)
                P = P/np.sum(P)
                # 按概率原则选取下一个城市
                Pcum = np.cumsum(P, axis=1)  # cumsum，元素累加即求和
                Select = [i for i in range(Pcum.shape[1]) if Pcum[0,i] >= random.random()]  # 若计算的概率大于原来的就选择这条路线,下标
                try:
                    to_visit = J[0,Select[0]]
                except:
                    print(J)
                    print(Select)
                    print(Pcum)
                    print(P)
                Tabu[i, j] = to_visit
        if NC >= 2:
            Tabu[0, :] = R_best[NC - 2, :]  ###############-1改为-2
            # # 第四步：记录本次迭代最佳路线
        L = np.zeros((m, 1))  # 开始距离为0，m * 1的列向量
        for i in range(m):
            R = Tabu[i, :]
            for j in range(n - 1):
                L[i,0] = L[i,0] + D[R[j], R[j + 1]]  # 原距离加上第j个城市到第j + 1个城市的距离
            L[i,0] = L[i,0] + D[R[0], R[n-1]]  # 一轮下来后走过的距离
        L_best[NC - 1] = min(L)  # 最佳距离取最小###################加了一个-1
        pos = [i for i in range(L.shape[0]) if L[i,0] == L_best[NC - 1]]
        R_best[NC - 1, :] = Tabu[pos[0], :]  # 此轮迭代后的最佳路线###################加了一个-1
        L_ave[NC - 1] = np.mean(L)  # 此轮迭代后的平均距离###################加了一个-1
        NC = NC + 1  # 迭代继续

        # # 第五步：更新信息素
        Delta_Tau = np.zeros((n, n))  # 开始时信息素为n * n的0矩阵
        for i in range(m):
            for j in range(n - 1):
                Delta_Tau[Tabu[i, j], Tabu[i, j + 1]] = Delta_Tau[Tabu[i, j], Tabu[i, j + 1]] + Q / L[
                    i]  ###################加了多个-1
                # 此次循环在路径（i，j）上的信息素增量
            Delta_Tau[Tabu[i, n - 1], Tabu[i, 0]] = Delta_Tau[Tabu[i, n - 1], Tabu[i, 0]] + Q / L[
                i]  ##################加了多个-1
            # 此次循环在整个路径上的信息素增量
        Tau = (1 - Rho) * Tau + Delta_Tau  # 考虑信息素挥发，更新后的信息素
        # # 第六步：禁忌表清零
        Tabu = np.zeros((m, n),dtype=int)  # # 直到最大迭代次数
    # # 第七步：输出结果
    Pos = [i for i in range(L_best.shape[0]) if L_best[i] == min(L_best)]  # 找到最佳路径（非0为真）################加了min
    r = R_best[Pos[0], :]
    Shortest_Route = Cities[r, 0]  # 最大迭代次数后最佳路径
    # Shortest_Length = L_best(Pos(1)) # 最大迭代次数后最短距离
    # 将最佳路径修改顺序，确保配送中心置于第一位
    tmp = np.concatenate((Shortest_Route, Shortest_Route), axis=0)
    pointer = 0
    while not tmp[pointer] == DD.shape[0]-1:
        pointer += 1
    Shortest_Route = tmp[pointer:n + pointer]  ###############删除最后的-1
    return Shortest_Route

