# priority queue doesn't have front or back, it's just a bag with priority value,
# when you call the following function it deletes the node with highest priority within the priority queue

# def extractMax(self):
    # if len(self.queue) > 0:
    #     max = self.queue[0]
    #     for i in range(1,len(self.queue)):
    #         element = self.queue[i]
    #         if element > max:
    #             max = element
class MyHeapQueue:
    def __init__(self):
        self.queue = []
    
    def pushBack(self,element):
        self.queue.append(element)
    
    def popFront(self):
        self.queue.pop(0)
    
    
