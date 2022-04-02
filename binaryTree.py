#create a node class

from json.encoder import INFINITY   #code to import infinity


class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


## Depth First Search

# Implementing the DFS algorithm ITTERATIVELY

def depthFirstSearch(root):
    #if the root is none return an empty list
    result = []
    if root is None:
        return result
    stack = [root]

    while len(stack) > 0:
        current = stack.pop()
        result.append(current.val)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return result


# Implementing the DFS with a RECURSIVE solution

def depthFirstSearchRecurssive(root):
    
    if root is None:
        return []
    
    leftValues = depthFirstSearchRecurssive(root.left)
    rightValues = depthFirstSearchRecurssive(root.right)
    return(leftValues + [root.val] + rightValues)
    

## Implementing the BFS algorithm
# Implementing the BFS algorithm ITTERATIVELY

def breadthFirstSearch(root):
    result = []
    #if the root is none return empty
    if root == None:
        return result
    #create a queue
    queue = [root]

    while len(queue)>0:
        current = queue.pop(0)
        result.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result


# Create a funtion to check if a value exists in a binary tree

#Itterative breadth first search

def treeIncludes(root, target):
    if root is None:
        return False
    queue = [root]
    while len(queue) > 0:
        current = queue.pop(0)
        if current.val == target:
            return True

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)        

    return False

#Recursive depth first treeIncludes
#returns true if the target is in the tree

def treeIncludesRecursive(root, target):
    if root is None:
        return False
    if root.val == target:
        return True
    return treeIncludesRecursive(root.left, target) or treeIncludesRecursive(root.right, target)


## Create a Tree Sum for a binary tree

#Recursive treeSum

def treeSumRecursive(root):
    if root is None:
        return 0
    return root.val + treeSumRecursive(root.left) + treeSumRecursive(root.right)

#Iiterative treeSum
def treeSumIterative(root):
    if root is None:
        return 0
    sum = 0
    queue = [root]

    while len(queue) > 0:
        current = queue.pop(0)
        sum += current.val
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return sum


## Create a recursive code function to find the minimum value in a binary tree

#Itterative solution

def minValIter(root):
    smallest = INFINITY
    stack = [root]
    if root is None:
        return None
    while len(stack) > 0:
        current = stack.pop()
        if current.val < smallest:
            smallest = current.val
        
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    return smallest


#creating a binary tree            
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
g.right = None
#      a
#    /   \
#   b     c
#  / \   / \
# d   e f

#create a binary tree of integers

aa = Node(20)
bb = Node(23)
cc = Node(19)
dd = Node(4)
ee = Node(15)

aa.left = bb
aa.right = cc
bb.left = dd
bb.right = ee


       
#print(depthFirstSearch(g))
#print(depthFirstSearchRecurssive(a))
#print(breadthFirstSearch(a))
#print(treeIncludes(a, 'm'))
#print(treeIncludesRecursive(a, 'f'))
print(treeSumRecursive(aa))
print(minValIter(aa))