class Node:
    def __init__(self, val= 0, prev = None, next=None):
        self.val = val
        self.prev= prev
        self.next = next

class DoublyLinkedList:
    def __init__(self,array = []):
        self.head = None
        self.tail = None
        self.n = 0
        if len(array) > 0:
            self.convert(array)

    def insertBeginning(self,val):
        newNode = Node(val,None,self.head)
        self.head.prev = newNode
        self.head = newNode
        self.n += 1
        
    def insertEnd(self,val):
        self.tail.next = cur
        cur = Node(val,self.tail,None)
        self.tail = cur
        self.n += 1
    
    def insertAfter(self,index,val):
        cur = self.head
        i = 0
        while i < index:
            cur = cur.next
            i += 1

        next = cur.next
        cur.next = Node(val,cur,next)
        next.prev = cur.next
        self.n += 1
    
    def deleteNode(self,node):
        #update prev and next nodes
        if node.prev == None:
            self.head = self.head.next
            self.head.prev = None
        else:
            if node.next == None:
                self.tail.prev.next = None
                self.tail = self.tail.prev
            else:
                prev = node.prev
                next = node.next
                prev.next = next
                next.prev = prev
        self.n -= 1

    def reverse(self):
        modified = 0
        if self.n > 0:
            cur = self.head
            prev = cur.prev
            next = cur.next
            while modified < self.n:
                modified += 1
                next = cur.next
                cur.prev,cur.next = cur.next,prev
                # print("cur: ",cur.val)
                # if cur.prev == None:
                #     print("prev: None")
                # else:
                #     print("prev: ",cur.prev.val)
                # if cur.next == None:
                #     print("next: None")
                # else:
                #     print("next: ",cur.next.val)

                prev = cur
                cur = next
              
        self.head,self.tail = self.tail, self.head

    def convert(self,array):
        self.head = Node(None,None,None)
        self.n = 0
        if len(array) > 0:
            self.head.val = array.pop(0)
            self.n += 1
            cur = self.head
            prev = cur
            while len(array) > 0:
                cur.next = Node(array.pop(0),prev,None)
                prev = cur
                cur = cur.next
                self.n += 1
            self.tail = cur
    
    def print(self):
        cur = self.head
        array = []
        while cur != None:
            array.append(cur.val)
            cur = cur.next
        return array

converted = DoublyLinkedList([1,2,3,4])
converted.reverse()
print(converted.print())

