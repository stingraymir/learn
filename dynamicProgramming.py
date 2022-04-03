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

def dynamicFib(n):
    #initialize a Dict(hash map) for which keys are argument to the function and values are the return value
    memo = {}
    if n in memo:
        return memo[n]
    if n <= 2: 
        return 1
    #store the value in the dictionary
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]










print(fib(30))
print(dynamicFib(30))