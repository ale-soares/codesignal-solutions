# https://app.codesignal.com/arcade/intro/level-1/s5PbmwxfECC52PWyQ

# Given the string, check if it is a palindrome.

# Example

# For inputString = "aabaa", the output should be
# solution(inputString) = true;
# For inputString = "abac", the output should be
# solution(inputString) = false;
# For inputString = "a", the output should be
# solution(inputString) = true.

def solution(inputString):
  n = len(inputString)
  l, r = 0, n - 1
  
  while l <= r:
    if inputString[l] != inputString[r]: return False
        
    l += 1
    r -= 1
      
  return True