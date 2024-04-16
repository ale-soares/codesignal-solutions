# https://app.codesignal.com/arcade/intro/level-2/xzKiBHjhoinnpdh6m

# You are given a two-digit integer n. Return the sum of its digits.

# Example

# For n = 29, the output should be
# solution(n) = 11.

def solution(n):
  digits = [int(d) for d in str(n)]
  sum = 0
  
  for i in range(len(digits)):
    sum += digits[i]
  
  return sum