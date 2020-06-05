import math


def recursion(index, minDis, visited, path_index, path, route, n, DD, Cities, distance):
    sum = [0] * math.factorial(n - 1)
    if not path_index == n:  ###########增加-1 # 如果已经去过的城市数目不等于城市数量
        for i in range(n):
            if visited[i] == 0:  # 如果没有访问过
                visited[i] = 1
                path[route, path_index] = Cities[i, 0]
                path_index = path_index + 1
                minDis, visited, path_index, path, route, distance = recursion(i, minDis, visited, path_index, path,
                                                                               route, n, DD,
                                                                               Cities, distance)
                # 回溯
                path_index = path_index - 1
                visited[i] = 0
    else:
        path[route, path_index] = Cities[index, 0]  # 存下了这个路径顺序
        sum[route] = 0
        for i in range(n):
            if not i == n - 1:
                sum[route] += DD[path[route, i], path[route, i + 1]]  # 第一个加第二个、第二个加第三个……
            else:
                sum[route] += DD[path[route, i], path[route, 0]]  # 最后个加第一个
            path[route + 1, i] = path[route, i]  # 前面的需要保留，后面变化
        # sum[route] = sum[route] + DD[index, Cities[0, 0]]  # 加上返回的路程
        distance[route, 0] = sum[route]  # 存距离############去掉n后面的-1
        if minDis > sum[route]:
            minDis = sum[route]
        route += 1
    return minDis, visited, path_index, path, route, distance
