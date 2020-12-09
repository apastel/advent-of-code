def traverse(right, down):
    tree_count = 0
    row, column = (0, 0)
    while row < len(grid):
        curr_pos = grid[row][column % len(grid[0])]
        if curr_pos == "#":
            tree_count += 1
        row += down
        column += right
    return tree_count
    
if __name__ == "__main__":
    with open("2020/input/day3.txt") as f:
        grid = [[square for square in line] for line in f.read().splitlines()]
        print(traverse(1, 1) * traverse(3, 1) * traverse(5, 1) * traverse(7, 1) * traverse(1, 2))