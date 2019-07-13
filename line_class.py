from heapq import heappop, heappush


class Line:
    def __init__(self, num = 0):
        self.length = num
        self.heap_queue = []

    def add(self, event):
        if len(self.heap_queue)!= num:
            self.length += 1
            heappush(self.heap_queue,event)

    def remove(self):
        if len(self.heap_queue)>0:
            self.length -= 1
            return heappop(self.heap_queue)

    def size(self):
        return len(self.heap_queue)

    def is_full(self):
        if self.num == 0:
            return False
        else:
            return len(self.heap_queue) == self.length
