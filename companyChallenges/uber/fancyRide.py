# https://app.codesignal.com/company-challenges/uber/4c3qzzQg8Zg9AfLKH

# Being a new Uber user, you have $20 off your first ride. You want to make the most out of it and drive in the fanciest car you can afford, without spending any out-of-pocket money. There are 5 options, from the least to the most expensive: "UberX", "UberXL", "UberPlus", "UberBlack" and "UberSUV".
# You know the length l of your ride in miles and how much one mile costs for each car. Find the best car you can afford.

# Example

# For l = 30 and fares = [0.3, 0.5, 0.7, 1, 1.3], the output should be
# solution(l, fares) = "UberXL".

# The cost for the ride in this car would be $15, which you can afford, but "UberPlus" would cost $21, which is too much for you.

import math

def solution(l, fares):
  limit = 20
  options = ["UberX", "UberXL", "UberPlus", "UberBlack", "UberSUV"]
  cost_per_option = {}
  
  for i in range(len(fares)):
    cost = math.ceil(l * fares[i])
    cost_per_option[options[i]] = cost
    
    if cost_per_option[options[i]] <= limit:
      best_option = options[i]
      
  return best_option