# Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

# Example

# For inputArray = [3, 6, -2, -5, 7, 3], the output should be
# solution(inputArray) = 21.

# 7 and 3 produce the largest product.

def solution(inputArray):
  l, r = 0, 1
  max_product = inputArray[l] * inputArray[r]
  
  while r <= len(inputArray) - 1:
    product = inputArray[l] * inputArray[r]
    max_product = max(max_product, product)
    
    l += 1
    r += 1
      
  return max_product