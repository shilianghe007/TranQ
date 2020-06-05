import random
#####################################

# 根据变异或交叉概率，返回一个 0 或 1 的数
def crossMuteOrNot(crossMuteProb):
    test = [0] * 100
    l = round(100 * crossMuteProb)
    test[0: l] = [1]*l
    n = round(random.random() * 99)#######################去掉+1
    crossProbc = test[n]
    return crossProbc
