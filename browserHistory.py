class Node:
    def __init__(self,val,prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.homepage = Node(homepage)
        self.cur = self.history.head
        return None

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        prev = self.cur
        cur = Node(url,self.cur)
        prev.next = cur
        self.cur = cur
        return None
    
    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps > 0 and self.cur != None:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps > 0 and self.cur.next != None:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val
seq = []
obj = BrowserHistory("leetcode.com")
seq.append(obj)
seq.append(obj.visit("google.com"))
seq.append(obj.visit("facebook.com"))
seq.append(obj.visit("youtube.com"))
seq.append(obj.back(1))
print(seq)