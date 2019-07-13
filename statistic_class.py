import matplotlib.pyplot as plt

class Statistic:
    def __init__(self):
        self.stat_list = [] # events_list
        self.entity_dict = dict() # {entity_i : event_a_i , event_d_i}
        self.num_entity_in = 0 # number of entity in system
        self.end_time = 0 # time of the end of system
        self.start_time = 0 # time of the start system
        self.num_entity_dict = dict() # { time_i : number of entity in time i}

    def set_end_time(self, time):
        self.end_time = time

    def set_start_time(self, time):
        self.start_time = time

    def change_num_entity(self, num, time):
        self.num_entity_in += num
        self.num_entity_dict[time] = self.num_entity_in

    def add_statistic(self, stat):
        self.stat_list.append(stat)

    def get_statistic(self):
        return self.stat_list

    def sort_entity(self):
        entity_set = set()
        for event in self.stat_list:
            print event
            entity_set.add(event[4])


        for en in entity_set:
            self.entity_dict[en] = [event for event in self.stat_list if event[4] == en]

    def get_l_t(self,time):
        num = 0
        for i in range(self.num_entity_dict.keys()):
            if self.num_entity_dict.keys() > time:
                key = self.num_entity_dict.keys()[i-1]
                num = self.num_entity_dict[key]
        return num

    def get_p_n(self, num):
        times_num = 0
        keys = self.num_entity_dict.keys()
        for i in range(len(keys)):
            key = keys[i]
            if self.num_entity_dict[key] >= num:
                if i != len(keys)-1:
                    times_num += keys[i+1]-key
                else:
                    times_num += self.end_time - key

        return float(times_num)/(self.end_time - self.start_time)


    def get_a_n(self, num):
        entities = self.entity_dict.keys()
        second_customer = self.entity_dict[entities[num]]
        first_customer = self.entity_dict[entities[num-1]]
        s = second_customer[0][0]
        f = first_customer[0][0]
        a_n = s - f
        return a_n

    def get_s_n(self, num):
        entities = self.entity_dict.keys()
        st = entities[num].get_st()
        return st

    def get_w_n(self, num):

        entities = self.entity_dict.keys()
        ar_and_departure = self.entity_dict[entities[num]]
        w_n = 0
        for i in range(1, len(ar_and_departure), 2):
            w_n += ar_and_departure[i][0]-ar_and_departure[i-1][0]

        return w_n

    def get_l_t(self, time):
        num = 0
        for i in range(len(self.num_entity_dict.keys())):
            if self.num_entity_dict.keys() > time:
                key = self.num_entity_dict.keys()[i-1]
                num = self.num_entity_dict[key]

        return num

    def plot_num_entity_time(self):
        time = self.num_entity_dict.keys()
        num = self.num_entity_dict.values()
        plt.bar(time, num)

        plt.show()

    def plot_server_utilization(self, servers, labels):
        time = self.end_time - self.start_time
        server_ut =[]
        for s in servers:
            l = [item for item in self.stat_list if item[3] == s and item[1] == 'D']
            st_s = 0
            for event in l:
                st_s += event[4].get_st()
            server_ut.append(int((float(st_s)/time)*100))

        plt.bar([0, 1], server_ut, align='center', width=0.1)
        plt.show()



    def plot_server(self, servers, labels):
        server_cols = []
        for s in servers:
            server_col = len([item for item in self.stat_list if item[3] == s and item[1] == 'D'])
            server_cols.append(server_col)

        plt.pie(server_cols, None, labels)
        plt.show()
