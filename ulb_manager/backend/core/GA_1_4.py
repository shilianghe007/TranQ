import numpy as np
import random
import math
from .getFit_2 import getFit_2
from .AG import AG
from .cross import cross
from .mut import mut
from .select import select
from .short_route import short_route
from ..models import iteration

###########################################
# 加入不同车型的算法，方法是贪婪算法，适应度函数变成了getFit_2()
# # 初始化操作
# 设置各项参数和位置矩阵
class GA:
    def __init__(self,token,Car_Number,Dis_max,M_max,City_Number,N,crossProb,muteProb,iteration,punishment,Location,center,M):
        self.token = token
        self.Car_Number = Car_Number  # 汽车数量
        self.Dis_max = Dis_max  # 车辆最大行驶距离
        self.M_max = M_max  # 最大载重量
        self.City_Number = City_Number  # 需求点数量
        self.N = N  # 群体规模
        self.crossProb = crossProb  # 交叉概率
        self.muteProb = muteProb  # 变异概率
        self.iteration = iteration  # 迭代次数
        self.punishment = punishment  # 惩罚权重
        # self.width = width  # 范围
        self.Location = Location  # 随机生成坐标点
        # self.center = np.mat([self.width / 2, self.width / 2])  # 配送中心坐标
        # self.Location = np.concatenate((self.Location, self.center))  # jiang
        self.M = M# 随机生成各点需求量
        # Location = [Location,center]
        # 计算点之间的路径
        self.DD = np.zeros((self.City_Number + 1, self.City_Number + 1))
        for i in range(self.City_Number + 1):  ##############+1
            for j in range(self.City_Number + 1):  ################+1
                if not i == j:
                    self.DD[i, j] = math.pow(
                        math.pow(self.Location[i, 0] - self.Location[j, 0], 2) + math.pow(self.Location[i, 1] - self.Location[j, 1], 2),
                        0.5)
                else:
                    self.DD[i, j] = np.spacing(1)

    def run(self):
        # # 初始化群体
        # 随机产生初始种群
        population = np.zeros((self.N, self.City_Number + self.Car_Number - 1), dtype=int)  # population
        for i in range(self.N):
            population[i] = np.arange(self.City_Number + self.Car_Number - 1)  # 不重复的随机排列
            random.shuffle(population[i])
        # 为初始种群，包括多条染色体

        # # 计算适应度矩阵（记录每个个体适应度）
        fit, ill_path_Num, length, manzai = getFit_2(self.N, self.M, self.DD, self.Dis_max, self.M_max, self.punishment, self.City_Number, population)
        # # 记录每一次迭代的最优个体
        best_routes = np.zeros((self.iteration, self.City_Number + self.Car_Number - 1))
        best_manzais = np.zeros((self.iteration, self.City_Number + self.Car_Number - 1))
        best_lengths = np.zeros((self.iteration, 1))
        # # 循环迭代
        for i in range(self.iteration):
            # # 计算被选中的概率及累加概率
            sum_fit = np.sum(fit)
            pro = fit / sum_fit
            cumulativeProbs = np.zeros((self.N, 1))
            sum_temp = 0
            for j in range(self.N):
                sum_temp = sum_temp + pro[j, 0]
                cumulativeProbs[j, 0] = sum_temp
            newPopulation = np.zeros((self.N, self.City_Number + self.Car_Number - 1), dtype=int)
            for j in range(0, self.N, 2):  # 俩俩搭配
                selectedChromos = select(cumulativeProbs)  # 选择操作，选出两条需要交叉编译的染色体，即父亲母亲
                crossedChromos = cross(population, selectedChromos, self.crossProb)  # 交叉操作，返回交叉后的染色体
                newPopulation[j, :] = mut(crossedChromos[0, :], self.muteProb)  # 对交叉后的染色体进行变异操作
                newPopulation[j + 1, :] = mut(crossedChromos[1, :], self.muteProb)  # 对交叉后的染色体进行变异操作
            # 用蚁群算法对生成的种群进行局部微调
            print("微调开始"+str(i))
            for j in range(self.N):
                """ 检测出每个个体中的每条路径
                # 若序列为
                1
                2
                3
                10
                12
                5
                6
                14，则position_length = [1, 3
                6, 2]
                """
                position_length = []
                pointer = 0  ##############1改为0
                length = 0
                pos = 0  ##############1改为0
                new = newPopulation[j, :]
                while pointer < newPopulation.shape[1] - 1:  # @@@@@@@@@@@@@@-1
                    if newPopulation[j, pointer] < self.City_Number:  # @@@@@@@@@@@@@@去掉最后的+1
                        pos = pointer
                        while pointer < newPopulation.shape[1] - 1 and newPopulation[j, pointer] < self.City_Number:
                            length = length + 1
                            pointer = pointer + 1
                        position_length += [[pos, length]]
                        length = 0
                    else:
                        pointer += 1
                # 对每一个个体中的路径遍历，微调
                p = random.random()
                weitiao = 1
                position_length = np.mat(position_length)
                for k in range(position_length.shape[0]):
                    pos1 = position_length[k, 0]
                    pos2 = position_length[k, 0] + position_length[k, 1] - 1
                    # tmp = np.mat([City_Number] + new[pos1:pos2 + 1])
                    # tmp = np.append(np.mat([City_Number]), new[pos1:pos2 + 1], axis=1)
                    new_change = new[pos1:pos2 + 1]
                    new_change.shape = (1, pos2 - pos1 + 1)
                    tmp = np.append(np.mat([self.City_Number]), new_change, axis=1)
                    if position_length[k, 1] < 7:  ###############1
                        tmp = np.transpose(short_route(self.DD, np.transpose(tmp)))
                    else:
                        if p < 1 - i / self.iteration:
                            tmp = np.transpose(AG(self.DD, np.transpose(tmp)))
                        else:
                            weitiao = 0
                    tmp = tmp[0, 1:position_length[k, 1] + 1]  # 去掉头部#############1->0 2->1
                    # new = [new[0:pos1], tmp, new[pos2 + 1: new.shape[1]]]  ##########1->0  去掉+1
                    new[pos1:pos2 + 1] = tmp
                newPopulation[j, :] = new
                if weitiao == 1:
                    print("对第" + str(i + 1) + "次迭代的第" + str(j + 1) + "个个体进行微调")  ############+1
            population = newPopulation  # 产生了新的种群
            # # 计算适应度矩阵（记录每个个体适应度）
            fit, ill_path_Num, length, manzai = getFit_2(self.N, self.M, self.DD, self.Dis_max, self.M_max, self.punishment, self.City_Number, population)

            # 发回每次迭代中最优的个体情况
            best_length = float("inf")
            best_fit = 0
            best_population = np.ones((1, self.City_Number + self.Car_Number - 1), dtype=int) * (self.City_Number + 1)
            best_manzai = 0
            ak = -1
            for j in range(self.N):
                if ill_path_Num[j, 0] == 0 and length[j, 0] < best_length:
                    ak = j
                    best_length = length[j, 0]
                    best_fit = fit[j, 0]
                    best_population = population[j, :]
                    best_manzai = manzai[j, 0]
            path = best_population
            path.shape = (1, self.City_Number + self.Car_Number - 1)
            # 将路径的范围缩为City_Number + 1以内
            #path1 = np.hstack((np.mat([self.City_Number + 1], path, np.mat([self.City_Number + 1]))))
            #path1 = np.hstack(np.mat([self.City_Number + 1]), path, np.mat([self.City_Number + 1])))
            # path1 = np.hstack((np.mat([self.City_Number + 1]), path, np.mat([self.City_Number + 1])))
            # for j in range(path1.shape[1]):
            #     if path1[0, j] > self.City_Number:
            #         path1[0, j] = self.City_Number + 1
            # 输出这条路径
            print("第" + str(i) + "次迭代的最优路径为：")
            print(path)
            print('满载率对应：' + str(best_manzai) + '这次迭代中第' + str(ak) + '个个体最优')
            # 计算本次迭代最优个体和整体平均效果
            # 整体适应度
            fit_ave = sum_fit
            # 整体路径总长度
            length_ave = np.sum(length)
            # 最优适应度
            fit_best = best_fit
            # 最优个体的总长
            length_best = best_length
            # 最优个体满载率
            full = best_manzai
            best_lengths[i, 0] = best_length
            best_routes[i,:] = path
            best_manzais[i,0] = full

            # 存储迭代结果进入数据库
            try:
                iter = iteration()
                iter.best_length = best_length
                iter.ave_fit = str(sum_fit) + '#' + str(full)
                iter.token = self.token
                iter.iter_id = i
                pathci = ''
                print(iter.ave_fit)
                for num in path[0]:
                    #print(num)
                    pathci += '#'
                    pathci += str(num)
                #print(pathci)
                iter.best_route = pathci
                iter.save()
            except:
                print('第'+str(i)+'次迭代的结果保存失败')

        # 发回最终最有个体情况
        list_best_lengths = best_lengths[:, 0].tolist()
        a = min(list_best_lengths)
        b = list_best_lengths.index(a)
        # [a, b] = min(best_lengths)  # a代表最小值，b代表最小值在原数组中的下标
        path = best_routes[b, :]
        # 存储最终结果进入数据库
        try:
            iter = iteration()
            iter.best_length = b
            iter.ave_fit = str(best_manzais[b, :]) + '#' + str(best_manzais[b, :])
            iter.token = self.token
            iter.iter_id = self.iteration
            pathci = ''
            print(iter.ave_fit)
            for num in path[0]:
                # print(num)
                pathci += '#'
                pathci += str(num)
            # print(pathci)
            iter.best_route = pathci
            iter.save()
        except:
            print('最终结果保存失败')
#
# Car_Number = 10  # 汽车数量
# Dis_max = 25  # 车辆最大行驶距离
# M_max = np.mat([[5, 5], [8, 5]])  # 最大载重量
# City_Number = 20  # 需求点数量
# N = 150  # 群体规模
# crossProb = 0.4  # 交叉概率
# muteProb = 0.1  # 变异概率
# iteration = 200  # 迭代次数
# punishment = 200  # 惩罚权重
# width = 10  # 范围
# Location = np.random.random((City_Number, 2)) * width  # 随机生成坐标点
# center = np.mat([width / 2, width / 2])  # 配送中心坐标
# Location = np.concatenate((Location, center))  # jiang
# M = np.random.random((1, City_Number)) * 3 #  随机生成各点需求量
#
# ins = GA(Car_Number,Dis_max,M_max,City_Number,N,crossProb,muteProb,iteration,punishment,width,Location,center,M)
# ins.run()
