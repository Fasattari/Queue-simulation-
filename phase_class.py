from server_class import *
import random


class Phase:
    def __init__(self):
        self.servers = []
        self.probs = []
        self.pending = []
        self.index = 0

    def addServer(self, server, prob):
        self.servers.append(server)
        self.probs.append(prob)

    def set_index(self,index):
        #print "num_phase_phase :",index
        self.index = index

    def get_index(self):
        #print "num_phase_phase_out :",self.index
        return self.index

    def set_probability(self):
        probability = []
        n = 0
        for p in self.probs:
            probability.append([n, n+p])
            n += p

        self.probs = probability

    def getServer(self):
        rnd = random.random()
        for i in range(len(self.probs)):
            l = self.probs[i]
            if l[0] <= rnd <= l[1]:
                return self.servers[i]
