ROWS = [x for x in range(128)]
COLS = [x for x in range(8)]

if __name__ == "__main__":
    with open("2020/input/day5.txt") as f:
        lines = f.read().splitlines()
        seat_IDs = []
        for line in lines:
            row_set = line[:7]
            col_set = line[7:]
            possible_rows = ROWS
            possible_cols = COLS
            for char in row_set:
                if char == "F":
                    possible_rows = possible_rows[:int(len(possible_rows) / 2)]
                elif char == "B":
                    possible_rows = possible_rows[int(len(possible_rows) / 2):]
            for char in col_set:
                if char == "L":
                    possible_cols = possible_cols[:int(len(possible_cols) / 2)]
                elif char == "R":
                    possible_cols = possible_cols[int(len(possible_cols) / 2):]
            seat_id = possible_rows[0] * 8 + possible_cols[0]
            seat_IDs.append(seat_id)
        
        seat_IDs.sort()
        compare_set = [x for x in range(84, 902)]
        print(set(compare_set) - set(seat_IDs))
