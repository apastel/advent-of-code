from advent.load import read_input

def is_symbol(grid, row, col):
  if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
    return False
  return grid[row][col] in "!@#$%^&*()-_=+[{]}]|;:,<>/?"

def is_valid_part(grid, row, col):
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if is_symbol(grid, i, j):
               return True
    return False

def sum_part_numbers(grid):
  total_sum = 0
  is_part = False
  for row, line in enumerate(grid):
    current_number = ""
    is_part = False
    for col, char in enumerate(line):
      if char.isdigit():
        current_number += char
        if (not is_part):
            is_part = is_valid_part(grid, row, col)
        if is_part and col == len(line) - 1:
          total_sum += int(current_number)   
      elif current_number:
        total_sum += int(current_number) if is_part else 0
        current_number = ""
        is_part = False
  return total_sum

# Read the input file
grid = read_input(group=True)[0]

# Sum all part numbers
part_number_sum = sum_part_numbers(grid)

# Print the result
print(f"Sum of all part numbers: {part_number_sum}")
