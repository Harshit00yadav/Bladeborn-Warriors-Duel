from math import dist


class Constrain:
    def __init__(self, length, n1, n2, flag):
        self.n1 = n1
        self.n2 = n2
        self.length = length
        self.flag = flag

    def method0(self):
        cur_dist = dist(self.n1.pos, self.n2.pos)
        if cur_dist > self.length or cur_dist < self.length:
            offset = (self.n1.pos - self.n2.pos) * (self.length - cur_dist) / cur_dist
            self.n1.add_forces(offset / 2)
            self.n2.add_forces(- offset / 2)

    def method1(self):
        cur_dist = dist(self.n1.pos, self.n2.pos)
        if cur_dist > self.length:
            offset = (self.n1.pos - self.n2.pos) * (self.length - cur_dist) / cur_dist
            self.n1.add_forces(offset / 2)
            self.n2.add_forces(- offset / 2)

    def solve(self):
        if self.flag == 0:
            self.method0()
        elif self.flag == 1:
            self.method1()
