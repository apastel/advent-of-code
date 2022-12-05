with open("2020/input/day3.txt") as f:
    grid = [[square for square in line] for line in f.read().splitlines()]
    row, column = (0, 0)
    tree_count = 0
    while row < len(grid):
        curr_pos = grid[row][column % len(grid[0])]
        if curr_pos == "#":
            tree_count += 1
        row += 1
        column += 3

print(tree_count)