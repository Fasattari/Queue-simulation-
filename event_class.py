class Event:
    def __init__(self, time, type, phase=0, server=0, entity=0,inventory=0,num=0):
        self.time = time
        self.type = type
        self.phase = phase
        self.server = server
        self.entity = entity
        self.inventory = inventory
        self.num = num

    def get_time(self):
        return self.time

    def get_server(self):
        return self.server

    def get_type(self):
        return self.type

    def get_phase(self):
        return self.phase

    def get_entity(self):
        return self.entity

    def get_tuple_event(self):
        if self.phase == 0:
            event_tuple = (self.time, self.type, self.inventory, self.num)
        else:
            event_tuple = (self.time, self.type, self.phase, self.server, self.entity)
        return event_tuple

    def get_inventory(self):
        return self.inventory

    def get_num(self):
        return self.num