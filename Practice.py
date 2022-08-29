#valid palindrome 2
#using recursion

def isPalindrome(string):
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return isPalindrome(string[1:-1])
    return False

#reversing the string in place
def isPalin(string):
  if string[::-1] == string:
    return True
  return False


def validParenthesis(string):
  stack = []
  for char in string:
    if char == '(':
      stack.append('(')
    elif char == ')':
      if not stack:
        return False
      stack.pop()
  return not stack

def validBracket(string):
  stack = []
  open = ['(', '{', '[']
  close = [')', '}', ']']
  for char in string:
    if char in open:
      stack.append(char)
    elif char in close:
      if not stack:
        return False
      if open.index(stack.pop()) != close.index(char):
        return False
  return not stack

#write a function to delete node in a linked list
def deleteNode(node):
  node.data = node.next.data
  node.next = node.next.next

#Given the head of a linked list, remove the nth node from the end of the list and return its head
def removeNthFromEnd(head, n):
  if not head:
    return None
  if not head.next:
    return None
  if n == 1:
    return head.next
  curr = head
  for i in range(n-1):
    curr = curr.next
  prev = head
  while curr.next:
    prev = prev.next
    curr = curr.next
  prev.next = prev.next.next
  return head


  #Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0
def reverse(x):
  if x == 0:
    return 0
  if x < 0:
    x = -x
  rev = 0
  while x:
    rev = rev * 10 + x % 10
    x = x // 10
  if rev > 2**31 - 1 or rev < -2**31:
    return 0
  return rev if x > 0 else -rev

  #define a linked list
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

#longest palindromic substring
def longestPalindrome(s):
  if not s:
    return ""
  if len(s) == 1:
    return s
  max_len = 1
  start = 0
  for i in range(len(s)):
    if i - max_len >= 1 and s[i - max_len - 1:i + 1] == s[i - max_len - 1:i + 1][::-1]:
      start = i - max_len - 1
      max_len += 2
      continue
    if i - max_len >= 0 and s[i - max_len:i + 1] == s[i - max_len:i + 1][::-1]:
      start = i - max_len
      max_len += 1
  return s[start:start + max_len]





#reverse a linked list

def reverseList(head):
  if not head or not head.next:
    return head
  prev = None
  curr = head
  while curr:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
  return prev



#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
def twoSum(nums, target):
  if len(nums) < 2:
    return []
  d = {}
  for i in range(len(nums)):
    if nums[i] in d:
      return [d[nums[i]], i]
    d[target - nums[i]] = i
  return []




#a function that takes as input an array and returns all the pairs of numbers in that array that equal to a particular sum
def pairSums(arr, sum)








