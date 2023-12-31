from advent.load import read_input
import math

# key: position (row, col) of gear
# value: list of adjacent part numbers
gear_map = {}

def is_gear(grid, row, col):
  if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
    return False
  return grid[row][col] == "*"

def is_valid_part(grid, row, col, gear_pos):
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if is_gear(grid, i, j):
              gear_pos = (i, j)
              return (True, gear_pos)
    return (False, gear_pos)

def sum_part_numbers(grid):
  is_part = False
  gear_pos = ()
  for row, line in enumerate(grid):
    current_number = ""
    is_part = False
    for col, char in enumerate(line):
      if char.isdigit():
        current_number += char
        if (not is_part):
            is_part, gear_pos = is_valid_part(grid, row, col, gear_pos)
        if is_part and col == len(line) - 1: # part is at the end of the line
          gear_map.setdefault(gear_pos, []).append(current_number)
      elif current_number:
        # add/update gear_map with gear position (i, j) and part number (grid[row][col])
        if is_part:
          gear_map.setdefault(gear_pos, []).append(current_number)
        current_number = ""
        gear_pos = ()
        is_part = False

def sum_gear_ratios():
  """
  For every gear in gear_map, if it has 2 part numbers, multiply them together.
  Add up all gear ratios.
  """
  gear_ratio_sum = 0
  for gear_pos, parts_list in gear_map.items():
    #  print(parts_list)
      if len(parts_list) == 2:
        gear_ratio_sum += math.prod(int(part) for part in parts_list)
      else:
        print(gear_pos, parts_list)
  return gear_ratio_sum
  

# Read the input file
grid = read_input(group=True)[0]

# Sum all part numbers
part_number_sum = sum_part_numbers(grid)


print(f"Sum of all gear ratios: {sum_gear_ratios()}")
