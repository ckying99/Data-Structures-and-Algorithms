# Definition for singly-linked list.
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    firstNumber = getNumber(l1)
    secondNumber = getNumber(l2)
    c = [int(i) for i in str(firstNumber+secondNumber)]
    return convert(c)

def getNumber(linkedList):
    digits = []
    cur = linkedList
    n = 0
    while cur != None:
        digits.insert(0,cur.val)
        cur = cur.next
        n += 1
    total = 0
    for num in digits:
        total += num*(pow(10,n-1))
        n -= 1
    return total

def convert(aList):
    start = ListNode(aList.pop(),None)
    linkedList = start
    while len(aList) > 0:    
        new = ListNode(aList.pop(),None)
        linkedList.next = new
        linkedList = linkedList.next
    
    return start


