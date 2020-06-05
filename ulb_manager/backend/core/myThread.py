import threading
import time
from .GA_1_4 import GA
exitFlag = 0


class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, token, Car_Number, Dis_max, M_max, City_Number, N, crossProb, muteProb, iteration, punishment, Location, center, M):
        threading.Thread.__init__(self)
        self.token = token
        self.Car_Number = Car_Number
        self.Dis_max = Dis_max
        self.M_max = M_max
        self.City_Number = City_Number
        self.N = N
        self.crossProb = crossProb
        self.muteProb = muteProb
        self.muteProb = muteProb
        self.punishment = punishment
        self.iteration = iteration
        # self.width = width
        self.Location = Location
        self.center = center
        self.M = M

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        ins = GA(self.token, self.Car_Number, self.Dis_max, self.M_max, self.City_Number, self.N, self.crossProb, self.muteProb, self.iteration, self.punishment, self.Location, self.center, self.M)
        ins.run()

