class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node('alpha')
b = Node('beta')
c = Node('charlie')
d = Node('delta')

a.next = b
b.next = c
c.next = d
#a > b > c > d > None

#Traversal Algorith for Linked List
def printList(head):
    current = head
    while current:
        print(current.data)
        current = current.next

#LinkedList traversal recursively
  
def traverseRecursive(head):
    if head:
        print(head.data)
        traverseRecursive(head.next)

traverseRecursive(a)






printList(a)
