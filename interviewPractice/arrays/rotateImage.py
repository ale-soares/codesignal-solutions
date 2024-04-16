# https://app.codesignal.com/interview-practice/question/5A8jwLGcEpTPyyjTB/description

# Note: Try to solve this task in-place (with O(1) additional memory), since this is what you'll be asked to do during an interview.

# You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

# Example

# For

# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]

# the output should be:

# solution(a) = [[7, 4, 1],
#                [8, 5, 2],
#                [9, 6, 3]]

from typing import List

# CodeSignal Solution | Ref: https://medium.com/@silasburger/problem-link-https-leetcode-com-problems-rotate-image-d967fdcbec71
def solution(a):
  n = len(a)
  
  for row in range(n):
    for col in range(row, n):
      a[row][col], a[col][row] = a[col][row], a[row][col]

  for row in a:
    reverse(row)

  return a
    
def reverse(row):
  p1 = 0
  p2 = len(row) - 1
  
  while p1 < p2:
    row[p1], row[p2] = row[p2], row[p1]
    p1 = p1 + 1
    p2 = p2 - 1

  return row

# Neetcode Solution
class Solution:
  def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    l, r = 0, len(matrix) - 1

    while l < r:
      for i in range(r - l):
        top, bottom = l, r

        # save the top left
        topLeft = matrix[top][l + i]

        # move bottom left into top left
        matrix[top][l + i] = matrix[bottom - i][l]
        # move bottom right into bottom left
        matrix[bottom - i][l] = matrix[bottom][r - i]
        # move top right into bottom right
        matrix[bottom][r - i] = matrix[top + i][r]
        # move top left into top right
        matrix[top + i][r] = topLeft
          
      r -= 1
      l += 1
      