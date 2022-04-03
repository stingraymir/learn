## Dynamic programming problems can use recursion or tabulation
## Recursion is mostly used for Dynamic programming

## Problem 1: Write a function that takes a number as an argument and returns the n-th number of the Fibboacci sequence

#Lets define a fib recursively
#has a O(2^n) time complexity and O(n) space complexity

def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)    

#By Memoization we can store a recuurent pattern or subproblems and use it to calculate the fibonacci sequence
#This is called Dynamic programming

#initialize the memo dictionary
memo = {}
def dynamicFib(n): 
    
    if n <= 2: 
        return 1
    if n in memo:
        return memo[n]
    #store the value in the dictionary
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

# so memoization allows us to not traverse the full tree every time we call the function
# The time complexity of this method is O(n) and the space complexity is O(n)

## Problem 2: Write a function to travel to a goal on a grid of m*n dimensions
# e.g gridTraveller(2,3) returns all ways to travel from start of the grid at top left to bottom right of a 2*3 GRID
# base case is 1*1 grid
# a non memoized solution will look like fib

memoGrid = {}
def gridTraveller(n, m):
    
    key = str(n) + ',' + str(m)
    #memo = {}
    if key in memoGrid:
        return memoGrid[key]
    if n == 1 and m == 1:
        return 1
    if n == 0 or m == 0:
        return 0
    
    memoGrid[key] = gridTraveller(m-1, n) + gridTraveller(n-1, m)
    return memoGrid[key]



print(dynamicFib(50))
#print(fib(50))
#print(gridTraveller(2, 3))
#print(gridTraveller(18, 18))