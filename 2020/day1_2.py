import itertools

entries = open("input/day1.txt", "r").readlines()
entries = [int(i) for i in entries]
for pair in itertools.combinations(entries, 3):
    if pair[0] + pair[1] + pair[2] == 2020:
        print(f"{pair[0]} + {pair[1]} + {pair[2]} = 2020")
        print(f"{pair[0]} * {pair[1]} * {pair[2]} = {pair[0] * pair[1] * pair[2]}")