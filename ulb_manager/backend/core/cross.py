import random
import numpy as np
from .crossMuteOrNot import crossMuteOrNot
####################################################

# “交叉”操作
def cross(population, selectedChromoNums, crossProb):
    length = population.shape[1]  # 染色体的长度
    crossedChromos = np.zeros((2, length),dtype=int)
    crossProbc = crossMuteOrNot(crossProb)  # 根据交叉概率决定是否进行交叉操作，1则是，0则否
    crossedChromos[0, :] = population[selectedChromoNums[0], :]####################加了-1
    crossedChromos[1, :] = population[selectedChromoNums[1], :]####################加了-1
    if crossProbc == 1:
        c1 = round(random.random() * (length - 2)) + 1  # 在[1,bn - 1]范围内随机产生一个交叉位 c1
        c2 = round(random.random() * (length - 2)) + 1  # 在[1,bn - 1]范围内随机产生一个交叉位 c2
        chb1 = min(c1, c2)
        chb2 = max(c1, c2)
        middle = (crossedChromos[0, chb1:chb2]).copy()  # 两条染色体 chb1 到 chb2 之间互换位置#########去掉+1
        crossedChromos[0, chb1: chb2] = crossedChromos[1, chb1: chb2]
        crossedChromos[1, chb1: chb2] = middle
        for i in range(chb1):  # 看交叉后，染色体上是否有相同编码的情况（路径上重复出现两个城市）。若有，则该编码不参与交叉

            """
            这里find函数是返回值相同的下标，用了while 
            但是我觉得太繁琐而且find后返回的是个列表，不应该能够直接chb1+location
            所以我想到染色体上不会有重复的数字就不用使用while 改变为使用if语句，直接返回一个int值用来加减
            下面同理
            
            原代码改python:（下面chb1+location有错）
            """
            # index = [i for i in range(L_best.shape[0]) if L_best[i] == min(L_best)]
            # while find(crossedChromos[0, chb1 + 1: chb2] == crossedChromos[0, i]):
            #     location = find(crossedChromos[0, chb1 + 1: chb2] == crossedChromos[0, i])
            #     y = crossedChromos[1, chb1 + location]
            #     crossedChromos[0, i] = y
            tmp = [k for k in range(chb1,chb2) if crossedChromos[0,k]==crossedChromos[0,i]]
            while not len(tmp) == 0:
                y = crossedChromos[1,tmp[0]]
                crossedChromos[0,i] = y
                #tmp.pop(0)
                tmp = [k for k in range(chb1, chb2) if crossedChromos[0, k] == crossedChromos[0, i]]
            tmp1 = [k for k in range(chb1, chb2) if crossedChromos[1, k] == crossedChromos[1, i]]
            while not len(tmp1) == 0:
                y = crossedChromos[0,tmp1[0]]
                crossedChromos[1,i] = y
                #tmp1.pop(0)
                tmp1 = [k for k in range(chb1, chb2) if crossedChromos[1, k] == crossedChromos[1, i]]
            """
                if crossedChromos[0, i] in crossedChromos[0, chb1:chb2]:
                location = crossedChromos[0, chb1:chb2].index(crossedChromos[0, i])
                y = crossedChromos[1, chb1 + location]
                crossedChromos[0, i] = y

            if crossedChromos[1, i] in crossedChromos[1, chb1 + 1: chb2]:
                location = crossedChromos[1, chb1 + 1: chb2].index(crossedChromos[1,i])
                y = crossedChromos[0, chb1 + location]
                crossedChromos[1, i] = y
            """


        """
        此代码逻辑检测[chb1,+1:chb2]两边是否有重复的基因
        上面检验左边，下面检验右边，所以下面我认为应该遍历的范围有改动
        
        原代码转python:
        if crossedChromos[0, i] in crossedChromos[0, : chb2]
        
        """
        for i in  range(chb2, length):####################去掉了+1
            tmp = [k for k in range(0, chb2) if crossedChromos[0, k] == crossedChromos[0, i]]
            while not len(tmp) == 0:
                y = crossedChromos[1, tmp[0]]
                crossedChromos[0, i] = y
                #tmp.pop(0)
                tmp = [k for k in range(0, chb2) if crossedChromos[0, k] == crossedChromos[0, i]]
            tmp1 = [k for k in range(0, chb2) if crossedChromos[1, k] == crossedChromos[1, i]]
            while not len(tmp1) == 0:
                y = crossedChromos[0, tmp1[0]]
                crossedChromos[1, i] = y
                # tmp1.pop(0)
                tmp1 = [k for k in range(0, chb2) if crossedChromos[1, k] == crossedChromos[1, i]]

    nums = np.zeros((length,1),dtype=int)
    for i in range(length):
        if(nums[crossedChromos[0,i],0] != 0):
            a = 0   #出现重复
        else:
            nums[crossedChromos[0, i], 0] = 1
    return crossedChromos
