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

#Using Decorators for memoizing 
#Decorators are functions that modify other functions

memory = {}
def memoize(f):
     
    # This inner function has access to memory
    # and 'f'
    def inner(num):
        if num not in memory:        
            memory[num] = f(num)
        return memory[num]
    return inner

@memoize
def dynamicFib(n): 
    if n <= 2:
        return 1
    return dynamicFib(n-1) + dynamicFib(n-2)

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


##Memoize grdiTraveller using decorators in Pyhton
memo ={}
def gridMemoize(f):
    def inner(n, m):
        key = str(n) + ',' + str(m)
        if key not in memo:
            memo[key] = f(n, m)
        return memo[key]
    return inner

@gridMemoize
def gridTravellerMemo(n, m):
    if n == 1 and m == 1:
        return 1
    if n == 0 or m == 0:
        return 0
    return gridTravellerMemo(m-1, n) + gridTravellerMemo(n-1, m)





##Problem 3: Write a function 'canSum(target, numbers)' 
#That returns a Boolean indicating whether or not it is possible to generate targetSum usingnumbers from the array.
#We can use an element in the array as many times as needed
#All Inputs will be positive integers

#brute force recursive solution
def canSum(target, array):
    if target == 0:
        return True
    if (target < 0) or (len(array) == 0):
        return False
    for num in array:
        remainder = target - num
        if canSum(remainder, array) == True:
            return True
    return False

#Using memoization
memo = {}
def canSumMemo(target, array):
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if (target < 0) or (len(array) == 0):
        return False

    for num in array:
        remainder = target - num
        if canSumMemo(remainder, array) == True:
            memo[target] = True
            return True

    memo[target] = False
    return False







##Tests

#print(dynamicFib(81))
#print(fib(50))
#print(gridTraveller(2, 3))
#print(gridTraveller(36, 36))
#print(gridTravellerMemo(36, 36))
print(canSum(7, [2,3]))
print(canSum(7, [2, 4]))
#print(canSum(300, [7, 14]))
print(canSumMemo(300, [7, 14]))


