# https://app.codesignal.com/company-challenges/uber/tucq8L9FB7QyDZ4M6

# Consider a big city located on n islands. There are bridges connecting the islands, but they all have only one-way traffic. To make matters worse, most of the bridges are closed at night, so there is at most one bridge with traffic going from any island A to any other island B.
# There is a programmer who turns a penny by working nights as an Uber driver. One night his phone dies right after he picks up a rider going from island 0 to island (n - 1). He has the map of the city bridges in his laptop though (stored as a matrix of distances), so he decides to implement an algorithm that calculates the shortest path between those two islands and evaluate the cost based on the distance of the path. Assume that each mile of the trip is 1$.

# Example

# For

# city = [[-1, 5, 20],
#         [21, -1, 10],
#         [-1, 1, -1]]
# the output should be solution(city) = 15.

# city[i][j] equals the distance between the ith and the jth islands in miles, or -1 if there is no bridge by which one can move from island i to island j.
# solution(city) should be 15, since the shortest distance from the 0th to the 2nd island is 15. The distance from the 0th to the 1st is city[0][1] = 5, and from the 1st to the 2nd is city[1][2] = 10.

def solution(city):
  return shortest(city, 0, set())
    
def shortest(city, cur, visited):
  # if already in the last island
  if cur == len(city) - 1: return 0

  # if not in last island
  best = None
  # try all possible nodes that are reachable from the current one
  for nxt, d in enumerate(city[cur]):
    # check if next node has not already been visited
    # and if there is a bridge between the islands
    if nxt not in visited and d != -1:
      visited.add(nxt)
      path_from_nxt_to_n = shortest(city, nxt, visited)
      visited.remove(nxt)
      
      # check if there is a path from next to n
      if path_from_nxt_to_n is not None:
        # d = path from the current node to the next node
        path_from_cur_to_n = path_from_nxt_to_n + d
        # check if best pass can be updated (update if it is shorter)
        if best is None or path_from_cur_to_n < best:
          best = path_from_cur_to_n
              
  return best
