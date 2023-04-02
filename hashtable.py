class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self,node):
        self.head = node
        
class MyHashMap(object):

    def __init__(self):
        self.hashMap = [None,None,None,None,None,None,None,None,None,None]
        self.m = 10

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        index = key % self.m
        if self.hashMap[index] != None:
            cur = self.hashMap[index].head
            prev = None
            inserted = False
            while cur != None:
                if cur.key == key:
                    cur.val = value
                    inserted = True
                    break
                prev = cur
                cur = cur.next
            if not inserted:
                prev.next = Node(key,value)
            
        else:
            self.hashMap[index] = LinkedList(Node(key,value))
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        index = key % self.m
        cur = self.hashMap[index]
        if cur != None:
            cur = cur.head
        while cur != None:
            if cur.key == key:
                return cur.val
            else:
                cur = cur.next
        return -1
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = key % self.m
        cur = self.hashMap[index]
        if cur != -1:
            cur = cur.head
        prev = None
        while cur != None:
            if cur.key == key:
                if prev == None:
                    self.hashMap[index] = None
                    break
                else:
                    next = cur.next
                    prev.next = next
                    break
            else:
                 cur = cur.next


      
# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
print(obj.get(3))
obj.put(2, 1)
print(obj.get(2))
obj.remove(2)
print(obj.get(2))