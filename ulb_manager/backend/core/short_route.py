import numpy as np
import math
from .recursion import recursion


#######################################
def short_route(DD, Cities):
    n = len(Cities)  ##城市数量
    minDis = float('inf')  ##最短路径
    visited = np.zeros((n, 1))  ##第i个城市已经去过为1，反之为0
    path_index = 1  ##已经去过的城市数目(1默认已去)################1->0
    path = np.zeros((math.factorial(n - 1) + 1, n + 1), dtype=int)  ##存储经过城市的路线，最后一位存距离
    distance = np.zeros((math.factorial(n - 1) + 1, 1))
    path[:, 0] = Cities[0]
    route = 0  ##存储第几条路线################1->0
    Shortest_Route = np.zeros((n, 1))
    visited[0] = 1  # 出发城市################1->0
    minDis, a, b, path, c, distance = recursion(0, minDis, visited, path_index, path, route, n, DD, Cities,
                                                distance)  #########1->0
    for i in range(math.factorial(n - 1)):
        if distance[i, 0] == minDis:  ###############去掉+1
            for j in range(n):
                Shortest_Route[j, 0] = path[i, j]  ################1->0
    return Shortest_Route
