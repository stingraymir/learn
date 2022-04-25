#valid palindrome 2

def isPalindrome(string):
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return isPalindrome(string[1:-1])
    return False

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

#write s function to 

    


