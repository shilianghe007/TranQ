import numpy as np
import random

####################################################
# --------------------------------------------------
# “选择”操作，返回所选择染色体在种群中对应的位置
# cumulatedPro 所有染色体的累计概率
def select(cumulatedPro):
    selectedChromoNums = np.zeros((2, 1),dtype=int)
    # 从种群中选择两个个体，最好不要两次选择同一个个体
    for i in range(2):
        r = random.random()  # 产生一个随机数
        prand = cumulatedPro - r
        j = 0
        while prand[j] < 0:
            j += 1

        if i == 1 and j == selectedChromoNums[i - 1]:  # 若相同就再选一次
            r = random.random()  # 产生一个随机数
            prand = cumulatedPro - r
            j = 0
            while prand[j] < 0:
                j += 1
        selectedChromoNums[i] = j
    return selectedChromoNums
