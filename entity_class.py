class Entity:
    def __init__(self, name, index):
        self.name = name
        self.index = index
        self.st = 0

    def set_st(self, num):
        self.st += num

    def get_st(self):
        return self.st

    def set_index(self, index):
        self.index = index

    def get_index(self):
        return self.index
