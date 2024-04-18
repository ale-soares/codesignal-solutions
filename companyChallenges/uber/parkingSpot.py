# https://app.codesignal.com/company-challenges/uber/XHNFMPBYsqNyhx9PP

# This time you are an Uber driver and you are trying your best to park your car in a parking lot.
# Your car has length carDimensions[0] and width carDimensions[1]. You have already picked your lucky spot (rectangle of the same size as the car with upper left corner at (luckySpot[0], luckySpot[1])) and bottom right corner at (luckySpot[2], luckySpot[3]) and you need to find out if it's possible to park there or not.
# It is possible to park your car at a given spot if and only if you can drive through the parking lot without any turns to your lucky spot (for safety reasons, the car can only move in two directions inside the parking lot - forwards or backwards along the long side of the car) starting from some side of the lot (all four sides are valid options).
# Naturally, you can't park your car if the lucky spot is already occupied. The car can't drive through or park at any of the occupied spots.

# Example

# For carDimensions = [3, 2],

# parkingLot = [[1, 0, 1, 0, 1, 0],
#               [0, 0, 0, 0, 1, 0],
#               [0, 0, 0, 0, 0, 1],
#               [1, 0, 1, 1, 1, 1]]
# and luckySpot = [1, 1, 2, 3], the output should be solution(carDimensions, parkingLot, luckySpot) = true.

def solution(carDimensions, parkingLot, luckySpot):
    spot_upper_left = (luckySpot[0], luckySpot[1])
    spot_lower_right = (luckySpot[2], luckySpot[3])
    
    # check if lucky spot is empty
    if not is_empty(parkingLot, spot_upper_left, spot_lower_right): return False
    
    # check if lucky spot is positioned horizontally or vertically
    is_horizontal = luckySpot[3] - luckySpot[1] > luckySpot[2] - luckySpot[0]
    
    # if is horizontal, check if left or right rectangles are empty
    if is_horizontal:
        is_left_empty = is_empty(parkingLot, (luckySpot[0], 0), (luckySpot[2], luckySpot[1]))
        is_right_empty = is_empty(parkingLot, (luckySpot[0], luckySpot[3]), (luckySpot[2], len(parkingLot[0]) - 1))
    
        return is_left_empty or is_right_empty
    # if its vertical, check if top or bottom rectangles are empty
    else:
        is_top_empty = is_empty(parkingLot, (0, luckySpot[1]), (luckySpot[0], luckySpot[3]))
        is_bottom_empty = is_empty(parkingLot, (luckySpot[2], luckySpot[1]), (len(parkingLot) - 1, luckySpot[3]))
    
        return is_top_empty or is_bottom_empty

# helper func to check if a given rectangle is empty
def is_empty(lot, ul, lr):
    for i in range(ul[0], lr[0] + 1):
        for j in range(ul[1], lr[1] + 1):
            if lot[i][j] == 1: return False
            
    return True
