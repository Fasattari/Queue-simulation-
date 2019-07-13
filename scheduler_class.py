from heapq import heappop, heappush
from enviroment_class import *
from statistic_class import *
from event_class import *

class Scheduler:

    def __init__(self, env, clock=0, statistic=Statistic(), day=0):
        self.FEL = []
        self.clock = clock
        self.env = env
        self.output = []
        self.statistic = statistic
        self.day = day

    def set_clock(self, time):
        self.clock += time

    def add_event(self, event):
        time = event.get_time()
        heappush(self.FEL, (time, event))

    def set_stop_event(self):
        stop_time = self.env.get_stop()
        if stop_time != 0:
            event = Event(stop_time, 'S', 0, 0, 0)
            self.add_event(event)
    def set_start_event(self):
        print "in start_event"
        print self.env.get_first_phase()
        print self.env.get_inventory()
        if self.env.get_first_phase() != 0:
            print "set arrival event"
            event = Event(self.clock, 'A', self.env.get_first_phase(), 0, self.env.create_entity()[0])
            self.add_event(event)

        elif self.env.get_inventory() != 0:
            print "set day event"
            event = Event(self.clock, 'DY', inventory=self.env.get_inventory())
            self.add_event(event)

    def switch_event(self, event):
        event_type = event.get_type()
        print "event_type ",event_type," event:",event.get_tuple_event()
        if event_type == 'A': #arrival_event
            self.statistic.change_num_entity(1, self.clock)
            self.arrival_process(event)
        elif event_type == 'D': #departure_event
            self.statistic.change_num_entity(-1, self.clock)
            self.departure_process(event)
        elif event_type == 'C': #check_event
            self.check_process(event)
        elif event_type == 'L': #load_event
            self.load_process(event)
        elif event_type == 'DE': #demand_event
            self.demand_process(event)
        elif event_type == 'SC': #scrap_event
            self.scrap_process(event)
        elif event_type == 'DY': #day_event
            self.day_process(event)
        else:
            self.end(event)

    def create_new_arrival(self):
        create_new_entity = self.env.create_entity()
        if create_new_entity != []:
            time = self.clock + create_new_entity[1]
            event = Event(time, 'A', self.env.get_first_phase(), 0, create_new_entity[0])
            self.add_event(event)

    # tuple(t,D/A,phase,server,customer)
    def arrival_process(self, event):
        server = event.get_phase().getServer()
        tuple_event = event.get_tuple_event()

        if server.get_state() == 0:
            st =  server.get_service_time()
            event.get_entity().set_st(st)
            time = self.clock + st
            server.set_free()

            event = Event(time, 'D', event.get_phase(), server, event.get_entity())
            self.add_event(event)

        else:
            tuple_event.add(True)
            server.add_line(event)

        self.statistic.add_statistic(tuple_event)
        self.create_new_arrival()

        self.print_event(event)

    def departure_process(self, event):

        server = event.get_server()
        self.statistic.add_statistic(event.get_tuple_event())
        if server.get_size() == 0:
            server.set_free()
            phase = self.env.get_next_phase(event.get_phase())
            if phase.get_index() != 0:
                event = Event(self.clock, 'A', phase, 0, event.get_entity())
                self.add_event( event)

            else:
                self.output.append((event.get_time(), event.get_entity()))

        else:
            event = server.get_event_in_line()
            st =  event.get_server().get_service_time()
            event.get_entity().set_st(st)
            time = self.clock + st
            event = Event(time, 'D', event.get_phase(), event.get_server(), event.get_entity())
            self.add_event(event)

        self.print_event(event)
    # tuple(t,type,inv,num)
    def day_process(self, event):
        event_tomorrow = Event(self.clock+self.day, 'DY', inventory=event.get_inventory())
        self.add_event(event_tomorrow)
        print "inv in day", event.get_inventory()
        num = event.get_inventory().get_demand_num()
        print "num",num
        event_demand = Event(self.clock, 'DE', inventory=event.get_inventory(), num=num)
        self.add_event(event_demand)
        if event.get_inventory().get_cost_scrap() != -1:
            event_scrap = Event(self.clock, 'SC', inventory=event.get_inventory())
            self.add_event(event_scrap)

    def demand_process(self, event):
        event.get_inventory().dec_available_stuff(event.get_num())

    def check_process(self, event):
        inventory = event.get_inventory()
        num = inventory.get_needs()
        day = inventory.get_load_day()
        event_load = Event(self.clock+self.day*day, 'L', inventory=inventory, num=num)
        self.add_event(event_load)

    def load_process(self, event):
        inventory = event.get_inventory()
        inventory.make_full(event.get_num())

    def scrap_process(self, event):
        inv = event.get_inventory()
        print "inv in scrap ",inv
        num = inv.make_empty()

    def end(self, event):
        del self.FEL[:]

    def start(self):

        self.statistic.set_start_time(self.clock)
        self.set_start_event()
        self.set_stop_event()

        while len(self.FEL) != 0:
            event = heappop(self.FEL)
            self.clock = event[0]
            self.switch_event(event[1])

        self.statistic.set_end_time(self.clock)

    def print_event(self, event):
        print "-------------event-------------"
        print "time: ", event.get_time()
        print "type: ", event.get_type()
        if event.get_phase() == 0:
            print "phase: ", event.get_phase()
        else:
            print "phase: ", event.get_phase().get_index(), " "
        print "server: ", event.get_server(), " "
        if event.get_entity() == 0:
            print "customer: ", event.get_entity()
        else:
            print "customer: ", event.get_entity().get_index()

    def get_output(self):
        return self.output

    def get_statistics(self):
        return self.statistic
