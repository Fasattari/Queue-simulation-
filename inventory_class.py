__author__ = 'mahdieh & faezeh'
import random
class Inventory:

    def __init__(self, capacity, order_time, available_stuff, cost, cost_scrap=-1):

        self.capacity = capacity
        self.order_time = order_time
        self.available_stuff = available_stuff
        self.cost = cost
        self.cost_scrap = cost_scrap
        self.probs_load = []
        self.probs_demand = []

    def get_capacity(self):
        return self.capacity

    def get_cost(self):
        return self.cost

    def get_cost_scrap(self):
        return self.cost_scrap

    def get_order_time(self):
        return self.order_time

    def get_availeble_stuff(self):
        return self.available_stuff

    def dec_available_stuff(self, num):
        if num < self.available_stuff :
            self.available_stuff -= num
            return num
        else:
            num = self.available_stuff
            self.available_stuff = 0
            return num

    def get_needs(self):
        return self.capacity - self.available_stuff
    def make_empty(self):
        num = self.available_stuff
        self.available_stuff = 0
        return num

    def make_full(self, num):
        self.available_stuff += num

    def cumulitive_prob(self, probs):
        probability = []
        n = 0
        for p in probs:
            probability.append([n, n+p])
            n += p
        return probability

    def set_priority_demad(self, demand_list, prob_demand_list, day_list=0,day_probs=0):
        if day_list !=0:
            day_probs= self.cumulitive_prob(day_probs)
            prob_days_demand = []
            for p in prob_demand_list:
                prob_demand = self.cumulitive_prob(p)
                prob_days_demand.append(prob_demand)
            self.probs_demand=[day_list,day_probs,demand_list,prob_days_demand]
        else:
            prob_demand = self.cumulitive_prob(prob_demand_list)
            self.probs_demand = [demand_list,prob_demand]

    def set_priority_load(self, day_list , prob_list):
        probability = []
        n = 0
        for p in prob_list:
            probability.append([n, n+p])
            n += p

        self.probs_load = [probability,day_list]

    def get_demand_num(self):
        if len(self.probs_demand) == 2:
            rnd = random.random()
            prob_demand = self.probs_demand[1]
            for i in range(len(prob_demand)):
                if prob_demand[i][0]<= rnd <= prob_demand[i][1]:

                    return self.probs_demand[0][i]

        else:
            rnd = random.random()
            day_probs = self.probs_demand[1]
            for i in range(len(day_probs)):
                if day_probs[i][0]<= rnd <= day_probs[i][1]:
                    day = i

            rnd = random.random()
            prob_demand = self.probs_demand[3][day]
            for i in range(len(prob_demand)):

                if prob_demand[i][0]<= rnd <= prob_demand[i][1]:
                    return self.probs_demand[2][i]

    def get_load_day(self):
        if self.probs!=[]:
            rnd = random.random()
            for i in range(len(self.probs[0])):
                l = self.probs[0][i]
                if l[0] <= rnd <= l[1]:
                    return self.probs[1][i]
        else:
            return 0













