# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def splitListToParts(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: List[ListNode]
    """
    n = 0
    cur = head
    while cur.next != None:
        cur = cur.next
        n += 1
    
    q, r = divmod(n,k)
    

object = ListNode(1, ListNode(2,ListNode(3,ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8,ListNode(9, ListNode(10,None))))))))))

print(splitListToParts(object, 3))