class Node:
    def __init__(self,value):
        self.value =  value
        self.next = None

class Stack:
    def __init__(self):
        self.topmostNode = None
    
    def push(self,value):
        newNode = Node(value)
        newNode.next = self.topmostNode
        self.topmostNode = newNode
    
    def pop(self):
        self.topmostNode = self.topmostNode.next