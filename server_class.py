from distribution_class import *
from line_class import *


class Server:
    def __init__(self, dist_st, line=Line(), capacity=1):
        self.state = 0  # 0 idle 1 busy
        self.served = 0
        self.capacity = capacity
        self.serverLine = line
        self.dist_st = dist_st

    def get_service_time(self):
        service_time = self.dist_st.get_num()
        #service_time = random.randint()
        return service_time

    def set_busy(self):
        self.served += 1
        if self.served == self.capacity:
            self.state = 1

    def set_free(self):
        self.served -= 1
        if self.served < self.capacity:
            self.state = 0

    def get_state(self):
        return self.state

    def add_line(self, event):
            self.serverLine.add(event)

    def is_full(self):
        return self.serverLine.is_full()

    def get_event_in_line(self):
        return self.serverLine.remove()

    def get_size(self):
        return self.serverLine.size()
