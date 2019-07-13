from phase_class import *
from create_class import *
from inventory_class import *

class Environment:
    def __init__(self, create=Create()):
        self.phases = []
        self.num_phase = 0
        self.create = create
        self.stop_time = 0
        self.inventory = 0

    def add_inventory(self, inv):
        self.inventory = inv

    def get_inventory(self):
        if self.inventory !=0:
            return self.inventory
        return 0

    def add_phase(self, phase):
        self.num_phase += 1
        phase.set_index(self.num_phase)
        self.phases.append(phase)

    def get_first_phase(self):
        if self.phases!=[]:
            return self.phases[0]
        else:
            return 0

    def get_next_phase(self, phase):
        ph_index = phase.get_index()
        for p in self.phases:
            i = p.get_index()
            if i == ph_index +1 :
                return p
        p = Phase()
        return p

    def set_stop(self, time):
        self.stop_time = time

    def get_stop(self):
        return self.stop_time

    def create_entity(self):
        return self.create.create()

