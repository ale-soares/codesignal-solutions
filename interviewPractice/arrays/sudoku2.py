import collections

def solution(grid):
  # Create dictionaries to keep track of numbers in rows, columns, and sub-boxes
    rows = collections.defaultdict(set)
    columns = collections.defaultdict(set)
    boxes = collections.defaultdict(set)

    # Iterate through each cell in the 9x9 Sudoku grid
    for row in range(9):
      for col in range(9):
        num = grid[row][col]

        # Skip empty cells represented by "."
        if num == ".": continue

        # Check if the current number violates Sudoku rules
        if (num in rows[row] or 
            num in columns[col] or 
            num in boxes[(row // 3, col // 3)]):
            return False

        # Update sets to keep track of encountered numbers
        rows[row].add(num)
        columns[col].add(num)
        boxes[(row // 3, col // 3)].add(num)

    # If all cells satisfy Sudoku rules, the grid is valid
    return True
