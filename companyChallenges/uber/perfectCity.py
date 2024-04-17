# https://app.codesignal.com/company-challenges/uber/gsjPcfsuNavxhsQQ7

# Consider a city where the streets are perfectly laid out to form an infinite square grid. In this city finding the shortest path between two given points (an origin and a destination) is much easier than in other more complex cities. As a new Uber developer, you are tasked to create an algorithm that does this calculation.
# Given user's departure and destination coordinates, each of them located on some street, find the length of the shortest route between them assuming that cars can only move along the streets. Each street can be represented as a straight line defined by the x = n or y = n formula, where n is an integer.

# Example

# For departure = [0.4, 1] and destination = [0.9, 3], the output should be
# solution(departure, destination) = 2.7.

# 0.6 + 2 + 0.1 = 2.7, which is the answer.

import math

def solution(departure, destination):
  dep, dest = departure, destination
  
  # two points in different lines
  min_x = abs(dep[0] - dest[0])
  min_y = abs(dep[1] - dest[1])
  
  # two points in the same line
  if math.ceil(dep[0]) == math.ceil(dest[0]):
    path1 = math.ceil(dep[0]) - dep[0] + math.ceil(dest[0]) - dest[0]
    path2 = dep[0] - math.floor(dep[0]) + dest[0] - math.floor(dest[0])
    min_x = min(path1, path2)
      
  if math.ceil(dep[1]) == math.ceil(dest[1]):
    path1 = math.ceil(dep[1]) - dep[1] + math.ceil(dest[1]) - dest[1]
    path2 = dep[1] - math.floor(dep[1]) + dest[1] - math.floor(dest[1])
    min_y = min(path1, path2)
  
  return min_x + min_y