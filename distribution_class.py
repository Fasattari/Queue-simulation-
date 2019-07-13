import numpy as np
import random

class Distribution:

    def __init__(self, type='random',args=[2,7]):
        self.type = type
        self.args = args

    def get_num(self):

        if self.type=="poisson":
            return self.poisson()
        elif self.type=="normal":
            return self.normal()
        elif self.type=="lognormal":
            return self.lognormal()
        elif self.type=="gamma":
            return self.gamma()
        elif self.type=="betta":
            return self.betta
        elif self.type=="exponential":
            return self.exponential()
        elif self.type=="uniform":
            return self.uniform()
        elif self.type=="random":
            return self.random()

    def random(self):

        a=self.args[0]
        b=self.args[1]
        return random.randint(a,b)

    def poisson(self):
        lam = self.args[0]
        size=1
        return int(np.random.poisson(lam,size)[0])

    def normal(self):
        loc=self.args[0]
        scale = self.args[1]
        size =1
        return int(np.random.normal(loc,scale,size)[0])

    def lognormal(self):
        mean = self.args[0]
        sigma = self.args[1]
        size=1
        return int(np.random.lognormal(mean,sigma,size)[0])

    def gamma(self):
        shape = self.args[0]
        scale = self.args[1]
        size = 1
        return int(np.random.gamma(shape,scale,size)[0])

    def betta(self):
        a = self.args[0]
        b = self.args[1]
        size = 1
        return int(np.random.beta(a,b,size)[0])

    def exponential(self):
        scale = self.args[0]
        size = 1
        return int(np.random.exponential(scale,size)[0])

    def uniform (self):
        low = self.args[0]
        high = self.args[1]
        size = 1
        return int(np.random.uniform(low,high,size)[0])
