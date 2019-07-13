from distribution_class import *
from entity_class import *


class Create:

    def __init__(self, dist_at=Distribution(), input_entity=[], num_entity=-1):
        self.num_entity = num_entity
        self.created_num = 0
        self.dist_at = dist_at
        self.input_entity = input_entity

    def create(self):
        if self.num_entity == -1:
            ar = self.dist_at.get_num()
            if len(self.input_entity) == 0:
                en = Entity('cst', self.created_num)
            elif self.created_num != len(self.input_entity):
                en = self.input_entity[self.created_num][1]
            else:
                return []

        else:
            ar = self.dist_at.get_num()
            if len(self.input_entity) == 0 and self.created_num != self.num_entity:
                en = Entity('cst', self.created_num)
            elif self.created_num != self.num_entity:
                en = self.input_entity[self.created_num][1]
            else:
                return []
        self.created_num += 1
        print "en in create: ", en
        return [en, ar]










