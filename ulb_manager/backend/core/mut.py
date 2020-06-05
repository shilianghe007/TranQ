import random
import numpy as np
from .crossMuteOrNot import crossMuteOrNot
#“变异”操作
# choromo 为一条染色体
##########################################
def mut(chromo,muteProb):
    length = len(chromo) # 染色体的的长度
    snnew = chromo
    muteProbm = crossMuteOrNot(muteProb)  # 根据变异概率决定是否进行变异操作，1则是，0则否
    if muteProbm == 1:
        """
        我觉得该在[0,bn-1]内产生
        
        原代码转pyhton:
        c1 = round(random.random()*(length - 2)) + 1  # 在 [1, bn - 1]范围内随机产生一个变异位
        c2 = round(random.random()*(length - 2)) + 1  # 在 [1, bn - 1]范围内随机产生一个变异位
        """
        c1 = round(random.random()*(length - 2)) + 1  # 在 [1, bn - 1]范围内随机产生一个变异位
        c2 = round(random.random()*(length - 2)) + 1  # 在 [1, bn - 1]范围内随机产生一个变异位
        chb1 = min(c1, c2)
        chb2 = max(c1, c2)
        """
        这里[chb1+1:chb2]我挺疑惑，到时候分析下
        """
        x = chromo[chb1 : chb2]################chb2后+1
        snnew[chb1 : chb2] = np.flipud(x) # 变异，则将两个变异位置的染色体倒转##########chb2后+1

        # nums = np.zeros((length, 1), dtype=int)
        # for i in range(length):
        #     if (nums[snnew[i], 0] != 0):
        #         a = 0  # 出现重复
        #     else:
        #         nums[snnew[i], 0] = 1
    return snnew
