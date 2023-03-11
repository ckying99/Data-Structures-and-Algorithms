class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
     
class List:
    def __init__(self):
        self.firstNode = None
        self.lastNode = None
    def push(self,data):
        newNode = Node(data)
        if self.firstNode != None:
            self.lastNode.next = newNode
            self.lastNode = newNode
        else:
            self.firstNode = newNode
            self.lastNode = newNode
    def length(self):
        node = self.firstNode
        count = 0
        while node != None:
            count += 1
            node = node.next

        return count
    
aList = List()
aList.push(1)
aList.push(2)
aList.push(3)
aList.push(4)
print(aList.length())