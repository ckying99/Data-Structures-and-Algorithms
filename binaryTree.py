class Node:
    def __init__(self,val,left,right):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self,val):
        self.root = Node(val,None,None)
    
    def bfs(self):
        pass

    def dfs(self,root):
        #base case [] [1] 
        cur = root
        if root != None:
            cur = cur.left
        stack = [cur]
        ascList = []
        while len(stack) > 0:
            if cur != None:
                stack.append(cur)
                cur = cur.left
            if len(stack) > 0:
                ascList.append(stack.pop())
            
    def insert(self,val):
        cur = self.root
        while cur != None:
            if val <= cur.val:
                cur = cur.left
            else:
                cur = cur.right
        if cur == None:
            cur = Node(val)
    
    def search(self,val):
        cur = self.root
        while cur != None:
            if val < cur.val:
                cur = cur.left
            elif val > cur.val:
                cur = cur.right
            else:
                return True
        return False

    def remove(self,val):
        cur = self.root
        while cur != None:
            if cur.val == val:
                if cur.right != None:
                    left = cur.left
                    cur = cur.right
                    if left != None:
                        while cur != None:
                            cur = cur.left
                        cur = left
                    break
                elif cur.left != None:
                    cur = cur.left
                    break
                else:
                    cur = None
            elif val < cur.val:
                cur = cur.left
            else:
                cur = cur.right

a = Tree(1)
b = Node(1,None,None)
a.root = b
print(a.dfs(a.root))

