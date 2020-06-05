import numpy as np
#######################################
def getFit_2(N, M, DD, Dis_max, M_max, punishment, City_Number, population):
    # M_max是一个二维矩阵，分别代表了不同车型的最大载重量以及车型数量，按载重量升序排列，如：
    # [2, 4;5, 3]表示有载重量5吨车子3辆，2吨车子4辆
    # 计算每个个体的适应度
    fit = np.zeros((N,1))  # 记录每一个个体的适应度
    Num = np.zeros((N,1))  # 记录每一个个体的不合格路径数
    length = np.zeros((N,1))  # 记录每一个个体的路径总长度
    manzai = np.zeros((N, 1))  # 记录每一个个体的满载率
    num_of_car_type = M_max.shape[0]
    for j in range(N):  # 对每一个个体进行遍历
        temp_M_max = M_max.copy()
        if population[j, 0] > City_Number - 1:
            Z = 0
        else:
            Z = DD[City_Number, int(population[j, 0])]  # 记录一个个体中所有路线总长度
        z = Z  # 单条路线长度
        m = 0  # 单条路线载重量
        num = 0  # 距离上和载重量上不合格路径数
        for k in range(population.shape[1] - 1):  # 对经过的每一个点遍历, 除最后一个点
            if population[j, k] > City_Number - 1:  # 表示该点为配送中心
                # 先判断在载重是否超出限制
                ok = 0
                for n in range(num_of_car_type):
                    if m > 0:
                        if temp_M_max[n, 0] > m and temp_M_max[n, 1] > 0:
                            ok = 1
                            temp_M_max[n, 1] -= 1
                            break
                    else:
                        ok = 1
                        break
                if ok == 0:
                    num += 1
                else:
                    if z > Dis_max:
                        num += 1
                        # 如果形成超过限制，是否应该把在前面for循环中减去的车辆数加回来？（待写）
                m = 0
                z = 0  # 清零
            if population[j, k] > City_Number:  # 计算距离
                if population[j, k + 1] > City_Number - 1:
                    distance = 0
                else:
                    distance = DD[City_Number, int(population[j, k + 1])]
            else:
                if population[j, k + 1] > City_Number - 1:
                    distance = DD[population[j, k], City_Number]
                else:
                    distance = DD[population[j, k], population[j, k + 1]]

            z = z + distance  # 累加每条路径的长度
            Z = Z + distance
            if population[j, k] <= City_Number - 1:  # 累加载重量
                m = m + M[0, population[j, k]]
            else:
                m = m
        # 处理最后那个没有被计入的点
        if population[j, population.shape[1]-1] <= City_Number - 1:
            z = z + DD[City_Number, population[j, population.shape[1]-1]]
            m = m + M[0, population[j, population.shape[1]-1]-1]
        # 先判断在载重是否超出限制
        ok = 0
        for n in range(num_of_car_type):
            if temp_M_max[n, 0] > m and temp_M_max[n, 1] > 0:
                ok = 1
                temp_M_max[n, 1] -= 1
                break
        if ok == 0:
            num += 1
        else:
            if z > Dis_max:
                num += 1
                # 如果形成超过限制，是否应该把在前面for循环中减去的车辆数加回来？（待写）

        # 计算满载率
        sum_manzai = 0
        for n in range(M_max.shape[0]):
            sum_manzai += (M_max[n, 1] - temp_M_max[n, 1]) * M_max[n, 0]
        print('第'+str(j)+'代 sum_manzai:')
        print(sum_manzai)
        # print(M_max)
        print(temp_M_max)
        manzai[j, 0] = np.sum(M) / sum_manzai
        # 计算适应度值
        fit[j, 0] = 1 / (Z + punishment * num)
        Num[j, 0] = num
        length[j, 0] = Z
    return fit,Num,length,manzai
